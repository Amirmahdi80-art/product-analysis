from django.utils.dateparse import parse_date
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404

from .models import (
    TwelveMonthAnalysis,
    TwelveMonthAnalysisStore,
    AnalysisGradeOne,
    TwelveMonthAnalysis,
    TwelveMonthAnalysisStore,
    Action,
)
from .serializers import (
    TwelveMonthAnalysisSerializer,
    TwelveMonthAnalysisStoreSerializer,
    AnalysisGradeOneSerializer,
    ActionSerializer,
)
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta
from django.db.models import Max
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .ai import ai_give_answers, ai_persian_system_prompt

logger = logging.getLogger(__name__)


class ProductFilterMixin:
    """
    Shared filtering for both endpoints:
      - product_code (single, repeated, or comma-separated)
      - category_code
      - from / to (date range on first_show_date)
    """

    date_field = "first_show_date"

    def _split_multi(self, value):
        return [v for v in value.split(",") if v]

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.query_params

        product_codes = self._split_multi(",".join(params.getlist("product_code")))
        if product_codes:
            qs = qs.filter(product_code__in=product_codes)

        category_code = params.get("category_code")
        if category_code:
            qs = qs.filter(category_code=category_code)

        date_from = params.get("from")
        if date_from:
            d = parse_date(date_from)
            if d:
                qs = qs.filter(**{f"{self.date_field}__gte": d})

        date_to = params.get("to")
        if date_to:
            d = parse_date(date_to)
            if d:
                qs = qs.filter(**{f"{self.date_field}__lte": d})

        return qs


class TwelveMonthAnalysisViewSet(ProductFilterMixin, viewsets.ReadOnlyModelViewSet):
    queryset = TwelveMonthAnalysis.objects.all()
    serializer_class = TwelveMonthAnalysisSerializer
    lookup_field = "product_code"


class TwelveMonthAnalysisStoreViewSet(
    ProductFilterMixin, viewsets.ReadOnlyModelViewSet
):
    queryset = TwelveMonthAnalysisStore.objects.all()
    serializer_class = TwelveMonthAnalysisStoreSerializer
    lookup_field = "id"

    def get_queryset(self):
        qs = super().get_queryset()
        p = self.request.query_params

        store_id = p.get("sales_office_id")
        if store_id:
            qs = qs.filter(sales_office_id=store_id)

        name = p.get("name")
        if name:
            qs = qs.filter(name=name)

        age = p.get("age_in_months")
        if age not in (None, ""):
            qs = qs.filter(age_in_months=age)

        category_code = p.get("category_code")
        if age not in (None, ""):
            qs = qs.filter(category_code=category_code)

        return qs


class AnalysisGradeOneViewSet(ProductFilterMixin, viewsets.ModelViewSet):
    """
    GET /api/analysis-grade-one/                       → list
    GET /api/analysis-grade-one/?product_code=...      → filter by product (single/bulk)
    GET /api/analysis-grade-one/?category_code=..      → filter by category
    GET /api/analysis-grade-one/?age_in_months=1..6    → filter by age in months
    GET /api/analysis-grade-one/?completed=0|1         → filter by completed flag
    GET /api/analysis-grade-one/?discount_quality=...  → ORGANIC|SUPPORTED|DEPENDENT|DISTRESSED
    GET /api/analysis-grade-one/?status_tag=...        → e.g. STRONG, RISK, HEALTHY
    GET /api/analysis-grade-one/?action=...            → e.g. ARCHIVE, CLEARANCE, DISCOUNT_50
    GET /api/analysis-grade-one/{product_code}/        → retrieve one
    """

    queryset = AnalysisGradeOne.objects.all()
    serializer_class = AnalysisGradeOneSerializer
    lookup_field = "product_code"
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = (
            super().get_queryset()
        )  # product_code, category_code, from/to handled by the mixin
        p = self.request.query_params

        age = p.get("age_in_months")
        if age not in (None, ""):
            qs = qs.filter(age_in_months=age)

        completed = p.get("completed")
        if completed not in (None, ""):
            qs = qs.filter(completed=completed)

        dq = p.get("discount_quality")
        if dq:
            qs = qs.filter(discount_quality=dq)

        st = p.get("status_tag")
        if st:
            qs = qs.filter(status_tag=st)

        ac = p.get("action")
        if ac:
            qs = qs.filter(action=ac)

        category = p.get("name")
        if category:
            category = qs.filter(name=category)

        return qs


