
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^details/(?P<id>\w{0,50})/$', views.details),	
	url(r'^compose', views.compose, name='compose'),
	url(r'^sent', views.sent, name='sent'),
	url(r'^trash', views.trash, name="trash"),
	url(r'^trashdetails/(?P<id>\w{0,50})/$', views.trashdetails),
	url(r'^deletemail/(?P<id>\w{0,50})/$', views.deletemail),
	url(r'^deleted_insert', views.deleted_insert, name='deleted_insert')
]

