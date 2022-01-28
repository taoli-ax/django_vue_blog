from rest_framework import serializers
from .models import Article
# from rest_framework import mixins
# from rest_framework import generics
import sys

sys.path.append('..')
# 父类变成了 ModelSerializer
from user_info.serializers import UserDescSerializer


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)

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
