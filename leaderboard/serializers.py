from django.db.models import fields
from rest_framework import serializers

from authentication.models import User


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
