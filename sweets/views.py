from django.views.generic import ListView, DetailView
from .models import Cake, Category


class HomePage(ListView):
    model = Category
    template_name = 'sweets/index.html'
    context_object_name = 'category'

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
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Cake.objects.filter(slug=self.kwargs['slug'])


class CakeDetail(DetailView):
    model = Cake
    template_name = 'sweets/cake_detail.html'
    context_object_name = 'cake_item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Cake.objects.get(slug=self.kwargs['slug'])
        return context
