from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.routers import DefaultRouter


from .views import (
    TwelveMonthAnalysisViewSet,
    TwelveMonthAnalysisStoreViewSet,
    AnalysisGradeOneViewSet,
    ActionViewSet,
    ai_analyze,
)

router = DefaultRouter()
router.register(
    r"twelve-month-analysis",
    TwelveMonthAnalysisViewSet,
    basename="twelve-month-analysis",
)
router.register(
    r"twelve-month-analysis-store",
    TwelveMonthAnalysisStoreViewSet,
    basename="twelve-month-analysis-store",
)
router.register(
    r"analysis-grade-one",
    AnalysisGradeOneViewSet,
    basename="analysis-grade-one",
)

router.register(
    r"actions",
    ActionViewSet,
    basename="actions",
)

urlpatterns = [
    path("ai/analyze/", ai_analyze, name="ai-analyze"),
] + router.urls
