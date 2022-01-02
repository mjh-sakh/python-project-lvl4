import random

from django.contrib.auth import get_user_model
from django.test import Client
import pytest


@pytest.mark.django_db
@pytest.fixture(scope='session')
def temp_user_in_BD():
    users = get_user_model()
    username = f'test_user_{random.randint(1E9, 1E20)}'
    first_name = 'Test'
    last_name = 'User'
    password = 'no secrets here'
    tmp_user = users(username=username, first_name=first_name, last_name=last_name)
    tmp_user.set_password(password)
    tmp_user.exposed_password = password
    tmp_user.save()
    yield
    tmp_user.delete()

@pytest.fixture(scope='session')
def django_client():
    return Client()

def test_user_get_authenticated(django_client, temp_user_in_BD):
    response = django_client.post('login/', {
        'username': temp_user_in_BD.username,
        'password': temp_user_in_BD.exposed_passwrod,
        })
    assert response.status_code == 200
