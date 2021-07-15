from django.contrib import admin
from .models import Cake, Category


class AdminCake(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category',)
    prepopulated_fields = {"slug": ("name",)}


class AdminCategory(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Cake, AdminCake)
admin.site.register(Category, AdminCategory)
