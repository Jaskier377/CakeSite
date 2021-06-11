from rest_framework import serializers
from .models import Cake, Category


class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake
        fields = ('name', 'description', 'text', 'image', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'image', 'icon')

