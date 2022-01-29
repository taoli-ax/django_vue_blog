from django.contrib import admin

# Register your models here.
from .models import Article, Category, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    model = Tag
