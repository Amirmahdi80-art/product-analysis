from rest_framework import serializers

from .models import TwelveMonthAnalysis, TwelveMonthAnalysisStore, AnalysisGradeOne


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