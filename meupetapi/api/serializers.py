from rest_framework import serializers
from . import models

class PetSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'nome',
			'raca',
		)
		model = models.Review

