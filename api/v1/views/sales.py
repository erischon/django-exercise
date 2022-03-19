from django.db.models import Avg, Sum, Q

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

from sales.models import Article, ArticleCategory, Sale
from api.v1.serializers.sales import (
    SaleSerializer,
    SaleListSerializer,
    ArticleSerializer,
    BoardSerializer,
)
from sales.paginators import SalePagination


class ListCreateArticle(generics.ListCreateAPIView):
    """List and Create Articles."""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        SessionAuthentication,
    ]


class ListCreateSale(generics.ListCreateAPIView):
    """List and Create sales."""
    queryset = Sale.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        SessionAuthentication,
    ]
    pagination_class = SalePagination

    def perform_create(self, serializer):
        """Adding the author of Sale."""
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        """Get the Serializer we want."""
        if self.request.method == "GET":
            return SaleListSerializer
        else:
            return SaleSerializer


class PutDeleteSale(generics.RetrieveUpdateDestroyAPIView):
    """Put and Delete for a Sale."""
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        SessionAuthentication,
    ]

    def get_queryset(self):
        """Only for the author of the sale."""
        return Sale.objects.filter(author=self.request.user)


class BoardView(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    allowed_methods = ('GET',)
    
    def get_total_sales(self, request):
        article_total_sales = []
        for article in request:
            results = Sale.objects.filter(article=article.id)
            total_quantity = results.aggregate(Sum("quantity"))
            total_unit_selling_price = results.aggregate(Sum("unit_selling_price"))
            
            if total_quantity["quantity__sum"] and total_unit_selling_price["unit_selling_price__sum"]:
                total_sales = total_quantity["quantity__sum"] * total_unit_selling_price["unit_selling_price__sum"]
                print(total_sales)
            else:
                total_sales = None
            article_total_sales.append(total_sales)
        return article_total_sales

    # total_sales = Sum(quantity * unit_selling_price)
    # total_margin = Sum((quantity * unit_selling_price) - (quantity * manufacturing_cost))

