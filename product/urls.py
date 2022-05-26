from django.urls import path
from .views import ProductViewSet, RelatedProductView
urlpatterns = [
    path("list/", ProductViewSet.as_view()),
    path("list/<slug>/", ProductViewSet.as_view()),
    path("related/<id>/", RelatedProductView.as_view()),
]