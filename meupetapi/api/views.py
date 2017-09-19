from rest_framework import generics

from . import models
from . import serializers

class ListCreatePet(generics.ListCreateAPIView):
	queryset = models.Pet.objects.all()
	serializer_class = serializers.PetSerializer

class RetrieveUpdateDestroyPet(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Pet.objects.all()
	serializer_class = serializers.PetSerializer