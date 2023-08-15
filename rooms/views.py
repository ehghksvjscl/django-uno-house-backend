from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
)
from rest_framework.exceptions import NotFound

from .serializers import AmenitySerializer
from .models import Amenity


class AmenityApiView(APIView):
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
