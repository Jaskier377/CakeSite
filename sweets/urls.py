from django.urls import path
from .views import HomePage, CakeByCategory, CakeDetail

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('sweets/<slug:slug>/', CakeByCategory.as_view(), name='cake_by_category'),
    path('cake/<slug:slug>/', CakeDetail.as_view(), name='cake_detail'),
]
