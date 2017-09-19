from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

class ListPet(APIView):
	def get(self, request, format=None):
		pets = models.Pet.objects.all()
		serializer = serializers.PetSerializer(pets, many=True)
		return Response(serializer.data) 