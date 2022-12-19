# from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import mixins, permissions, status, viewsets
from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.tokens import AccessToken
from users.serializers import (UserCreateSerializer,
                               UserRecieveJWTSerializer,
                               UserSerializer)
from users.permissions import IsSuperUserOrIsAdminOnly
from users.utils import send_confirmation_code

User = get_user_model()


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """Создаем нового User-а."""
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        """Создает User-а и отправляет на почту код подтверждения."""
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, _ = User.objects.get_or_create(**serializer.validated_data)
        confirmation_code = default_token_generator.make_token(user)
        send_confirmation_code(
            email=user.email,
            username=user.username,
            confirmation_code=confirmation_code
        )
        message = serializer.data
        # message['confirmation_code'] = confirmation_code
        return Response(message, status=status.HTTP_200_OK)


class UserReceiveJWTViewSet(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """Получение пользователем JWT токена."""

    queryset = User.objects.all()
    serializer_class = UserRecieveJWTSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        """Предоставляет пользователю JWT токен по коду подтверждения."""
        serializer = UserRecieveJWTSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        confirmation_code = serializer.validated_data.get('confirmation_code')
        user = get_object_or_404(User, username=username)

        if not default_token_generator.check_token(user, confirmation_code):
            message = {'confirmation_code': 'Код невалиден!'}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)
        token = str(AccessToken.for_user(user))
        message = {'token': token}
        return Response(message, status=status.HTTP_200_OK)


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    """Вьюсет для обьектов модели User."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrIsAdminOnly,)
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('username',)
# class UserViewSet(viewsets.ViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'username'
#     """
#     A simple ViewSet for listing or retrieving users.
    # """
    # def list(self, request):
    #     queryset = User.objects.all()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
