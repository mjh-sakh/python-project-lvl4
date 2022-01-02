import random

import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from task_manager import views


@pytest.fixture(scope='session')
def client():
    return Client()


def test_homepage_status_code_and_name_and_template(rf, client):
    response = client.get('/')
    assert response.status_code == 200

    response = client.get(reverse('home'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')



# def test_test(rf):
#     # request:
#     request = rf.get('users')
#     response = views.UsersView.as_view()(request)
#     assert response.status_code == 200

#
# @pytest.mark.django_db
# @pytest.fixture(scope='session')
# def temp_user_in_BD():
#     users = get_user_model()
#     username = f'test_user_{random.randint(1E9, 1E20)}'
#     first_name = 'Test'
#     last_name = 'User'
#     password = 'no secrets here'
#     tmp_user = users(username=username, first_name=first_name, last_name=last_name)
#     tmp_user.set_password(password)
#     tmp_user.exposed_password = password
#     tmp_user.save()
#     yield
#     tmp_user.delete()

#
# def test_user_get_authenticated(django_client, temp_user_in_BD):
#     response = django_client.post('login/', {
#         'username': temp_user_in_BD.username,
#         'password': temp_user_in_BD.exposed_passwrod,
#         })
#     assert response.status_code == 200
