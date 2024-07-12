from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, status as status_code, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Word
from .permissions import IsAuthorOrReadOnly
from .services.client import client
from .services.find_subtopics import find_subtopics
from .services.generate_plan_2 import generate_plan
from .serializers import PlanWriteSerializer, PlanReadSerializer, WordReadSerializer

MAX_SUBTOPICS = 11

@extend_schema(tags=['Plans'])
@extend_schema_view(
    generate=extend_schema(
        summary='Создание плана'
    ),
    rebuild=extend_schema(
        summary='Обновление плана'
    ),
    approve=extend_schema(
        summary='Одобрение плана'
    )
)
class PlanViewSet(viewsets.GenericViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.action in ("generate",):
            return PlanWriteSerializer
        return PlanReadSerializer

    @action(detail=False, methods=['post'])
    def generate(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            work_type = data['work_type']
            language_of_work = data['language_of_work']
            work_theme = data['work_theme']
            discipline = data['discipline']
            page_count = data['page_count']
            wishes = data['wishes']

            cover_page_data = data['cover_page_data']

            if cover_page_data == "3":
                university = " "
                author_name = "___________________________"
                group_name = "___________________________"
                teacher_name = "___________________________"
            else:
                university = data.get('university', '')
                author_name = data.get('author_name', '')
                group_name = data.get('group_name', '')
                teacher_name = data.get('teacher_name', '')

            subtopics, context = self.generate_plan_and_subtopics(
                client=client,
                language_of_work=language_of_work,
                work_theme=work_theme,
                discipline=discipline,
                work_type=work_type,
                page_count=page_count,
                wishes=wishes,
            )

            if len(subtopics) == MAX_SUBTOPICS:
                plan = Word.objects.create(
                    work_type=work_type,
                    language_of_work=language_of_work,
                    work_theme=work_theme,
                    discipline=discipline,
                    page_count=page_count,
                    wishes=wishes,

                    cover_page_data=cover_page_data,
                    university=university,
                    author_name=author_name,
                    group_name=group_name,
                    teacher_name=teacher_name,

                    subtopics=subtopics,
                    context=context,

                    author=self.request.user
                )

                response_serializer = PlanReadSerializer(plan)
                return Response(response_serializer.data,
                                status=status_code.HTTP_201_CREATED)
            else:
                return Response({"error": "Subtopic generation failed"},
                                status=status_code.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,
                        status=status_code.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def rebuild(self, request, pk=None):
        try:
            plan = Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            return Response(status=status_code.HTTP_404_NOT_FOUND)

        subtopics, context = self.generate_plan_and_subtopics(
            client=client,
            language_of_work=plan.language_of_work,
            work_theme=plan.work_theme,
            discipline=plan.discipline,
            work_type=plan.work_type,
            page_count=plan.page_count,
            wishes=plan.wishes,
        )

        if len(subtopics) == MAX_SUBTOPICS:
            plan.subtopics = subtopics
            plan.context = context
            plan.save()

            serializer = PlanReadSerializer(plan)
            return Response(serializer.data)
        else:
            return Response({"error": "Subtopic generation failed"},
                            status=status_code.HTTP_400_BAD_REQUEST)

    @staticmethod
    def generate_plan_and_subtopics(*args, **kwargs):
        chatbot_response, context = generate_plan(**kwargs)
        subtopics = find_subtopics(chatbot_response, kwargs['language_of_work'])

        return subtopics, context


@extend_schema(tags=['Documents'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить список документов для автора'
    ),
    destroy=extend_schema(
        summary='Удалить документ'
    )
)
class WordViewSet(viewsets.GenericViewSet,
                  viewsets.mixins.DestroyModelMixin,
                  viewsets.mixins.ListModelMixin):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = WordReadSerializer

    def get_queryset(self):
        user = self.request.user
        return Word.objects.filter(author=user)
