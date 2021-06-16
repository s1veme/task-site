from os import name
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register('', UserViewSet, basename='user')


urlpatterns = [
    path('token-create/', obtain_jwt_token, name='obtain_jwt_token'),
]

urlpatterns += router.urls
