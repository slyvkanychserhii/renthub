from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerializer
from apps.reviews.permissions import IsOwnerOrReadOnly


@extend_schema_view(
    list=extend_schema(summary="Получить список всех отзывов аутентифицированного пользователя",),
    create=extend_schema(summary="Создать новый отзыв",),
    retrieve=extend_schema(summary="Получить детальную информацию об отзыве",),
    update=extend_schema(summary="Обновить отзыв",),
    partial_update=extend_schema(summary="Частично обновить отзыв",),
    destroy=extend_schema(summary="Удалить отзыв",),
)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action == 'list':
            return Review.objects.filter(user=self.request.user)
        return Review.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        elif self.action in ['create']:
            return [permissions.IsAuthenticated()]
        else:
            return [IsOwnerOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
