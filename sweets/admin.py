from django.contrib import admin
from .models import Cake, Category


class AdminCake(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category',)


admin.site.register(Cake, AdminCake)
admin.site.register(Category)
