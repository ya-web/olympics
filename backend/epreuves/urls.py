from django.urls import path
from . import views

urlpatterns = [
    path('epreuves/', views.epreuves_list, name='epreuves_list'),
]
