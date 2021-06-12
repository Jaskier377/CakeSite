import pytest
from django import urls
from django.contrib.auth import get_user_model


@pytest.mark.django_db
@pytest.mark.parametrize('param', ['home', 'login', 'registration'])
def test_sweet_view(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_signup(client, user_data_registration):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    signup_url = urls.reverse('registration')
    resp = client.post(signup_url, data=user_data_registration)
    assert user_model.objects.count() == 1
    assert resp.status_code == 302


@pytest.mark.django_db
def test_user_login(client, create_test_user, user_data_login):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('login')
    resp = client.post(login_url, data=user_data_login)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('home')


@pytest.mark.django_db
def test_user_logout(client, auth_user):
    logout_url = urls.reverse('logout')
    resp = client.get(logout_url)
    assert resp.status_code == 302
    assert resp.url == urls.reverse('login')
