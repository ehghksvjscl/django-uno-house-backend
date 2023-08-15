from django.urls import path
from .views import PerkApiView, PerkDetailApiView


urlpatterns = [
    path("perks/", PerkApiView.as_view()),
    path("perks/<int:pk>", PerkDetailApiView.as_view()),
]
