from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from markdown import Markdown
# Create your models here.


class Tag(models.Model):
    text = models.CharField(max_length=30)

    def __str__(self):
        return self.text

    class Meta:
        ordering =['-id']


class Category(models.Model):
    title = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


# 博客文章 model
class Article(models.Model):
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='articles'
    )
    tag = models.ManyToManyField(Tag,blank=True,related_name='articles')
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    # 标题
    title = models.CharField(max_length=100)
    # 正文
    body = models.TextField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

    def get_md(self):
        md = Markdown(
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc'
            ]
        )
        md_body = md.convert(self.body)
        return md_body, md.toc

