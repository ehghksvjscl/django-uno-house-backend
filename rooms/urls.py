from django.urls import path
from .views import AmenityApiView, AmenityDetailApiView


urlpatterns = [
    path("amenities/", AmenityApiView.as_view()),
    path("amenities/<int:pk>", AmenityDetailApiView.as_view()),
]
