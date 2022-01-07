import random

import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed, assertContains
from task_manager import views


def get_response_messages(response):
    return list(response.context['messages'])


@pytest.fixture(scope='function')
def client():
    return Client()


def test_homepage_status_code_and_name_and_template(rf, client):
    response = client.get('/')
    assert response.status_code == 200

    response = client.get(reverse('home'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')


@pytest.mark.django_db
def test_users_page_status_code_and_name_and_template(client):
    response = client.get('/users/', follow=True)
    assert response.status_code == 200

    response = client.get(reverse('users_list'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'users_list.html')


@pytest.mark.django_db
def test_login_page_status_code_and_name_and_template_and_redirection_and_wrong_user_message_and_success_message(rf, client):
    user_credentials = {
        'username': 'test_user',
        'password': 'test_pass',
    }
    wrong_credentials = {
        'username': 'wrong_user',
        'password': 'wrong_pass',
    }

    response = client.get('/login/', follow=True)
    assert response.status_code == 200

    response = client.get(reverse('login'))
    assert response.status_code == 200
    assertTemplateUsed(response, 'login.html')

    user = User.objects.create_user(**user_credentials)
    response = client.post('/login/', data=wrong_credentials, follow=True)
    assertContains(response,
                   'Пожалуйста, введите правильные имя пользователя и пароль')

    response = client.post('/login/', data=user_credentials, follow=True)
    assertTemplateUsed(response, 'index.html')
    messages = get_response_messages(response)
    assert messages[0].tags == 'success'
    assert messages[0].message == 'Рады вас видеть снова'


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
