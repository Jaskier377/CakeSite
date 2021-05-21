from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
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
