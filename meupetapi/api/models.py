from django.db import models

class Usuario(models.Model):
	id = models.AutoField(primary_key=True)
	primeiroNome = models.CharField(max_length=255)
	segundoNome = models.CharField(max_length=255)
	idade = models.DateField(auto_now=False)
	email = models.EmailField(max_length=255)
	descricaoUsuario = models.TextField()

	def __str__(self):
		return self.primeiroNome

	@property
	def full_name(self):
		return '%s %s' % (self.primeiroNome, self.segundoNome)

class Pet(models.Model):
	TAM_CACHORRO = (
		('P', 'Pequeno'),
		('M', 'Medio'),
		('G', 'Grande'),
	)
	id = models.AutoField(primary_key=True)
	dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	nome = models.CharField(max_length=255)
	raca = models.CharField(max_length=255)
	tamanho = models.CharField(max_length=1, choices=TAM_CACHORRO)
	descricaoPet = models.TextField(blank=True)

	def __str__(self):
		return self.nome

class Passeador(models.Model):
	id = models.AutoField(primary_key=True)
	primeiroNome = models.CharField(max_length=255)
	segundoNome = models.CharField(max_length=255)
	idade = models.DateField(auto_now=False)
	regiao = models.CharField(max_length=100)
	estaPasseando = models.BooleanField()
	email = models.EmailField(max_length=255)

class Passeio(models.Model):
	id = models.AutoField(primary_key=True)
	duracao = models.DurationField()
	descricaoPasseio = models.TextField()
	# fotoDoPasseio = models.ImageField()
