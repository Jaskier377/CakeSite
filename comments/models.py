from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='User', verbose_name='Автор')

    def get_absolute_url(self):
        return reverse_lazy('comment_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']
