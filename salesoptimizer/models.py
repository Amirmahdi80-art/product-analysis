from django.db import models

class CategoryContrAvgs(models.Model):
    category_name = models.CharField(
        db_column='category_name',
        max_length=100,
        null=True,
        blank=True,
        verbose_name='نام دسته‌بندی',
    )
    category_code = models.CharField(
        db_column='category_code',
        max_length=2,
        primary_key=True,
        verbose_name='کد دسته‌بندی',
    )
    avg_first_month_qty = models.DecimalField(
        db_column='avg_first_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه اول',
    )
    avg_second_month_qty = models.DecimalField(
        db_column='avg_second_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه دوم',
    )
    avg_third_month_qty = models.DecimalField(
        db_column='avg_third_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه سوم',
    )
    avg_forth_month_qty = models.DecimalField(
        db_column='avg_forth_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه چهارم',
    )
    avg_fifth_month_qty = models.DecimalField(
        db_column='avg_fifth_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه پنجم',
    )
    avg_sixth_month_qty = models.DecimalField(
        db_column='avg_sixth_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه ششم',
    )
    avg_seventh_month_qty = models.DecimalField(
        db_column='avg_seventh_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه هفتم',
    )
    avg_eighth_month_qty = models.DecimalField(
        db_column='avg_eighth_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه هشتم',
    )
    avg_ninth_month_qty = models.DecimalField(
        db_column='avg_ninth_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه نهم',
    )
    avg_tenth_month_qty = models.DecimalField(
        db_column='avg_tenth_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه دهم',
    )
    avg_eleventh_month_qty = models.DecimalField(
        db_column='avg_eleventh_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه یازدهم',
    )
    avg_twelveth_month_qty = models.DecimalField(
        db_column='avg_twelveth_month_qty',
        max_digits=47,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین مقدار ماه دوازدهم',
    )
    avg_first_month_per = models.DecimalField(
        db_column='avg_first_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه اول',
    )
    avg_second_month_per = models.DecimalField(
        db_column='avg_second_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه دوم',
    )
    avg_third_month_per = models.DecimalField(
        db_column='avg_third_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه سوم',
    )
    avg_forth_month_per = models.DecimalField(
        db_column='avg_forth_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه چهارم',
    )
    avg_fifth_month_per = models.DecimalField(
        db_column='avg_fifth_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه پنجم',
    )
    avg_sixth_month_per = models.DecimalField(
        db_column='avg_sixth_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه ششم',
    )
    avg_seventh_month_per = models.DecimalField(
        db_column='avg_seventh_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه هفتم',
    )
    avg_eighth_month_per = models.DecimalField(
        db_column='avg_eighth_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه هشتم',
    )
    avg_ninth_month_per = models.DecimalField(
        db_column='avg_ninth_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه نهم',
    )
    avg_tenth_month_per = models.DecimalField(
        db_column='avg_tenth_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه دهم',
    )
    avg_eleventh_month_per = models.DecimalField(
        db_column='avg_eleventh_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه یازدهم',
    )
    avg_twelveth_month_per = models.DecimalField(
        db_column='avg_twelveth_month_per',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد ماه دوازدهم',
    )
    avg_discount_percentage = models.DecimalField(
        db_column='avg_discount_percentage',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد تخفیف',
    )

    class Meta:
        managed = False
        db_table = 'category_contr_avgs'
        verbose_name = 'میانگین سهم دسته‌بندی'
        verbose_name_plural = 'میانگین سهم دسته‌بندی‌ها'


class Color(models.Model):
    id = models.AutoField(
        db_column='id',
        primary_key=True,
        verbose_name='شناسه',
    )
    code = models.CharField(
        db_column='code',
        max_length=255,
        verbose_name='کد',
    )
    color = models.CharField(
        db_column='color',
        max_length=255,
        verbose_name='رنگ',
    )

    class Meta:
        managed = False
        db_table = 'color'
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ‌ها'


