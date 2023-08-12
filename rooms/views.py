from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

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
        return Response(AmenitySerializer(serializer).data)


class AmenityDetailApiView(APIView):
    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
