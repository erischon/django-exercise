from django.urls import path, include

from rest_framework import routers

from api.v1.views.sales import ListSale, CreateArticle, CreateSale, PutSale, DeleteSale


router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path(
        "v1/",
        include(
            [
                path("", include(router.urls)),
                path("article/", CreateArticle.as_view()),
                path("sales/", ListSale.as_view()),
                path("sales/sale", CreateSale.as_view()),
                path("sales/<int:pk>/put", PutSale.as_view()),
                path("sales/<int:pk>/delete", DeleteSale.as_view()),
            ]
        ),
    )
]
