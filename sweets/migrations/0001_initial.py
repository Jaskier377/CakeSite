# Generated by Django 3.2.2 on 2021-07-15 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Категория')),
                ('image', models.ImageField(blank=True, upload_to='category_pic/%y/%m/%d/', verbose_name='Фото категории')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.CharField(max_length=200, verbose_name='Краткое описание')),
                ('text', models.TextField(verbose_name='Полное описание')),
                ('image', models.ImageField(null=True, upload_to='photos/%y/%m/%d/', verbose_name='Фото')),
                ('slug', models.SlugField(unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sweets.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Сладость',
                'verbose_name_plural': 'Сладости',
            },
        ),
    ]
