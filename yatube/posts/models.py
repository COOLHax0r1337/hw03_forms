from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        help_text='Текст вашего поста'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        help_text='Укажите название группы'
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-pub_date']
