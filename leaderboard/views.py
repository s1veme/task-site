from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .serializers import LeaderSerializer

from authentication.models import User


class LeaderTable(ListAPIView):
    serializer_class = LeaderSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        return LeaderSerializer(User.objects.order_by('number_of_points'), many=True)
