from rest_framework import serializers
from .models import TwelveMonthAnalysis, TwelveMonthAnalysisStore, AnalysisGradeOne, Action


class TwelveMonthAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwelveMonthAnalysis
        fields = '__all__'


class TwelveMonthAnalysisStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwelveMonthAnalysisStore
        fields = '__all__'


class AnalysisGradeOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisGradeOne
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = (
            'id',
            'product_code',
            'action_number',
            'action_type',
            'action_target',
            'action_created_date',
            'action_start_date',
            'action_end_date',
            'action_lift',
            'action_margin_impact',
            'action_verdict',
            'created_by',
            'notes',
        )
        read_only_fields = ('id', 'action_number')
        validators = []