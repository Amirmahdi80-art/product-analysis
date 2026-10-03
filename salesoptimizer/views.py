from django.utils.dateparse import parse_date
from rest_framework import viewsets
from django.shortcuts import render

from .models import TwelveMonthAnalysis, TwelveMonthAnalysisStore, AnalysisGradeOne
from .serializers import (
    TwelveMonthAnalysisSerializer,
    TwelveMonthAnalysisStoreSerializer,
    AnalysisGradeOneSerializer
)


class ProductFilterMixin:
    """
    Shared filtering for both endpoints:
      - product_code (single, repeated, or comma-separated)
      - category_code
      - from / to (date range on first_show_date)
    """

    date_field = 'first_show_date'

    def _split_multi(self, value):
        return [v for v in value.split(',') if v]

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.query_params

        product_codes = self._split_multi(','.join(params.getlist('product_code')))
        if product_codes:
            qs = qs.filter(product_code__in=product_codes)

        category_code = params.get('category_code')
        if category_code:
            qs = qs.filter(category_code=category_code)

        date_from = params.get('from')
        if date_from:
            d = parse_date(date_from)
            if d:
                qs = qs.filter(**{f'{self.date_field}__gte': d})

        date_to = params.get('to')
        if date_to:
            d = parse_date(date_to)
            if d:
                qs = qs.filter(**{f'{self.date_field}__lte': d})

        return qs


class TwelveMonthAnalysisViewSet(ProductFilterMixin, viewsets.ReadOnlyModelViewSet):
    queryset = TwelveMonthAnalysis.objects.all()
    serializer_class = TwelveMonthAnalysisSerializer
    lookup_field = 'product_code'


class TwelveMonthAnalysisStoreViewSet(ProductFilterMixin, viewsets.ReadOnlyModelViewSet):
    queryset = TwelveMonthAnalysisStore.objects.all()
    serializer_class = TwelveMonthAnalysisStoreSerializer
    lookup_field = 'id'

    def get_queryset(self):
        qs = super().get_queryset()
        p = self.request.query_params

        store_id = p.get('sales_office_id')
        if store_id:
            qs = qs.filter(sales_office_id=store_id)

        name = p.get('name')
        if name:
            qs = qs.filter(name=name)

        age = p.get('age_in_months')
        if age not in (None, ''):
            qs = qs.filter(age_in_months=age)

        category_code = p.get('category_code')
        if age not in (None, ''):
            qs = qs.filter(category_code=category_code)

        return qs


class AnalysisGradeOneViewSet(ProductFilterMixin, viewsets.ReadOnlyModelViewSet):
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
    lookup_field = 'product_code'

    def get_queryset(self):
        qs = super().get_queryset()  # product_code, category_code, from/to handled by the mixin
        p = self.request.query_params

        age = p.get('age_in_months')
        if age not in (None, ''):
            qs = qs.filter(age_in_months=age)

        completed = p.get('completed')
        if completed not in (None, ''):
            qs = qs.filter(completed=completed)

        dq = p.get('discount_quality')
        if dq:
            qs = qs.filter(discount_quality=dq)

        st = p.get('status_tag')
        if st:
            qs = qs.filter(status_tag=st)

        ac = p.get('action')
        if ac:
            qs = qs.filter(action=ac)

        category = p.get('name')
        if category:
            category = qs.filter(name=category)

        return qs


def analysis_grade_one_page(request):
    return render(request, 'analysis_grade_one.html')

def store_analysis(request):
    return render(request, 'store_analysis.html')

import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .ai import ai_give_answers, ai_persian_system_prompt

logger = logging.getLogger(__name__)


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