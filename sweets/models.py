from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Cake(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Краткое описание')
    text = models.TextField(verbose_name='Полное описание')
    image = models.ImageField(upload_to='photos/%y/%m/%d/', verbose_name='Фото', null=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, verbose_name='Категория')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('cake_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сладость'
        verbose_name_plural = 'Сладости'


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')
    image = models.ImageField(upload_to='category_pic/%y/%m/%d/', blank=True, verbose_name='Фото категории')
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('cake_by_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
