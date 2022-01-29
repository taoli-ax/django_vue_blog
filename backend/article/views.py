from rest_framework import status, generics, viewsets
from .models import Article,Category
from .serializers import ArticleSerializer, CategorySerializer, CategoryDetailSerializer, CategorySerializer
from .permissions import IsAdminUserOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

    class CategoryViewSet(viewsets.ModelViewSet):
        """分类视图集"""
        ...

        def get_serializer_class(self):
            if self.action == 'list':
                return CategorySerializer
            else:
                return CategoryDetailSerializer

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


