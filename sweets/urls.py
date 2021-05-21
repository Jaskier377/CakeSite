from django.urls import path, include
from rest_framework import routers
from .views import HomePage, CakeByCategory, CakeDetail, CakeViewSet, CategoryViewSet, registration, user_login, user_logout

router = routers.DefaultRouter()
router.register('cakes', CakeViewSet)
router.register('categories', CategoryViewSet)
urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', HomePage.as_view(), name='home'),
    path('sweets/<int:category_id>', CakeByCategory.as_view(), name='cake_by_category'),
    path('cake/<int:pk>', CakeDetail.as_view(), name='cake_detail'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
