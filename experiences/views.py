from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED,
)
from rest_framework.exceptions import NotFound

from .serializers import PerkSerializer
from .models import Perk


class PerkApiView(APIView):
    def get_object(self):
        return Perk.objects.all()

    def get(self, _):
        qs = self.get_object()
        serializer = PerkSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PerkSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        serializer = serializer.save()
        return Response(PerkSerializer(serializer).data, status=HTTP_201_CREATED)


class PerkDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            raise NotFound

    def get(self, _, pk):
        qs = self.get_object(pk=pk)
        return Response(PerkSerializer(qs).data)

    def put(self, request, pk):
        qs = self.get_object(pk=pk)
        serializer = PerkSerializer(qs, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        serializer = serializer.save()
        return Response(PerkSerializer(serializer).data)

    def delete(self, _, pk):
        qs = self.get_object(pk=pk)
        qs.delete()
        return Response(status=HTTP_204_NO_CONTENT)
