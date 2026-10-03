from django.contrib import admin
from django.urls import path, include
from salesoptimizer.views import analysis_grade_one_page, store_analysis, product_detail_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('salesoptimizer.urls')),
    path('analysis/', analysis_grade_one_page, name='analysis-grade-one-page'),
    path('store_analysis/', store_analysis, name='store-analysis'),
    path('product/<str:product_code>/', product_detail_page, name='product-detail'),
]

admin.site.site_header = "Product Cycle Analysis API"
admin.site.site_title = "API Source GUI"
admin.site.index_title = "API Source GUI"

