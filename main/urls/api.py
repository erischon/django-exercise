from django.urls import path, include

from rest_framework import routers

from api.v1.views.sales import ListCreateArticle, ListCreateSale, PutDeleteSale, BoardView


router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path(
        "v1/",
        include(
            [
                path("", include(router.urls)),
                path("articles/", ListCreateArticle.as_view()),
                path("sales/", ListCreateSale.as_view()),
                path("sales/<int:pk>/", PutDeleteSale.as_view()),
                path("board/", BoardView.as_view()),
            ]
        ),
    )
]
