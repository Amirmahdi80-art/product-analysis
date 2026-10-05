from rest_framework import serializers
from .models import (
    TwelveMonthAnalysis,
    TwelveMonthAnalysisStore,
    AnalysisGradeOne,
    Action,
)


class TwelveMonthAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwelveMonthAnalysis
        fields = "__all__"


class TwelveMonthAnalysisStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwelveMonthAnalysisStore
        fields = "__all__"


class AnalysisGradeOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisGradeOne
        fields = "__all__"


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = (
            "id",
            "product_code",
            "action_number",
            "action_type",
            "action_target",
            "action_created_date",
            "action_start_date",
            "action_end_date",
            "action_lift",
            "action_margin_impact",
            "action_verdict",
            "created_by",
            "notes",
        )
        read_only_fields = ("id", "action_number")
        validators = []
        extra_kwargs = {
            "action_created_date": {"required": False},
            "action_start_date": {"required": False},
            "action_end_date": {"required": False, "allow_null": True},
            "action_target": {"required": False, "allow_null": True},
            "measurement_start_date": {"required": False, "allow_null": True},
            "measurement_end_date": {"required": False, "allow_null": True},
            "action_lift": {"required": False, "allow_null": True},
            "action_margin_impact": {"required": False, "allow_null": True},
            "action_verdict": {"required": False, "allow_null": True},
            "created_by": {"required": False, "allow_null": True},
            "notes": {"required": False, "allow_null": True},
        }
