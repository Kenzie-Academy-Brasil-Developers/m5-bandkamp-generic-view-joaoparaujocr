from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(
            queryset=User.objects.all(),
        )],
    )
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'password']
        extra_kwargs = { 'password': { 'write_only': True } }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)
        