from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import admin
import datetime

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # перемещение пользователя после добавление нового поста
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=120)
    title_tag = models.CharField(max_length=120, default=title)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=5000)
    post_date = models.DateField("Date", default=datetime.date.today)
    category = models.CharField(max_length=120, default='Python')
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count() # считаем лайки

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # перемещение пользователя после добавление нового поста
        return reverse('home')

class Comment(models.Model):
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200, verbose_name='текст комментария')

    def __str__(self):
        return self.comment_text[:15]
    