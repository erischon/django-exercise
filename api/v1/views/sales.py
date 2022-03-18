from rest_framework import generics
from sales.models import Article, ArticleCategory, Sale
from api.v1.serializers.sales import SaleSerializer, ArticleSerializer


class CreateArticle(generics.CreateAPIView):
    serializer_class = ArticleSerializer


class ListSale(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class CreateSale(generics.CreateAPIView):
    serializer_class = SaleSerializer


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
