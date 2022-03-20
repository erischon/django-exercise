from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from sales.models import Sale, Article, ArticleCategory

from api.v1.serializers.sales import SaleListSerializer


class PublicSalesApiTests(TestCase):
    """"""
    def setUp(self):
        self.client = APIClient()

    def test_login_required_sales_lc(self):
        """ Test that login required for sales list and create. """
        res = self.client.get(reverse("sales-list-create"))

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_login_required_sales_pd(self):
        """ Test that login required for sales put and delete. """
        res = self.client.get(reverse("sales-put-delete", args=(1,)))

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_login_required_articles_lc(self):
        """ Test that login required for articles list and create. """
        res = self.client.get(reverse("articles-list-create"))

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_login_required_board(self):
        """ Test that login required for board. """
        res = self.client.get(reverse("board"))

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class PrivateSalesApiTests(TestCase):
    """ """

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@acme.com',
            'password1234'
        )
        self.article_category_1 = ArticleCategory.objects.create(display_name="category 1")
        self.article_category_2 = ArticleCategory.objects.create(display_name="category 2")
        self.article_1 = Article.objects.create(
            code = "ABC123",
            category = self.article_category_1,
            name = "article 1",
            manufacturing_cost = 12.3,
        )
        self.sale_1 = Sale.objects.create(
            date = "2022-03-19",
            author = self.user,
            article = self.article_1,
            quantity = 5,
            unit_selling_price = 9.87,
        )

        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_sales(self):
        """ Test retrieving sales. """
        res = self.client.get(reverse("sales-list-create"))

        sales = Sale.objects.all()
        serializer = SaleListSerializer(sales, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["results"], serializer.data)
