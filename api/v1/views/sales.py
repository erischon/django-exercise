from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from sales.models import Article, ArticleCategory, Sale
from api.v1.serializers.sales import SaleSerializer, SaleListSerializer, ArticleSerializer
from sales.paginators import SalePagination


class ListCreateArticle(generics.ListCreateAPIView):
    """"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication,]


class ListCreateSale(generics.ListCreateAPIView):
    """"""
    queryset = Sale.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication,]
    pagination_class = SalePagination

    def perform_create(self, serializer):
        """"""
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return SaleListSerializer
        else:
            return SaleSerializer


class PutDeleteSale(generics.RetrieveUpdateDestroyAPIView):
    """"""
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication,]

    def get_queryset(self):
        return Sale.objects.filter(author = self.request.user)
