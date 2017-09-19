from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.ListPet.as_view(), name='pets_list')
]