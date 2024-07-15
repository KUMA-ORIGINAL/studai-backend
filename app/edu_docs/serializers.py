from rest_framework import serializers

from .models import Word


class PlanWriteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Word
        fields = [
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
            'teacher_name',
            'author',
        ]


class PlanReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class WordReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'work_theme', 'page_count_display',
                  'work_type_display', 'language_of_work_display', 'status', 'file']
