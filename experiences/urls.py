from django.urls import path
from .views import PerkListApiView, PerkDetailApiView


urlpatterns = [
    path("perks/", PerkListApiView.as_view()),
    path("perks/<int:pk>", PerkDetailApiView.as_view()),
]