class CumulativeProductLookup(models.Model):
    id = models.AutoField(
        db_column='id',
        primary_key=True,
        verbose_name='شناسه',
    )
    parent_code = models.CharField(
        db_column='ParentCode',
        max_length=128,
        null=True,
        blank=True,
        verbose_name='کد والد',
    )
    expr1 = models.CharField(
        db_column='Expr1',
        max_length=512,
        verbose_name='عبارت ۱',
    )
    name = models.CharField(
        db_column='Name',
        max_length=256,
        verbose_name='نام',
    )
    category_code = models.CharField(
        db_column='category_code',
        max_length=2,
        null=True,
        blank=True,
        verbose_name='کد دسته‌بندی',
    )
    expr2 = models.DateTimeField(
        db_column='Expr2',
        verbose_name='عبارت ۲',
    )
    sales_office_id = models.BigIntegerField(
        db_column='SalesOfficeID',
        verbose_name='شناسه دفتر فروش',
    )
    major_unit_quantity = models.DecimalField(
        db_column='MajorUnitQuantity',
        max_digits=28,
        decimal_places=6,
        verbose_name='مقدار واحد اصلی',
    )
    total_inventory = models.DecimalField(
        db_column='total_inventory',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='موجودی کل',
    )
    first_entered_inventory_date = models.DateTimeField(
        db_column='first_entered_inventory_date',
        null=True,
        blank=True,
        verbose_name='تاریخ اولین ورود به انبار',
    )
    first_show_date = models.DateTimeField(
        db_column='first_show_date',
        null=True,
        blank=True,
        verbose_name='تاریخ اولین نمایش',
    )
    days_since_entry = models.IntegerField(
        db_column='days_since_entry',
        null=True,
        blank=True,
        verbose_name='روزهای سپری‌شده از ورود',
    )
    days_since_show = models.IntegerField(
        db_column='days_since_show',
        null=True,
        blank=True,
        verbose_name='روزهای سپری‌شده از نمایش',
    )
    date_diff = models.BigIntegerField(
        db_column='date_diff',
        null=True,
        blank=True,
        verbose_name='تفاوت تاریخ',
    )
    cumulative_qty = models.DecimalField(
        db_column='cumulative_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار تجمعی',
    )
    cumulative_netprice = models.DecimalField(
        db_column='cumulative_netprice',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='قیمت خالص تجمعی',
    )
    cumulative_reduction = models.DecimalField(
        db_column='cumulative_reduction',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='کاهش تجمعی',
    )
    cumulative_addition = models.DecimalField(
        db_column='cumulative_addition',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='افزایش تجمعی',
    )
    cumulative_price = models.DecimalField(
        db_column='cumulative_price',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='قیمت تجمعی',
    )

    class Meta:
        managed = False
        db_table = 'cumulative_product_lookup'
        verbose_name = 'جستجوی محصول تجمعی'
        verbose_name_plural = 'جستجوهای محصول تجمعی'


