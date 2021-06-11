from .models import Cake, Category
from .serializers import CakeSerializer, CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import permissions


class CakeListApi(ListCreateAPIView):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer
    permission_classes = [permissions.IsAdminUser]


class CakeDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryListApi(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CakeByCategory(ListAPIView):
    serializer_class = CakeSerializer

    def get_queryset(self):
        return Cake.objects.filter(category_id=self.kwargs['category_id'])
