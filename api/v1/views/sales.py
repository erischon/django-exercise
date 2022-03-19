from django.db.models import Prefetch

from rest_framework import generics
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
    # queryset = Sale.objects.raw("SELECT * FROM sales_sale GROUP BY quantity")
    # queryset = Sale.objects.values("article__name")
    # queryset = Sale.objects.order_by("article_id")
    # queryset = Sale.objects.select_related("article").order_by("article__name")
    queryset = Sale.objects.all().order_by("article__name")
    # queryset = Prefetch('pop_quizes', queryset=models.PopQuiz.objects.select_related('pop_quiz')('pop_quiz__pop_answers')
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    pagination_class = SalePagination

    # def get_queryset(self):
    #     """Only for the author of the sale."""
    #     return Sale.objects.filter().values("article")