class InvoiceItems(models.Model):
    invoice_item_id = models.AutoField(
        db_column='InvoiceItemID',
        primary_key=True,
        verbose_name='شناسه آیتم فاکتور',
    )
    party_id = models.BigIntegerField(
        db_column='PartyID',
        verbose_name='شناسه طرف حساب',
    )
    full_name = models.CharField(
        db_column='FullName',
        max_length=202,
        null=True,
        blank=True,
        verbose_name='نام کامل',
    )
    sales_office_id = models.BigIntegerField(
        db_column='SalesOfficeID',
        verbose_name='شناسه دفتر فروش',
    )
    name = models.CharField(
        db_column='Name',
        max_length=256,
        verbose_name='نام',
    )
    invoice_id = models.BigIntegerField(
        db_column='InvoiceID',
        verbose_name='شناسه فاکتور',
    )
    number = models.CharField(
        db_column='Number',
        max_length=100,
        verbose_name='شماره',
    )
    expr2 = models.DateTimeField(
        db_column='Expr2',
        verbose_name='عبارت ۲',
    )
    part_id = models.BigIntegerField(
        db_column='PartID',
        verbose_name='شناسه قطعه',
    )
    code = models.CharField(
        db_column='Code',
        max_length=128,
        verbose_name='کد',
    )
    expr1 = models.CharField(
        db_column='Expr1',
        max_length=512,
        verbose_name='عبارت ۱',
    )
    major_unit_quantity = models.DecimalField(
        db_column='MajorUnitQuantity',
        max_digits=28,
        decimal_places=6,
        verbose_name='مقدار واحد اصلی',
    )
    mobile = models.CharField(
        db_column='Mobile',
        max_length=20,
        null=True,
        blank=True,
        verbose_name='موبایل',
    )
    price = models.DecimalField(
        db_column='Price',
        max_digits=28,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='قیمت',
    )
    reduction_amount = models.DecimalField(
        db_column='ReductionAmount',
        max_digits=28,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مبلغ کاهش',
    )
    addition_amount = models.DecimalField(
        db_column='AdditionAmount',
        max_digits=28,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مبلغ افزایش',
    )
    net_price = models.DecimalField(
        db_column='NetPrice',
        max_digits=28,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='قیمت خالص',
    )
    first_name = models.CharField(
        db_column='FirstName',
        max_length=100,
        null=True,
        blank=True,
        verbose_name='نام',
    )
    last_name = models.CharField(
        db_column='LastName',
        max_length=100,
        null=True,
        blank=True,
        verbose_name='نام خانوادگی',
    )

    class Meta:
        managed = False
        db_table = 'invoiceitems'
        verbose_name = 'آیتم فاکتور'
        verbose_name_plural = 'آیتم‌های فاکتور'


class InvoiceItemsParent(models.Model):
    invoice_item_id = models.IntegerField(
        db_column='InvoiceItemID',
        primary_key=True,
        verbose_name='شناسه آیتم فاکتور',
    )
    party_id = models.BigIntegerField(
        db_column='PartyID',
        verbose_name='شناسه طرف حساب',
    )
    full_name = models.CharField(
        db_column='FullName',
        max_length=202,
        null=True,
        blank=True,
        verbose_name='نام کامل',
    )
    sales_office_id = models.BigIntegerField(
        db_column='SalesOfficeID',
        verbose_name='شناسه دفتر فروش',
    )
    name = models.CharField(
        db_column='Name',
        max_length=256,
        verbose_name='نام',
    )
    invoice_id = models.BigIntegerField(
        db_column='InvoiceID',
        verbose_name='شناسه فاکتور',
    )
    number = models.CharField(
        db_column='Number',
        max_length=100,
        verbose_name='شماره',
    )
    expr2 = models.DateTimeField(
        db_column='Expr2',
        verbose_name='عبارت ۲',
    )
    part_id = models.BigIntegerField(
        db_column='PartID',
        verbose_name='شناسه قطعه',
    )
    parent_code = models.CharField(
        db_column='ParentCode',
        max_length=128,
        null=True,
        blank=True,
        verbose_name='کد والد',
    )
    expr1 = models.CharField(
        db_column='Expr1',
        max_length=512,
        verbose_name='عبارت ۱',
    )
    major_unit_quantity = models.DecimalField(
        db_column='MajorUnitQuantity',
        max_digits=28,
        decimal_places=6,
        verbose_name='مقدار واحد اصلی',
    )
    mobile = models.CharField(
        db_column='Mobile',
        max_length=20,
        null=True,
        blank=True,
        verbose_name='موبایل',
    )
    price = models.DecimalField(
        db_column='Price',
        max_digits=28,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='قیمت',
    )
    reduction_amount = models.DecimalField(
        db_column='ReductionAmount',
        max_digits=28,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مبلغ کاهش',
    )
    addition_amount = models.DecimalField(
        db_column='AdditionAmount',
        max_digits=28,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مبلغ افزایش',
    )
    net_price = models.DecimalField(
        db_column='NetPrice',
        max_digits=28,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='قیمت خالص',
    )
    first_name = models.CharField(
        db_column='FirstName',
        max_length=100,
        null=True,
        blank=True,
        verbose_name='نام',
    )
    last_name = models.CharField(
        db_column='LastName',
        max_length=100,
        null=True,
        blank=True,
        verbose_name='نام خانوادگی',
    )

    class Meta:
        managed = False
        db_table = 'invoiceitems_parent'
        verbose_name = 'آیتم فاکتور والد'
        verbose_name_plural = 'آیتم‌های فاکتور والد'


