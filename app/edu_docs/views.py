from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, status as status_code, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Word
from .permissions import IsAuthorOrReadOnly
from .services.client import client
from .services.create_word_2 import create_word
from .services.find_subtopics import find_subtopics
from .services.generate_plan_2 import generate_plan
from .serializers import PlanWriteSerializer, PlanReadSerializer, WordReadSerializer
from .services.generate_texts_2 import generate_texts
from .services.texts_editor import texts_editor


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
            university = data.get('university', ''),
            author_name = data.get('author_name', ''),
            group_name = data.get('group_name', ''),
            teacher_name = data.get('teacher_name', '')
            page_count = data['page_count']
            wishes = data['wishes']
            cover_page_data = data['cover_page_data']

            subtopics, context = self.generate_plan_and_subtopics(
                client=client,
                language_of_work=language_of_work,
                work_theme=work_theme,
                discipline=discipline,
                university=university,
                work_type=work_type,
                author_name=author_name,
                group_name=group_name,
                teacher_name=teacher_name,
                page_count=page_count,
                wishes=wishes,
                cover_page_data=cover_page_data
            )

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
            return Response(response_serializer.data, status=status_code.HTTP_201_CREATED)
        return Response(serializer.errors, status=status_code.HTTP_400_BAD_REQUEST)

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
            university=plan.university,
            work_type=plan.work_type,
            author_name=plan.author_name,
            group_name=plan.group_name,
            teacher_name=plan.teacher_name,
            page_count=plan.page_count,
            wishes=plan.wishes,
            cover_page_data=plan.cover_page_data
        )

        plan.subtopics = subtopics
        plan.context = context
        plan.save()

        serializer = PlanReadSerializer(plan)
        return Response(serializer.data)


    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        try:
            plan = Word.objects.get(pk=pk)
        except Word.DoesNotExist:
            return Response(status=status_code.HTTP_404_NOT_FOUND)

        subtopic_texts, context = generate_texts(
            client=client,
            language_of_work=plan.language_of_work,
            subtopics=plan.subtopics,
            context=plan.context,
            page_count=plan.page_count
        )
        edited_subtopic_texts = texts_editor(
            subtopic_texts,
            plan.subtopics
        )
        file_path = create_word(
            work_theme=plan.work_theme,
            subtopics=plan.subtopics,
            texts=edited_subtopic_texts,
            university=plan.university,
            work_type=plan.work_type,
            author_name=plan.author_name,
            group_name=plan.group_name,
            teacher_name=plan.teacher_name,
            language_of_work=plan.language_of_work,
            cover_page_data=plan.cover_page_data
        )

        plan.status = True
        plan.file = file_path
        plan.save()

        serializer = PlanReadSerializer(plan)

        return Response(serializer.data)

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
)
class WordViewSet(viewsets.GenericViewSet,
                  viewsets.mixins.ListModelMixin):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = WordReadSerializer

    def get_queryset(self):
        user = self.request.user
        return Word.objects.filter(author=user, status=True)

