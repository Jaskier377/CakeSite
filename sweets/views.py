from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import PasswordChangeView
from .models import Cake, Category
from rest_framework import viewsets
# from .serializers import CakeSerializer, CategorySerializer
from .forms import RegisterUserForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserChangePasswordForm


def registration(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы зарегестрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = RegisterUserForm()
    return render(request, 'sweets/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'sweets/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


# class CakeViewSet(viewsets.ModelViewSet):
#     queryset = Cake.objects.all()
#     serializer_class = CakeSerializer
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class UserChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = UserChangePasswordForm
    template_name = 'sweets/pass_change.html'
    success_url = '/'


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
