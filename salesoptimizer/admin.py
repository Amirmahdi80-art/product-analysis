from django.contrib import admin

from .models import (
    CategoryContrAvgs,
    Color,
    CumulativeProductLookup,
    InvoiceItems,
    InvoiceItemsParent,
    ProductCategories,
    ProductsLookup,
    StoreMapping,
    TwelveMonthAnalysis,
    TwelveMonthAnalysisStore,
    AnalysisGradeOne,
    Action,
)


@admin.register(CategoryContrAvgs)
class CategoryContrAvgsAdmin(admin.ModelAdmin):
    list_display = ("category_code", "category_name", "avg_discount_percentage")
    search_fields = ("category_code", "category_name")
    ordering = ("category_code",)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "color")
    search_fields = ("code", "color")
    ordering = ("color",)


@admin.register(CumulativeProductLookup)
class CumulativeProductLookupAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "parent_code",
        "name",
        "category_code",
        "sales_office_id",
        "expr2",
        "cumulative_qty",
        "cumulative_price",
    )
    list_filter = ("category_code", "sales_office_id")
    search_fields = ("parent_code", "name", "expr1")
    ordering = ("-id",)
    date_hierarchy = "expr2"
    list_per_page = 50


@admin.register(InvoiceItems)
class InvoiceItemsAdmin(admin.ModelAdmin):
    list_display = (
        "invoice_item_id",
        "invoice_id",
        "code",
        "name",
        "sales_office_id",
        "expr2",
        "major_unit_quantity",
        "net_price",
    )
    list_filter = ("sales_office_id",)
    search_fields = ("code", "name", "number", "full_name", "mobile")
    ordering = ("-invoice_item_id",)
    date_hierarchy = "expr2"
    list_per_page = 50


@admin.register(InvoiceItemsParent)
class InvoiceItemsParentAdmin(admin.ModelAdmin):
    list_display = (
        "invoice_item_id",
        "invoice_id",
        "parent_code",
        "name",
        "sales_office_id",
        "expr2",
        "major_unit_quantity",
        "net_price",
    )
    list_filter = ("sales_office_id",)
    search_fields = ("parent_code", "name", "number", "full_name", "mobile")
    ordering = ("-invoice_item_id",)
    date_hierarchy = "expr2"
    list_per_page = 50


@admin.register(ProductCategories)
class ProductCategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "category_code", "category_name")
    search_fields = ("category_code", "category_name")
    ordering = ("category_code",)


@admin.register(ProductsLookup)
class ProductsLookupAdmin(admin.ModelAdmin):
    list_display = (
        "product_code",
        "category_code",
        "total_inventory",
        "first_show_date",
        "days_since_entry",
        "days_since_show",
    )
    list_filter = ("category_code",)
    search_fields = ("product_code",)
    ordering = ("product_code",)
    date_hierarchy = "first_show_date"
    list_per_page = 50


@admin.register(StoreMapping)
class StoreMappingAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "voucher_store_id", "invoice_store_id")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(TwelveMonthAnalysis)
class TwelveMonthAnalysisAdmin(admin.ModelAdmin):
    list_display = (
        "product_code",
        "category_code",
        "age_in_months",
        "total_sold_12_months",
        "discount_percentage",
        "first_show_date",
    )
    list_filter = ("category_code",)
    search_fields = ("product_code",)
    ordering = ("-total_sold_12_months",)
    date_hierarchy = "first_show_date"
    list_per_page = 50


@admin.register(TwelveMonthAnalysisStore)
class TwelveMonthAnalysisStoreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_code",
        "sales_office_id",
        "name",
        "category_code",
        "age_in_months",
        "total_sold_12_months",
    )
    list_filter = ("category_code", "sales_office_id")
    search_fields = ("product_code", "name")
    ordering = ("-id",)
    list_per_page = 50


@admin.register(AnalysisGradeOne)
class AnalysisGradeOneAdmin(admin.ModelAdmin):
    list_display = (
        "product_code",
        "category_code",
        "status_tag",
        "action",
        "age_in_months",
        "total_sold_12_months",
        "remaining_months",
        "discount_quality",
        "completed",
    )
    list_filter = (
        "category_code",
        "status_tag",
        "action",
        "discount_quality",
        "completed",
    )
    search_fields = ("product_code",)
    ordering = ("product_code",)
    list_per_page = 50


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_code",
        "action_number",
        "action_type",
        "action_target",
        "action_start_date",
        "action_end_date",
        "action_verdict",
        "created_by",
        "action_created_date",
    )
    list_filter = (
        "action_type",
        "action_verdict",
        "action_created_date",
        "action_start_date",
        "action_end_date",
    )
    search_fields = (
        "product_code",
        "action_type",
        "action_target",
        "created_by",
    )
    date_hierarchy = "action_created_date"
    ordering = ("-action_created_date", "-action_number")
    list_per_page = 25

    # Read-only fields (auto-generated or sensitive)
    readonly_fields = ("id", "action_created_date")

    # Group fields nicely on the detail page
    fieldsets = (
        (
            "اطلاعات اصلی",
            {
                "fields": (
                    "id",
                    "product_code",
                    "action_number",
                    "action_type",
                    "action_target",
                )
            },
        ),
        (
            "زمان‌بندی",
            {"fields": ("action_start_date", "action_end_date", "action_created_date")},
        ),
        (
            "نتایج",
            {"fields": ("action_lift", "action_margin_impact", "action_verdict")},
        ),
        ("سایر", {"fields": ("created_by", "notes")}),
    )
