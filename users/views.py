from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from users.models import User
from users.permissions import IsActive
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet-класс для работы с моделью пользователь"""
    permission_classes = [IsAdminUser, IsActive]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        """Переопределение метода create, преобразование пароля в токен"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
