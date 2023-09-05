from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
)
from rest_framework.exceptions import NotFound
from django.db import transaction

from common.authentication import check_authentication, check_host
from common.qs import get_room_category, add_room_amenities
from .serializers import AmenitySerializer, RoomSerializer, RoomDetailSerializer
from .models import Amenity, Room


class RoomListView(APIView):
    def get_object(self):
        return Room.objects.all()

    def get(self, request):
        qs = self.get_object()
        serializer = RoomSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomDetailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        check_authentication(request)
        category = get_room_category(request)
        with transaction.atomic():
            room = serializer.save(host=request.user, category=category)
            room = add_room_amenities(request, room)

        return Response(RoomDetailSerializer(room).data, status=HTTP_201_CREATED)


class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        qs = self.get_object(pk=pk)
        return Response(RoomDetailSerializer(qs).data)

    def put(self, request, pk):
        check_authentication(request)
        qs = self.get_object(pk)
        check_host(request, qs)
        serializer = RoomDetailSerializer(qs, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        serializer = serializer.save()
        return Response(RoomDetailSerializer(serializer).data)

    def delete(self, request, pk):
        check_authentication(request)
        qs = self.get_object(pk)
        check_host(request, qs)
        qs.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class AmenityListApiView(APIView):
    def get_object(self):
        return Amenity.objects.all()

    def get(self, _):
        qs = self.get_object()
        serializer = AmenitySerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = AmenitySerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        serializer = serializer.save()
        return Response(AmenitySerializer(serializer).data, status=HTTP_201_CREATED)


class AmenityDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, _, pk):
        qs = self.get_object(pk=pk)
        return Response(AmenitySerializer(qs).data)

    def put(self, request, pk):
        qs = self.get_object(pk=pk)
        serializer = AmenitySerializer(qs, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        serializer = serializer.save()
        return Response(AmenitySerializer(serializer).data)

    def delete(self, _, pk):
        qs = self.get_object(pk=pk)
        qs.delete()
        return Response(status=HTTP_204_NO_CONTENT)
