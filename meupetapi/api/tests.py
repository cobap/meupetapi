from django.test import TestCase

from datetime import timedelta
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Passeio
from api.models import Passeador
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
        #descricao = "descrição Passeio teste"
        #testPasseio = Passeio(duracao);
        #create_passeio(duracao=timedelta(), descricaoPasseio = "descrição Passeio teste")
        #response = self.client.get(reverse('passeio:index'))

        # Using the standard RequestFactory API to create a form POST request
        #factory = APIRequestFactory()
        #request = factory.post('/passeio/', {'duracao': 15, 'descricaoPasseio': 'descrição Passeio teste'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Passeio.objects.count(), 2)

    def test_getPasseio(self):
        """
        Ensure we can see the details of a pet walk
        """

        response2 = self.client.get('/api/v1/passeio/1/')
        self.assertEqual(response2.data, {'id': 1, 'duracao': '15 00:00:00', 'descricaoPasseio': 'descrição Passeio teste'})

    def test_editPasseio(self):
        """
        Ensure we can edit the details of a pet walk
        """

        url = reverse('api:passeio_detail',args=[1])
        data = {'duracao': '15 22:45:00', 'descricaoPasseio': 'descrição Passeio teste editada'}
        response = self.client.patch(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response2 = self.client.get('/api/v1/passeio/1/')
        self.assertEqual(response2.data, {'id': 1, 'duracao': '15 22:45:00', 'descricaoPasseio': 'descrição Passeio teste editada'})

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

    def test_getPasseador(self):
        """
        Ensure we can see the details of a pet walker
        """

        response2 = self.client.get('/api/v1/passeador/1/')
        self.assertEqual(response2.data, {'id': 1,'primeiroNome': 'Passeador', 'segundoNome': 'Sobrenome', 'idade':'1992-09-13','regiao':'São Paulo','estaPasseando':False,'email':'passeador@mail.com'})


    def test_editPasseador(self):
        """
        Ensure we can edit the details of a pet walker
        """

        url = reverse('api:passeador_detail',args=[1])
        data = {'primeiroNome': 'Passeador Editado', 'segundoNome': 'Sobrenome', 'idade':'1992-09-13','regiao':'São Paulo','estaPasseando':False,'email':'passeador_editado@mail.com'}
        response = self.client.patch(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response2 = self.client.get('/api/v1/passeador/1/')
        self.assertEqual(response2.data, {'id': 1,'primeiroNome': 'Passeador Editado', 'segundoNome': 'Sobrenome', 'idade':'1992-09-13','regiao':'São Paulo','estaPasseando':False,'email':'passeador_editado@mail.com'})
