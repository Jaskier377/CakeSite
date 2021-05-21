from .models import Cake, Category
from rest_framework import serializers


class CakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cake
        fields = ['id', 'url', 'name', 'description', 'text', 'image', 'category']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'url', 'title', 'image', 'icon']
