from django.db import models


class ArticleTopic(models.Model):
    title = models.CharField(max_length=256, verbose_name='Тема статьи')

    def __str__(self):
        return self.title


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    article_topic = models.ManyToManyField(ArticleTopic, verbose_name='Тема статьи')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
