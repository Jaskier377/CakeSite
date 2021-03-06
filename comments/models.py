from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def get_absolute_url(self):
        return reverse_lazy('comment_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
