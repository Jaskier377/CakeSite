# import pytest
# from django.contrib.auth import get_user_model
#
#
# @pytest.fixture()
# def user_data_registration():
#     return {'email': 'test@gmail.com', 'username': 'TestUser', 'password1': '12345678qwe', 'password2': '12345678qwe'}
#
#
# @pytest.fixture()
# def user_data_login():
#     return {'username': 'TestUser', 'password': '12345678qwe'}
#
#
# @pytest.fixture
# def create_test_user(user_data_login):
#     user_model = get_user_model()
#     test_user = user_model.objects.create_user(**user_data_login)
#     test_user.set_password(user_data_login.get('password'))
#     return test_user
#
#
# @pytest.fixture
# def auth_user(client, user_data_login):
#     user_model = get_user_model()
#     test_user = user_model.objects.create_user(**user_data_login)
#     test_user.set_password(user_data_login.get('password'))
#     test_user.save()
#     client.login(**user_data_login)
#     return test_user
