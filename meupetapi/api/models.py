from django.db import models

class Pet(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=255)
	raca = models.CharField(max_length=255)

	def __str__(self):
		return self.nome