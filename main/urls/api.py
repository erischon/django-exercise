from django.urls import path, include

from rest_framework import routers

from api.v1.views.sales import ListCreateArticle, ListCreateSale, PutSale, DeleteSale


router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path(
        "v1/",
        include(
            [
                path("", include(router.urls)),
                path("article/", ListCreateArticle.as_view()),
                path("sales/", ListCreateSale.as_view()),
                path("sales/<int:pk>/put", PutSale.as_view()),
                path("sales/<int:pk>/delete", DeleteSale.as_view()),
            ]
        ),
    )
]
