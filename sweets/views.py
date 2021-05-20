from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cake, Category


class HomePage(ListView):
    model = Category
    template_name = 'sweets/index.html'
    context_object_name = 'category'

    # paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class CakeByCategory(ListView):
    model = Cake
    template_name = 'sweets/cake_by_category.html'
    context_object_name = 'cake'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Cake.objects.filter(category_id=self.kwargs['category_id'])


class CakeDetail(DetailView):
    model = Cake
    template_name = 'sweets/cake_detail.html'
    context_object_name = 'cake_item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Cake.objects.get(pk=self.kwargs['pk'])
        return context
