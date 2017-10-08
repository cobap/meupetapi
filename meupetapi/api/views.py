from rest_framework import generics

from . import models
from . import serializers

#Metodo do Usuario
class ListCreateUsuario(generics.ListCreateAPIView):
	queryset = models.Usuario.objects.all()
	serializer_class = serializers.UsuarioSerializer

class RetrieveUpdateDestroyUsuario(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Usuario.objects.all()
	serializer_class = serializers.UsuarioSerializer

#Metodos do Pet
class ListCreatePet(generics.ListCreateAPIView):
	queryset = models.Pet.objects.all()
	serializer_class = serializers.PetSerializer

class RetrieveUpdateDestroyPet(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Pet.objects.all()
	serializer_class = serializers.PetSerializer

#Metodos do Passeador
class ListCreatePasseador(generics.ListCreateAPIView):
	queryset = models.Passeador.objects.all()
	serializer_class = serializers.PasseadorSerializer

class RetrieveUpdateDestroyPasseador(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Passeador.objects.all()
	serializer_class = serializers.PasseadorSerializer

#Metodos do Passeio
class ListCreatePasseio(generics.ListCreateAPIView):
	queryset = models.Passeio.objects.all()
	serializer_class = serializers.PasseioSerializer

class RetrieveUpdateDestroyPasseio(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Passeio.objects.all()
	serializer_class = serializers.PasseioSerializer