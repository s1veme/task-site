from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('token-create/', obtain_jwt_token, name='token'),
]