class ProductCategories(models.Model):
    id = models.AutoField(
        db_column='id',
        primary_key=True,
        verbose_name='شناسه',
    )
    category_code = models.CharField(
        db_column='category_code',
        max_length=2,
        null=True,
        blank=True,
        verbose_name='کد دسته‌بندی',
    )
    category_name = models.CharField(
        db_column='category_name',
        max_length=100,
        null=True,
        blank=True,
        verbose_name='نام دسته‌بندی',
    )

    class Meta:
        managed = False
        db_table = 'product_categories'
        verbose_name = 'دسته‌بندی محصول'
        verbose_name_plural = 'دسته‌بندی‌های محصول'


class ProductsLookup(models.Model):
    product_code = models.CharField(
        db_column='product_code',
        max_length=128,
        primary_key=True,
        verbose_name='کد محصول',
    )
    category_code = models.CharField(
        db_column='category_code',
        max_length=2,
        null=True,
        blank=True,
        verbose_name='کد دسته‌بندی',
    )
    total_inventory = models.DecimalField(
        db_column='total_inventory',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='موجودی کل',
    )
    first_entered_inventory_date = models.DateTimeField(
        db_column='first_entered_inventory_date',
        null=True,
        blank=True,
        verbose_name='تاریخ اولین ورود به انبار',
    )
    first_show_date = models.DateTimeField(
        db_column='first_show_date',
        null=True,
        blank=True,
        verbose_name='تاریخ اولین نمایش',
    )
    days_since_entry = models.IntegerField(
        db_column='days_since_entry',
        null=True,
        blank=True,
        verbose_name='روزهای سپری‌شده از ورود',
    )
    days_since_show = models.IntegerField(
        db_column='days_since_show',
        null=True,
        blank=True,
        verbose_name='روزهای سپری‌شده از نمایش',
    )

    class Meta:
        managed = False
        db_table = 'products_lookup'
        verbose_name = 'جستجوی محصول'
        verbose_name_plural = 'جستجوهای محصول'


class StoreMapping(models.Model):
    id = models.AutoField(
        db_column='id',
        primary_key=True,
        verbose_name='شناسه',
    )
    name = models.CharField(
        db_column='name',
        max_length=100,
        unique=True,
        verbose_name='نام',
    )
    voucher_store_id = models.IntegerField(
        db_column='voucher_store_id',
        unique=True,
        verbose_name='شناسه فروشگاه در سیستم فاکتور',
    )
    invoice_store_id = models.IntegerField(
        db_column='invoice_store_id',
        unique=True,
        verbose_name='شناسه فروشگاه در سیستم فاکتور',
    )

    class Meta:
        managed = False
        db_table = 'store_mapping'
        verbose_name = 'نقشه‌برداری فروشگاه'
        verbose_name_plural = 'نقشه‌برداری فروشگاه‌ها'


