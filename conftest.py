import pytest
from pytest import fixture

from django.contrib.auth import get_user_model

from tasks.models import Task

from rest_framework.test import APIClient


User = get_user_model()


@fixture()
def create_user():
    user = User.objects.create(
        username='test',
        password='testpassword',
        email='testemail@gmail.com'
    )
    user.is_active = True
    user.save()

    return user


@fixture()
def create_task():
    ...


@pytest.fixture()
def api_client():
    return APIClient()
