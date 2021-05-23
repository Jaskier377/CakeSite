from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import AddComment
from django import forms
from .models import Comment


class CommentsView(ListView):
    model = Comment
    template_name = 'comments/comment_list.html'
    context_object_name = 'comments'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Комментарии'
        return context


class CommentDetailView(DetailView):
    model = Comment
    context_object_name = 'comment'


class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = AddComment
    template_name = 'comments/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)