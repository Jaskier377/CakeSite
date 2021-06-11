from django.urls import path
from .views import CakeListApi, CakeDetailApi, CategoryListApi, CategoryDetailApi, CakeByCategory

urlpatterns = [
    path('cake/', CakeListApi.as_view()),
    path('cake/<int:pk>/', CakeDetailApi.as_view()),
    path('category/', CategoryListApi.as_view()),
    path('category/<int:pk>/', CategoryDetailApi.as_view()),
    path('cake_by_category/<int:category_id>/', CakeByCategory.as_view()),
]