class TwelveMonthAnalysis(models.Model):
    product_code = models.CharField(
        db_column='product_code',
        max_length=128,
        primary_key=True,
        verbose_name='کد محصول',
    )
    category_code = models.CharField(
        db_column='category_code',
        max_length=2,
        null=True,
        blank=True,
        verbose_name='کد دسته‌بندی',
    )
    total_inventory = models.DecimalField(
        db_column='total_inventory',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='موجودی کل',
    )
    first_show_date = models.DateTimeField(
        db_column='first_show_date',
        null=True,
        blank=True,
        verbose_name='تاریخ اولین نمایش',
    )
    age_in_months = models.BigIntegerField(
        db_column='age_in_months',
        null=True,
        blank=True,
        verbose_name='سن به ماه',
    )
    age_in_days = models.IntegerField(
        db_column='age_in_days',
        null=True,
        blank=True,
        verbose_name='سن به روز',
    )
    first_month_qty = models.DecimalField(
        db_column='first_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه اول',
    )
    second_month_qty = models.DecimalField(
        db_column='second_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه دوم',
    )
    third_month_qty = models.DecimalField(
        db_column='third_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه سوم',
    )
    forth_month_qty = models.DecimalField(
        db_column='forth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه چهارم',
    )
    fifth_month_qty = models.DecimalField(
        db_column='fifth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه پنجم',
    )
    sixth_month_qty = models.DecimalField(
        db_column='sixth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه ششم',
    )
    seventh_month_qty = models.DecimalField(
        db_column='seventh_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه هفتم',
    )
    eighth_month_qty = models.DecimalField(
        db_column='eighth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه هشتم',
    )
    ninth_month_qty = models.DecimalField(
        db_column='ninth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه نهم',
    )
    tenth_month_qty = models.DecimalField(
        db_column='tenth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه دهم',
    )
    eleventh_month_qty = models.DecimalField(
        db_column='eleventh_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه یازدهم',
    )
    twelveth_month_qty = models.DecimalField(
        db_column='twelveth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه دوازدهم',
    )
    first_month_per = models.DecimalField(
        db_column='first_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه اول',
    )
    second_month_per = models.DecimalField(
        db_column='second_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه دوم',
    )
    third_month_per = models.DecimalField(
        db_column='third_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه سوم',
    )
    forth_month_per = models.DecimalField(
        db_column='forth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه چهارم',
    )
    fifth_month_per = models.DecimalField(
        db_column='fifth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه پنجم',
    )
    sixth_month_per = models.DecimalField(
        db_column='sixth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه ششم',
    )
    seventh_month_per = models.DecimalField(
        db_column='seventh_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه هفتم',
    )
    eighth_month_per = models.DecimalField(
        db_column='eighth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه هشتم',
    )
    ninth_month_per = models.DecimalField(
        db_column='ninth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه نهم',
    )
    tenth_month_per = models.DecimalField(
        db_column='tenth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه دهم',
    )
    eleventh_month_per = models.DecimalField(
        db_column='eleventh_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه یازدهم',
    )
    twelveth_month_per = models.DecimalField(
        db_column='twelveth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه دوازدهم',
    )
    max_cumulative_reduction = models.DecimalField(
        db_column='max_cumulative_reduction',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='حداکثر کاهش تجمعی',
    )
    max_cumulative_price = models.DecimalField(
        db_column='max_cumulative_price',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='حداکثر قیمت تجمعی',
    )
    discount_percentage = models.DecimalField(
        db_column='discount_percentage',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد تخفیف',
    )
    total_sold_12_months = models.DecimalField(
        db_column='total_sold_12_months',
        max_digits=58,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='مجموع فروش ۱۲ ماه',
    )

    class Meta:
        managed = False
        db_table = 'twelve_month_analysis'
        verbose_name = 'تحلیل دوازده ماهه'
        verbose_name_plural = 'تحلیل‌های دوازده ماهه'


