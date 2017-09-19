from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.ListCreatePet.as_view(), name='pets_list'),
	url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDestroyPet.as_view(), name='pets_detail')
]