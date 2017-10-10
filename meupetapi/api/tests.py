<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-
>>>>>>> 80da97cee4c92278656157b4e3befc30963cecce
from django.test import TestCase

from datetime import timedelta
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Passeio
from api.models import Passeador
from api.models import Pet
from api.models import Usuario
from api import views

import json
#from rest_framework.test import APIRequestFactory

# Create your tests here.

class PasseioMethodTest(TestCase):

    def setUp(self):
        duracao = timedelta(15)
        url = reverse('api:passeio_list')
        data = {'duracao': duracao, 'descricaoPasseio': 'descrição Passeio teste'}
        response = self.client.post(url, data, format='json')

    def test_newPasseio(self):
        """
        Ensure we can create a new pet walk
        """
        duracao = timedelta(20)
        url = reverse('api:passeio_list')
        data = {'duracao': duracao, 'descricaoPasseio': 'descrição Passeio teste 2'}
        response = self.client.post(url, data, format='json')
        #descricao = "descricao Passeio teste"
        #testPasseio = Passeio(duracao);
        #create_passeio(duracao=timedelta(), descricaoPasseio = "descrição Passeio teste")
        #response = self.client.get(reverse('passeio:index'))

        # Using the standard RequestFactory API to create a form POST request
        #factory = APIRequestFactory()
        #request = factory.post('/passeio/', {'duracao': 15, 'descricaoPasseio': 'descrição Passeio teste'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Passeio.objects.count(), 2)

    # def test_getPasseio(self):
    #     """
    #     Ensure we can see the details of a pet walk
    #     """

    #     response2 = self.client.get('/api/v1/passeio/1/')
    #     self.assertEqual(response2.data, {'id': 1, 'duracao': '15 00:00:00', 'descricaoPasseio': 'descrição Passeio teste'})

    # def test_editPasseio(self):
    #     """
    #     Ensure we can edit the details of a pet walk
    #     """

    #     url = reverse('api:passeio_detail',args=[1])
    #     data = {'duracao': '15 22:45:00', 'descricaoPasseio': 'descrição Passeio teste editada'}
    #     response = self.client.patch(url, json.dumps(data), content_type='application/json')

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     response2 = self.client.get('/api/v1/passeio/1/')
    #     self.assertEqual(response2.data, {'id': 1, 'duracao': '15 22:45:00', 'descricaoPasseio': 'descrição Passeio teste editada'})

class PasseadorMethodTest(TestCase):

	#id = models.AutoField(primary_key=True)
	#primeiroNome = models.CharField(max_length=255)
	#segundoNome = models.CharField(max_length=255)
	#idade = models.DateField(auto_now=False)
	#regiao = models.CharField(max_length=100)
	#estaPasseando = models.BooleanField()
	#email = models.EmailField(max_length=255)

    def setUp(self):

        url = reverse('api:passeador_list')
        data = {'primeiroNome': 'Passeador', 'segundoNome': 'Sobrenome', 'idade':'1992-09-13','regiao':'São Paulo','estaPasseando':False,'email':'passeador@mail.com'}
        response = self.client.post(url, data, format='json')

    def test_newPasseador(self):
        """
        Ensure we can create a new pet walker
        """
        url = reverse('api:passeador_list')
        data = {'primeiroNome': 'Passeador 2', 'segundoNome': 'Sobrenome 2', 'idade':'1992-09-13','regiao':'São Paulo','estaPasseando':False,'email':'passeador@mail.com'}
        response = self.client.post(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Passeador.objects.count(), 2)

    # def test_getPasseador(self):
    #     """
    #     Ensure we can see the details of a pet walker
    #     """

    #     response2 = self.client.get('/api/v1/passeador/1/')
    #     self.assertEqual(response2.data, {'id': 1,'primeiroNome': 'Passeador', 'segundoNome': 'Sobrenome', 'idade':'1992-09-13','regiao':'São Paulo','estaPasseando':False,'email':'passeador@mail.com'})


    # def test_editPasseador(self):
    #     """
    #     Ensure we can edit the details of a pet walker
    #     """

    #     url = reverse('api:passeador_detail',args=[1])
    #     data = {'primeiroNome': 'Passeador Editado', 'segundoNome': 'Sobrenome', 'idade':'1992-09-13','regiao':'São Paulo','estaPasseando':False,'email':'passeador_editado@mail.com'}
    #     response = self.client.patch(url, json.dumps(data), content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     response2 = self.client.get('/api/v1/passeador/1/')
    #     self.assertEqual(response2.data, {'id': 1,'primeiroNome': 'Passeador Editado', 'segundoNome': 'Sobrenome', 'idade':'1992-09-13','regiao':'São Paulo','estaPasseando':False,'email':'passeador_editado@mail.com'})


