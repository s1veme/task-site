from rest_framework import serializers

from user.models import User


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'number_of_points')
