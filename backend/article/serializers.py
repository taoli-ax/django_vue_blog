from rest_framework import serializers
from .models import Article, Category
# from rest_framework import mixins
# from rest_framework import generics
import sys

sys.path.append('..')
# 父类变成了 ModelSerializer
from user_info.serializers import UserDescSerializer


class ArticleCategoryDetailSerializer(serializers.ModelSerializer):
    """给分类详情的嵌套序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = Article
        fields = [
            'url',
            'title',
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    """分类详情"""
    articles = ArticleCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'articles',
        ]


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True,allow_null=True,required=False)

    def validate_category_id(self, values):
        if not Category.objects.filter(id = values).exists() or values is not None:
            raise serializers.as_serializer_error("Category with id {} not exists.")
        return values

    class Meta:
        model = Article
        fields = '__all__'
# class ArticleListSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="article:detail")
#     author = UserDescSerializer(read_only=True)
#
#     class Meta:
#         model = Article
#         fields = [
#             'id',
#             'title',
#             'created',
#             'author',
#             'url',
#         ]
#         # read_only_fields = ['author']
#
#
# class ArticleDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class ArticleDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     """文章详情视图"""
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
