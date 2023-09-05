from django.urls import path
from .views import AmenityListApiView, AmenityDetailApiView, RoomListView, RoomDetail


urlpatterns = [
    path("", RoomListView.as_view()),
    path("<int:pk>", RoomDetail.as_view()),
    path("amenities/", AmenityListApiView.as_view()),
    path("amenities/<int:pk>", AmenityDetailApiView.as_view()),
]