class TwelveMonthAnalysisStore(models.Model):
    id = models.AutoField(
        db_column='id',
        primary_key=True,
        verbose_name='شناسه',
    )
    product_code = models.CharField(
        db_column='product_code',
        max_length=128,
        null=True,
        blank=True,
        verbose_name='کد محصول',
    )
    sales_office_id = models.BigIntegerField(
        db_column='SalesOfficeID',
        verbose_name='شناسه دفتر فروش',
    )
    name = models.CharField(
        db_column='Name',
        max_length=256,
        verbose_name='نام',
    )
    category_code = models.CharField(
        db_column='category_code',
        max_length=2,
        null=True,
        blank=True,
        verbose_name='کد دسته‌بندی',
    )
    total_inventory = models.DecimalField(
        db_column='total_inventory',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='موجودی کل',
    )
    first_show_date = models.DateTimeField(
        db_column='first_show_date',
        null=True,
        blank=True,
        verbose_name='تاریخ اولین نمایش',
    )
    age_in_months = models.BigIntegerField(
        db_column='age_in_months',
        null=True,
        blank=True,
        verbose_name='سن به ماه',
    )
    age_in_days = models.IntegerField(
        db_column='age_in_days',
        null=True,
        blank=True,
        verbose_name='سن به روز',
    )
    first_month_qty = models.DecimalField(
        db_column='first_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه اول',
    )
    second_month_qty = models.DecimalField(
        db_column='second_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه دوم',
    )
    third_month_qty = models.DecimalField(
        db_column='third_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه سوم',
    )
    forth_month_qty = models.DecimalField(
        db_column='forth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه چهارم',
    )
    fifth_month_qty = models.DecimalField(
        db_column='fifth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه پنجم',
    )
    sixth_month_qty = models.DecimalField(
        db_column='sixth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه ششم',
    )
    seventh_month_qty = models.DecimalField(
        db_column='seventh_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه هفتم',
    )
    eighth_month_qty = models.DecimalField(
        db_column='eighth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه هشتم',
    )
    ninth_month_qty = models.DecimalField(
        db_column='ninth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه نهم',
    )
    tenth_month_qty = models.DecimalField(
        db_column='tenth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه دهم',
    )
    eleventh_month_qty = models.DecimalField(
        db_column='eleventh_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه یازدهم',
    )
    twelveth_month_qty = models.DecimalField(
        db_column='twelveth_month_qty',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='مقدار ماه دوازدهم',
    )
    first_month_per = models.DecimalField(
        db_column='first_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه اول',
    )
    second_month_per = models.DecimalField(
        db_column='second_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه دوم',
    )
    third_month_per = models.DecimalField(
        db_column='third_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه سوم',
    )
    forth_month_per = models.DecimalField(
        db_column='forth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه چهارم',
    )
    fifth_month_per = models.DecimalField(
        db_column='fifth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه پنجم',
    )
    sixth_month_per = models.DecimalField(
        db_column='sixth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه ششم',
    )
    seventh_month_per = models.DecimalField(
        db_column='seventh_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه هفتم',
    )
    eighth_month_per = models.DecimalField(
        db_column='eighth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه هشتم',
    )
    ninth_month_per = models.DecimalField(
        db_column='ninth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه نهم',
    )
    tenth_month_per = models.DecimalField(
        db_column='tenth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه دهم',
    )
    eleventh_month_per = models.DecimalField(
        db_column='eleventh_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه یازدهم',
    )
    twelveth_month_per = models.DecimalField(
        db_column='twelveth_month_per',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد ماه دوازدهم',
    )
    total_sold_12_months = models.DecimalField(
        db_column='total_sold_12_months',
        max_digits=58,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='مجموع فروش ۱۲ ماه',
    )
    best_store = models.BooleanField(
        db_column='best_store',
        default=False,
        verbose_name="بهترین فروشگاه"
    )

    class Meta:
        managed = False
        db_table = 'twelve_month_analysis_store'
        verbose_name = 'تحلیل دوازده ماهه فروشگاه'
        verbose_name_plural = 'تحلیل‌های دوازده ماهه فروشگاه'


