from rest_framework import generics

from spoiled.api.serializers import SpoiledSerializer
from spoiled.models import Spoiled

class SpoiledList(generics.ListCreateAPIView):
    queryset = Spoiled.objects.all()
    serializer_class = SpoiledSerializer

