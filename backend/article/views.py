from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics, viewsets
from django.http import Http404
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsAdminUserOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return SomeSerializer
    #     else:
    #         return AnotherSerializer

# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAdminUserOrReadOnly]
#     queryset = Article.objects.all()
#     serializer_class = ArticleDetailSerializer
#
#
# class ArticleList(generics.ListCreateAPIView):
#     permission_classes = [IsAdminUserOrReadOnly]
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#