class AnalysisGradeOne(models.Model):
    product_code = models.CharField(
        db_column='product_code',
        max_length=128,
        primary_key=True,
        verbose_name='کد محصول',
    )
    category_code = models.CharField(
        db_column='category_code',
        max_length=2,
        null=True,
        blank=True,
        verbose_name='کد دسته‌بندی',
    )
    age_in_months = models.BigIntegerField(
        db_column='age_in_months',
        null=True,
        blank=True,
        verbose_name='سن به ماه',
    )
    age_in_days = models.IntegerField(
        db_column='age_in_days',
        null=True,
        blank=True,
        verbose_name='سن به روز',
    )
    total_inventory = models.DecimalField(
        db_column='total_inventory',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='موجودی کل',
    )
    total_sold_12_months = models.DecimalField(
        db_column='total_sold_12_months',
        max_digits=58,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='مجموع فروش ۱۲ ماه',
    )
    remaining_inventory = models.DecimalField(
        db_column='remaining_inventory',
        max_digits=51,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='موجودی باقی‌مانده',
    )
    remaining_months = models.BigIntegerField(
        db_column='remaining_months',
        null=True,
        blank=True,
        verbose_name='ماه‌های باقی‌مانده',
    )
    cumulative_sell_through = models.DecimalField(
        db_column='cumulative_sell_through',
        max_digits=65,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='نرخ فروش تجمعی',
    )
    benchmark_cumulative_sell_through = models.DecimalField(
        db_column='benchmark_cumulative_sell_through',
        max_digits=65,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='نرخ فروش تجمعی مرجع',
    )
    rstr = models.DecimalField(
        db_column='rstr',
        max_digits=65,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='RSTR',
    )
    cdr = models.DecimalField(
        db_column='cdr',
        max_digits=65,
        decimal_places=10,
        null=True,
        blank=True,
        verbose_name='CDR',
    )
    rvr = models.DecimalField(
        db_column='rvr',
        max_digits=56,
        decimal_places=10,
        null=True,
        blank=True,
        verbose_name='RVR',
    )
    vt = models.CharField(
        db_column='vt',
        max_length=17,
        default='',
        verbose_name='VT',
    )
    discount_percentage = models.DecimalField(
        db_column='discount_percentage',
        max_digits=56,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='درصد تخفیف',
    )
    avg_discount_percentage = models.DecimalField(
        db_column='avg_discount_percentage',
        max_digits=57,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='میانگین درصد تخفیف',
    )
    dd = models.DecimalField(
        db_column='dd',
        max_digits=58,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name='DD',
    )
    discount_quality = models.CharField(
        db_column='discount_quality',
        max_length=10,
        default='',
        verbose_name='کیفیت تخفیف',
    )
    current_velocity = models.DecimalField(
        db_column='current_velocity',
        max_digits=50,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name='سرعت فروش فعلی',
    )
    required_future_velocity = models.DecimalField(
        db_column='required_future_velocity',
        max_digits=55,
        decimal_places=10,
        null=True,
        blank=True,
        verbose_name='سرعت فروش مورد نیاز آینده',
    )
    velocity_gap = models.DecimalField(
        db_column='velocity_gap',
        max_digits=64,
        decimal_places=10,
        null=True,
        blank=True,
        verbose_name='شکاف سرعت فروش',
    )
    completed = models.IntegerField(
        db_column='completed',
        default=0,
        verbose_name='تکمیل‌شده',
    )
    status_tag = models.CharField(
        db_column='status_tag',
        max_length=21,
        default='',
        verbose_name='برچسب وضعیت',
    )
    action = models.CharField(
        db_column='action',
        max_length=11,
        default='',
        verbose_name='اقدام',
    )
    active_action = models.CharField(
        db_column='active_action',
        max_length=32,
        null=True,
        blank=True,
        verbose_name='اقدام فعال',
    )
    active_action_start_date = models.DateField(
        db_column='active_action_start_date',
        null=True,
        blank=True,
        verbose_name='تاریخ شروع اقدام فعال',
    )
    active_action_end_date = models.DateField(
        db_column='active_action_end_date',
        null=True,
        blank=True,
        verbose_name='تاریخ پایان اقدام فعال',
    )
    action_count_total = models.BigIntegerField(
        db_column='action_count_total',
        null=True,
        blank=True,
        verbose_name='تعداد کل اقدامات',
    )
    action_count_measured = models.BigIntegerField(
        db_column='action_count_measured',
        null=True,
        blank=True,
        verbose_name='تعداد اقدامات اندازه‌گیری‌شده',
    )
    last_action = models.CharField(
        db_column='last_action',
        max_length=32,
        null=True,
        blank=True,
        verbose_name='آخرین اقدام',
    )
    last_action_verdict = models.CharField(
        db_column='last_action_verdict',
        max_length=16,
        null=True,
        blank=True,
        verbose_name='نتیجه آخرین اقدام',
    )
    last_action_lift = models.DecimalField(
        db_column='last_action_lift',
        max_digits=12,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name='لیفت آخرین اقدام',
    )
    last_action_margin_impact = models.DecimalField(
        db_column='last_action_margin_impact',
        max_digits=14,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name='تأثیر حاشیه آخرین اقدام',
    )
    actions_remaining = models.IntegerField(
        db_column='actions_remaining',
        null=True,
        blank=True,
        verbose_name='اقدامات باقی‌مانده',
    )
    next_recommended_action = models.CharField(
        db_column='next_recommended_action',
        max_length=32,
        null=True,
        blank=True,
        verbose_name='اقدام پیشنهادی بعدی',
    )
    name = models.CharField(
        db_column='name',
        max_length=100,
        null=True,
        blank=True,
        verbose_name='نام',
    )

    class Meta:
        managed = False
        db_table = 'analysis_grade_one'
        verbose_name = 'تحلیل'
        verbose_name_plural = 'تحلیل'


