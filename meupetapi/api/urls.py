from django.conf.urls import url

from . import views

urlpatterns = [
	#URLs do Usuario
	url(r'^usuario/$', views.ListCreateUsuario.as_view(), name='usuario_list'),
	url(r'usuario/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyUsuario.as_view(), name='usuario_detail'),

	#URLs do Pet
	url(r'^pet/$', views.ListCreatePet.as_view(), name='pets_list'),
	url(r'pet/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyPet.as_view(), name='pets_detail'),

	#URLs do Passeador
	url(r'^passeador/$', views.ListCreatePasseador.as_view(), name='passeador_list'),
	url(r'passeador/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyPasseador.as_view(), name='passeador_detail'),

	#URLs do Passeio
	url(r'^passeio/$', views.ListCreatePasseio.as_view(), name='passeio_list'),
	url(r'passeio/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyPasseio.as_view(), name='passeio_detail'),
]
