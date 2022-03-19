from rest_framework import serializers

from sales.models import Sale, Article, ArticleCategory


class SaleListSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Sale
        fields = "__all__"
        read_only_fields = ("author",)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
