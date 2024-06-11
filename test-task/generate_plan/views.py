from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, status
from rest_framework.response import Response

from generate_plan.client import client
from generate_plan.generate_plan_2 import generate_plan
from generate_plan.models import Plan
from generate_plan.serializers import PlanWriteSerializer, PlanReadSerializer


@extend_schema(tags=['Plans'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список планов'
    ),
    create=extend_schema(
        summary='Создание плана'
    ),
)
class PlanViewSet(viewsets.GenericViewSet,
                  viewsets.mixins.ListModelMixin,
                  viewsets.mixins.CreateModelMixin):
    queryset = Plan.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Получаем данные из сериализатора
            data = serializer.validated_data
            chatbot_response, context = generate_plan(
                client,
                data['language_of_work'],
                data['work_theme'],
                data['discipline'],
                data['university'],
                data['work_type'],
                data['author_name'],
                data['group_name'],
                data['teacher_name'],
                data['page_count'],
                data['wishes'],
                data['cover_page_data']
            )
            # Создаем и сохраняем запись в базе данных
            plan = Plan.objects.create(
                language_of_talk=data['language_of_talk'],
                work_type=data['work_type'],
                language_of_work=data['language_of_work'],
                work_theme=data['work_theme'],
                discipline=data['discipline'],
                page_count=data['page_count'],
                wishes=data['wishes'],
                cover_page_data=data['cover_page_data'],
                university=data.get('university', ''),
                author_name=data.get('author_name', ''),
                group_name=data.get('group_name', ''),
                teacher_name=data.get('teacher_name', ''),
                chatbot_response=chatbot_response
            )

            return Response(PlanReadSerializer(plan).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return PlanWriteSerializer
        return PlanReadSerializer
