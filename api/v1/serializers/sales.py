from django.db.models import Avg, Sum, Q

from rest_framework import serializers

from sales.models import Sale, Article, ArticleCategory


class SaleListSerializer(serializers.ModelSerializer):
    """Serializer for List of Sales."""
    category = serializers.CharField(source="article.category")
    article = serializers.CharField(source="article.name")
    code = serializers.CharField(source="article.code")
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = [
            "date",
            "category",
            "code",
            "article",
            "quantity",
            "unit_selling_price",
            "total_price",
        ]

    def get_total_price(self, obj):
        return obj.quantity * obj.unit_selling_price


class SaleSerializer(serializers.ModelSerializer):
    """Basic Serializer for Sales."""
    class Meta:
        model = Sale
        fields = "__all__"
        read_only_fields = ("author",)


class ArticleSerializer(serializers.ModelSerializer):
    """Basic Serializer for Articles."""
    class Meta:
        model = Article
        fields = "__all__"


class BoardSerializer(serializers.ModelSerializer):
    """Sale Board"""
    category = serializers.CharField(source="article.category")
    article = serializers.CharField(source="article.name")
    # article = serializers.SerializerMethodField()
    total_sale = serializers.SerializerMethodField()
    margin = serializers.SerializerMethodField()
    last_sale = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = [
            "article",
            "category",
            "total_sale",
            "margin",
            "last_sale",
        ]

    # def get_article(self, obj):
    #     qs = Sale.objects.filter(article=obj.article)
    #     article = serializers.CharField(source="article.name")
    #     return qs

    def get_total_sale(self, obj):
        """"""
        qs = Sale.objects.filter(article=obj.article)
        total_quantity = qs.aggregate(Sum("quantity"))
        total_unit_selling_price = qs.aggregate(Sum("unit_selling_price"))
        return total_quantity["quantity__sum"] * total_unit_selling_price["unit_selling_price__sum"]

    def get_margin(self, obj):
        """"""
        qs = Article.objects.filter(id=obj.article.id)
        qs2 = Sale.objects.filter(article=obj.article)

        total_sale = self.get_total_sale(obj)
        total_cost = qs2.aggregate(Sum("quantity"))["quantity__sum"] + qs.aggregate(Sum("manufacturing_cost"))["manufacturing_cost__sum"]
        margin = total_sale - total_cost
        return (margin / total_cost) * 100

    def get_last_sale(self, obj):
        """"""
        date = Sale.objects.filter(article=obj.article).latest("date")
        return date.date
