from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AddComment
from .models import Comment


class CommentsView(ListView):
    model = Comment
    template_name = 'comments/comment_list.html'
    context_object_name = 'comments'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Отзывы'
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


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = AddComment
    template_name = 'comments/update_comment.html'
    success_url = '/comments/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        else:
            return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comments/delete_confirm.html'
    success_url = '/'

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        else:
            return False
