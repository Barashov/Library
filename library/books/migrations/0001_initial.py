# Generated by Django 4.0.5 on 2022-06-21 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='категория')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='название')),
                ('author', models.CharField(max_length=30, verbose_name='автор')),
                ('file', models.FileField(upload_to='file/', verbose_name='файл книги')),
                ('photo', models.ImageField(upload_to='photo/', verbose_name='фотография')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.categories')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
    ]