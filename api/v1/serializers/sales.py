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
