from rest_framework.response import Response

from user.models import User
from .serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework import status

from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from tasks.models import Task

from django.db.models import F


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  GenericViewSet):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'username'

    def get_queryset(self):
        return User.objects.filter(is_active=True)

    @action(detail=False, methods=['PATCH'], permission_classes=[IsAuthenticated])
    def task_in_user_update(self, request):
        task_id = int(request.data.get('task_id'))
        answer = str(request.data.get('answer'))

        task = Task.objects.get(id=task_id)

        if not task_id \
                or not answer \
                or request.user.tasks.filter(id=task_id).exists():
            return Response(status=status.HTTP_204_NO_CONTENT)

        if answer == task.decision:
            request.user.number_of_points = F(
                'number_of_points') + task.number_of_points
            request.user.tasks.add(task_id)
            request.user.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def profile(self, request):
        serializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)
