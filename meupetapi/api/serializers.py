from rest_framework import serializers
from . import models

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'primeiroNome',
			'segundoNome',
			'idade',
			'email',
			'senha',
			'descricaoUsuario',
		)
		model = models.Usuario

class PetSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'nome',
			'raca',
			'dono',
			'tamanho',
			'descricaoPet',
		)
		model = models.Pet

class PasseadorSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'primeiroNome',
			'segundoNome',
			'idade',
			'regiao',
			'estaPasseando',
			'email',
		)
		model = models.Passeador

class PasseioSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'duracao',
			'descricaoPasseio',
		)
		model = models.Passeio

