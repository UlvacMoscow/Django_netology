from django.contrib import admin
from .models import ArticleTopic

from .models import Article


class ArticleTopicInline(admin.TabularInline):
    model = Article.article_topic.through

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        ArticleTopicInline,
    ]

@admin.register(ArticleTopic)
class ArticleTopicAdmin(admin.ModelAdmin):
    inlines = [
        ArticleTopicInline,
    ]