class PetMethodTest(TestCase):

	#TAM_CACHORRO = (
	#	('P', 'Pequeno'),
	#	('M', 'Medio'),
	#	('G', 'Grande'),
	#)
	#id = models.AutoField(primary_key=True)
	#dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	#nome = models.CharField(max_length=255)
	#raca = models.CharField(max_length=255)
	#tamanho = models.CharField(max_length=1, choices=TAM_CACHORRO)
	#descricaoPet = models.TextField(blank=True)
    userId = 0;

    def setUp(self):

        url = reverse('api:usuario_list')
        data = {'primeiroNome': 'Nome', 'segundoNome': 'Sobrenome', 'idade': '1992-01-02','email':'mail@mail.com','senha':'123','descricaoUsuario':'exemplo descricao'}
        userResponse = self.client.post(url, data, format='json')
        self.userId = userResponse.data['id']

        url = reverse('api:pets_list')
        data = {'dono': self.userId, 'nome': 'Nome do Pet', 'raca': 'Raça 1','tamanho':'M','descricaoPet':'Pet exemplo'}
        response = self.client.post(url, data, format='json')

    def test_newPet(self):
        """
        Ensure we can create a new pet
        """
        url = reverse('api:pets_list')
        data = {'dono': self.userId, 'nome': 'Nome do Pet 2', 'raca': 'Raça 1','tamanho':'M','descricaoPet':'Pet exemplo'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pet.objects.count(), 2)

    # def test_getPet(self):
    #     """
    #     Ensure we can see the details of a pet
    #     """

    #     response2 = self.client.get('/api/v1/pet/1/')
    #     self.assertEqual(response2.data, {'id': 1,'dono': self.userId, 'nome': 'Nome do Pet', 'raca': 'Raça 1','tamanho':'M','descricaoPet':'Pet exemplo'})


    # def test_editPet(self):
    #     """
    #     Ensure we can edit the details of a pet
    #     """

    #     url = reverse('api:pets_detail',args=[1])
    #     data = {'dono': self.userId, 'nome': 'Nome pet editado', 'raca': 'Raça 1','tamanho':'M','descricaoPet':'Pet exemplo'}
    #     response = self.client.patch(url, json.dumps(data), content_type='application/json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     response2 = self.client.get('/api/v1/pet/1/')
    #     self.assertEqual(response2.data, {'id': 1,'dono': self.userId, 'nome': 'Nome pet editado', 'raca': 'Raça 1','tamanho':'M','descricaoPet':'Pet exemplo'})


class UsuarioMethodTest(TestCase):

	#id = models.AutoField(primary_key=True)
	#primeiroNome = models.CharField(max_length=255)
	#segundoNome = models.CharField(max_length=255)
	#idade = models.DateField(auto_now=False)
	#email = models.EmailField(max_length=255)
	#senha = models.CharField(max_length=30)
	#descricaoUsuario = models.TextField()
    #userId = 0;

    def setUp(self):

        url = reverse('api:usuario_list')
        data = {'primeiroNome': 'Nome', 'segundoNome': 'Sobrenome', 'idade': '1992-01-02','email':'mail@mail.com','senha':'123','descricaoUsuario':'exemplo descricao'}
        response = self.client.post(url, data, format='json')

    def test_newUsuario(self):
        """
        Ensure we can create a new user
        """
        url = reverse('api:usuario_list')
        data = {'primeiroNome': 'Nome', 'segundoNome': 'Sobrenome', 'idade': '1992-01-02','email':'mail@mail.com','senha':'123','descricaoUsuario':'exemplo descricao'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.count(), 2)

    def test_getUsuario(self):
        """
        Ensure we can see the details of an user
        """

        response2 = self.client.get('/api/v1/usuario/1/')
        self.assertEqual(response2.data, {'id': 1,'primeiroNome': 'Nome', 'segundoNome': 'Sobrenome', 'idade': '1992-01-02','email':'mail@mail.com','senha':'123','descricaoUsuario':'exemplo descricao'})


    def test_editUsuario(self):
        """
        Ensure we can edit the details of a user
        """

        url = reverse('api:usuario_detail',args=[1])
        data = {'primeiroNome': 'Nome Editado', 'segundoNome': 'Sobrenome', 'idade': '1992-01-02','email':'mail@mail.com','senha':'123','descricaoUsuario':'exemplo descricao'}
        response = self.client.patch(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response2 = self.client.get('/api/v1/usuario/1/')
        self.assertEqual(response2.data, {'id': 1, 'primeiroNome': 'Nome Editado', 'segundoNome': 'Sobrenome', 'idade': '1992-01-02','email':'mail@mail.com','senha':'123','descricaoUsuario':'exemplo descricao'})
