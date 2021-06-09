from django.db.models import fields
from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id')
        read_only_fields = ('username', 'id')
