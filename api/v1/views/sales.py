from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from sales.models import Article, ArticleCategory, Sale
from api.v1.serializers.sales import SaleSerializer, ArticleSerializer


class ListCreateArticle(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class ListCreateSale(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]


class PutSale(generics.UpdateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class DeleteSale(generics.DestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     queryset = Sale.objects.filter(author = self.request.user, id = self.kwargs['pk'])
    #     return queryset
