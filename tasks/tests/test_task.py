import pytest

from django.urls import reverse
from rest_framework import status

pytestmark = [
    pytest.mark.django_db,
]


def test_answer_task(create_user, create_task, task_data, api_client):
    user = create_user
    task = create_task
    task_data = task_data

    assert task.decision == task_data['decision']

    api_client.force_authenticate(user=user)

    url = reverse('user-task-in-user-update')

    response = api_client.patch(
        url, {'answer': task_data['decision'], 'task_id': task.id}, format='json')

    assert response.status_code == 201
