from rest_framework import serializers

from generate_plan.models import Plan


class PlanWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = [
            'language_of_talk',
            'work_type',
            'language_of_work',
            'work_theme',
            'discipline',
            'page_count',
            'wishes',
            'cover_page_data',
            'university',
            'author_name',
            'group_name',
            'teacher_name'
        ]


class PlanReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
