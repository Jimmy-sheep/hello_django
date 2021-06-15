from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_api, name='add_api'),
    path('apilist', views.list_api, name='list_api'),
	
]