from rest_framework import serializers
from .models import Cake, Category


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ('id', 'name', 'description', 'text', 'image', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'image', 'icon')