def analysis_grade_one_page(request):
    return render(request, "analysis_grade_one.html")


def store_analysis(request):
    return render(request, "store_analysis.html")


@csrf_exempt
@require_POST
def ai_analyze(request):
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return JsonResponse({"error": "invalid JSON"}, status=400)

    user_prompt = (payload.get("prompt") or "").strip()
    rows = payload.get("rows") or []

    if not user_prompt:
        return JsonResponse({"error": "prompt is required"}, status=400)
    if not isinstance(rows, list) or len(rows) == 0:
        return JsonResponse({"error": "rows must be a non-empty array"}, status=400)
    if len(rows) > 500:
        return JsonResponse({"error": "too many rows (max 500)"}, status=400)

    # Compact JSON keeps the token count down.
    rows_json = json.dumps(rows, ensure_ascii=False, separators=(",", ":"))

    messages = [
        {"role": "system", "content": ai_persian_system_prompt()},
        {
            "role": "user",
            "content": f"{user_prompt}\n\nداده‌ها:\n{rows_json}",
        },
    ]

    try:
        reply = ai_give_answers(messages, temperature=0.4, max_tokens=4000)
    except Exception as e:
        logger.exception("DeepSeek call failed")
        return JsonResponse(
            {"error": "ai call failed", "detail": str(e)},
            status=502,
        )

    return JsonResponse({"reply": reply})


def product_detail_page(request, product_code):
    product = get_object_or_404(TwelveMonthAnalysis, product_code=product_code)

    stores = TwelveMonthAnalysisStore.objects.filter(
        product_code=product_code
    ).order_by("-total_sold_12_months")
    best_store = stores.filter(best_store=True).first()

    analysis = get_object_or_404(AnalysisGradeOne, product_code=product_code)

    # --- monthly series for the charts ---
    monthly_labels = [f"ماه {i}" for i in range(1, 13)]

    monthly_qty = [
        float(product.first_month_qty or 0),
        float(product.second_month_qty or 0),
        float(product.third_month_qty or 0),
        float(product.forth_month_qty or 0),
        float(product.fifth_month_qty or 0),
        float(product.sixth_month_qty or 0),
        float(product.seventh_month_qty or 0),
        float(product.eighth_month_qty or 0),
        float(product.ninth_month_qty or 0),
        float(product.tenth_month_qty or 0),
        float(product.eleventh_month_qty or 0),
        float(product.twelveth_month_qty or 0),
    ]

    monthly_pct = [
        float(product.first_month_per or 0),
        float(product.second_month_per or 0),
        float(product.third_month_per or 0),
        float(product.forth_month_per or 0),
        float(product.fifth_month_per or 0),
        float(product.sixth_month_per or 0),
        float(product.seventh_month_per or 0),
        float(product.eighth_month_per or 0),
        float(product.ninth_month_per or 0),
        float(product.tenth_month_per or 0),
        float(product.eleventh_month_per or 0),
        float(product.twelveth_month_per or 0),
    ]

    # --- AI widget payloads ---
    product_data = {
        "product_code": product.product_code,
        "name": analysis.name or "",
        "category_code": product.category_code,
        "total_inventory": float(product.total_inventory or 0),
        "age_in_months": product.age_in_months,
        "total_sold_12_months": float(product.total_sold_12_months or 0),
        "discount_percentage": float(product.discount_percentage or 0),
        "first_show_date": (
            product.first_show_date.isoformat() if product.first_show_date else None
        ),
    }

    stores_data = [
        {
            "sales_office_id": s.sales_office_id,
            "name": s.name,
            "total_inventory": float(s.total_inventory or 0),
            "age_in_months": s.age_in_months,
            "total_sold_12_months": float(s.total_sold_12_months or 0),
            "best_store": bool(s.best_store),
        }
        for s in stores
    ]

    context = {
        "product": product,
        "stores": stores,
        "best_store": best_store,
        "analysis": analysis,
        "monthly_labels": monthly_labels,
        "monthly_qty": monthly_qty,
        "monthly_pct": monthly_pct,
        "stores_data": stores_data,
        "product_data": product_data,
    }
    return render(request, "product_detail.html", context)


