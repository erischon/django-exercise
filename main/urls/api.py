from django.urls import path, include

from rest_framework import routers

from api.v1.views.sales import ListSale, CreateArticle


router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path(
        "v1/",
        include(
            [
                path("", include(router.urls)),
                path("article/", CreateArticle.as_view()),
                path("sales/", ListSale.as_view()),
            ]
        ),
    )
]