class Action(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True,
        verbose_name='شناسه',
    )
    product_code = models.CharField(
        db_column='product_code',
        max_length=64,
        verbose_name='کد محصول',
    )
    action_number = models.IntegerField(
        db_column='action_number',
        verbose_name='شماره اقدام',
    )
    action_type = models.CharField(
        db_column='action_type',
        max_length=64,
        verbose_name='نوع اقدام',
    )
    action_target = models.CharField(
        db_column='action_target',
        max_length=64,
        null=True,
        blank=True,
        verbose_name='هدف اقدام',
    )
    action_created_date = models.DateField(
        db_column='action_created_date',
        verbose_name='تاریخ ثبت اقدام',
        auto_now_add=True
    )
    action_start_date = models.DateField(
        db_column='action_start_date',
        verbose_name='تاریخ شروع اقدام',
    )
    action_end_date = models.DateField(
        db_column='action_end_date',
        null=True,
        blank=True,
        verbose_name='تاریخ پایان اقدام',
    )
    action_lift = models.DecimalField(
        db_column='action_lift',
        max_digits=12,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name='لیفت اقدام',
    )
    action_margin_impact = models.DecimalField(
        db_column='action_margin_impact',
        max_digits=14,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name='تأثیر حاشیه اقدام',
    )
    action_verdict = models.CharField(
        db_column='action_verdict',
        max_length=16,
        null=True,
        blank=True,
        verbose_name='نتیجه اقدام',
    )
    created_by = models.CharField(
        db_column='created_by',
        max_length=64,
        null=True,
        blank=True,
        verbose_name='ایجادکننده',
    )
    notes = models.TextField(
        db_column='notes',
        null=True,
        blank=True,
        verbose_name='یادداشت‌ها',
    )

    class Meta:
        managed = False
        db_table = 'actions'
        verbose_name = 'اقدام'
        verbose_name_plural = 'اقدامات'
