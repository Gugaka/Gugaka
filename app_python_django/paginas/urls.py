from django.urls import path
from .views import PaginaInicial

urlpatterns = [
    #path('endereço/', minhaDaView.as_view(), name='nomeDaURL'),
    path('', PaginaInicial.as_view(), name='inicio'),
]
