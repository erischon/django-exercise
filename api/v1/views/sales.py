from rest_framework import generics
from sales.models import Article, ArticleCategory, Sale
from api.v1.serializers.sales import SaleSerializer, ArticleSerializer


class ListSale(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class CreateArticle(generics.CreateAPIView):
    serializer_class = ArticleSerializer
