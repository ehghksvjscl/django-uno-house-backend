from django.urls import path
from .views import AmenityListApiView, AmenityDetailApiView


urlpatterns = [
    path("amenities/", AmenityListApiView.as_view()),
    path("amenities/<int:pk>", AmenityDetailApiView.as_view()),
]
