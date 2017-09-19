from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers

class ListPet(APIView):
	def get(self, request, format=None):
		pets = models.Pet.objects.all()
		serializers = serializers.PetSerializer(pet, many=True)
		return Response(serializers.data) 