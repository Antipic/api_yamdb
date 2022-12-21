from rest_framework import serializers
from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания User-a"""

    class Meta:
        model = User
        fields = (
            'username', 'email'
        )
        username = serializers.RegexField(
            regex=r'^[\w.@+-]+$',
            max_length=150,
            required=True
        )
        email = serializers.CharField(
            max_length=254,
            required=True
        )

    def validate_username(self, username):

        if username in 'me':
            raise serializers.ValidationError(
                'Использовать имя me запрещено!'
            )
        return username
    # def validate(self, data):
    #     print("-------------")
    #     return data


class UserRecieveJWTSerializer(serializers.Serializer):
    """Сериализатор для получения токена JWT."""

    username = serializers.RegexField(
        regex=r'^[\w.@+-]+$',
        max_length=150,
        required=True
    )
    confirmation_code = serializers.CharField(
        max_length=150,
        required=True
    )



class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role'
        )

    def validate_username(self, username):
        if username in 'me':
            raise serializers.ValidationError(
                'Использовать имя me запрещено!'
            )
        return username
