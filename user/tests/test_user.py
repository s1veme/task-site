import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core import mail
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()

pytestmark = [
    pytest.mark.django_db,
]


def test_create_user():
    api = APIClient(enforce_csrf_checks=True)

    username = 'test_user'
    password = 'test_user_password'
    email = 'necicada.test@gmail.com'

    user_data = {
        'username': username,
        'password': password,
        'email': email
    }

    url = reverse('user-list')
    response = api.post(url, user_data, format='json')
    content = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1
    assert len(mail.outbox) == 1

    user = User.objects.get(id=content['id'])

    assert user.username == user_data['username']
    assert user.email == user_data['email']

    html_mail_body = mail.outbox[0].alternatives[0][0]

    data_email_list = html_mail_body.split('___')

    url = reverse('user-activation')

    data = {
        'uid': data_email_list[1],
        'token': data_email_list[2]
    }

    response = api.post(url, data, format='json')
    user.refresh_from_db()

    assert response.status_code == 204
    assert user.is_active is True

    user_data = {
        'email': email,
        'password': password
    }

    url = reverse('obtain_jwt_token')
    response = api.post(url, user_data, format='json')

    assert response.status_code == 200
    assert 'token' in response.json()