@method_decorator(csrf_exempt, name="dispatch")
class ActionViewSet(viewsets.ModelViewSet):
    """
    GET /api/actions/                          → list (paginated)
    GET /api/actions/{id}/                     → retrieve one

    Filters (all optional, all combinable):
      ?action_type=تخفیف_20
      ?measurement_status=کامل_شده
      ?action_verdict=موثر

    Date range filters (YYYY-MM-DD, inclusive):
      ?created_from=2024-01-01&created_to=2024-06-30
      ?start_from=2024-01-01&start_to=2024-06-30
      ?end_from=2024-01-01&end_to=2024-06-30

    Also accepts the shorter aliases:
      ?from=<date>&to=<date>   → applies to action_created_date
    """

    queryset = Action.objects.all().order_by("-action_created_date", "-id")
    serializer_class = ActionSerializer
    lookup_field = "id"
    authentication_classes = []
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = super().get_queryset()
        p = self.request.query_params

        # --- categorical filters ---
        action_type = p.get("action_type")
        if action_type:
            qs = qs.filter(action_type=action_type)

        product_code = p.get("product_code")
        if product_code:
            qs = qs.filter(product_code=product_code)

        action_verdict = p.get("action_verdict")
        if action_verdict:
            qs = qs.filter(action_verdict=action_verdict)

        # --- date ranges ---
        # created
        created_from = p.get("created_from") or p.get("from")
        if created_from:
            d = parse_date(created_from)
            if d:
                qs = qs.filter(action_created_date__gte=d)

        created_to = p.get("created_to") or p.get("to")
        if created_to:
            d = parse_date(created_to)
            if d:
                qs = qs.filter(action_created_date__lte=d)

        # start
        start_from = p.get("start_from")
        if start_from:
            d = parse_date(start_from)
            if d:
                qs = qs.filter(action_start_date__gte=d)

        start_to = p.get("start_to")
        if start_to:
            d = parse_date(start_to)
            if d:
                qs = qs.filter(action_start_date__lte=d)

        # end
        end_from = p.get("end_from")
        if end_from:
            d = parse_date(end_from)
            if d:
                qs = qs.filter(action_end_date__gte=d)

        end_to = p.get("end_to")
        if end_to:
            d = parse_date(end_to)
            if d:
                qs = qs.filter(action_end_date__lte=d)

        return qs

    def perform_create(self, serializer):
        product_code = serializer.validated_data["product_code"]

        with transaction.atomic():
            # Lock the rows for this product so two concurrent POSTs
            # can't pick the same number.
            last = (
                Action.objects.select_for_update()
                .filter(product_code=product_code)
                .aggregate(m=Max("action_number"))
            )["m"] or 0
            next_number = last + 1

            extra = {"action_number": next_number}
            today = datetime.now().date()
            if not serializer.validated_data.get("action_created_date"):
                extra["action_created_date"] = today
            if not serializer.validated_data.get("action_start_date"):
                extra["action_start_date"] = today
            if not serializer.validated_data.get("action_end_date"):
                extra["action_end_date"] = today + timedelta(days=30)
            if (
                not serializer.validated_data.get("created_by")
                and self.request.user.is_authenticated
            ):
                extra["created_by"] = self.request.user.username

            serializer.save(**extra)


def actions_page(request):
    return render(request, "actions_list.html")
