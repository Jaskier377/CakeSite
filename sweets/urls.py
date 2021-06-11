from django.urls import path
from .views import HomePage, CakeByCategory, CakeDetail, registration, user_login, \
    user_logout, UserChangePasswordView

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path('', HomePage.as_view(), name='home'),
    path('sweets/<int:category_id>/', CakeByCategory.as_view(), name='cake_by_category'),
    path('cake/<int:pk>/', CakeDetail.as_view(), name='cake_detail'),

    path('account/password_change/', UserChangePasswordView.as_view(), name='change_pass'),
]
