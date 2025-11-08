from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('identites/', views.liste_identites, name='liste_identites'),
    path('detail/<int:id>/', views.detail_identite, name='detail_identite'),
]
