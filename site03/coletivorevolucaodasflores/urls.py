from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('obter/', views.obter_eventos_por_mes_ano, name='obter_eventos_por_mes_ano'),
    path('eventos/', views.eventos, name="eventos"),
    path('eventos/<int:id>', views.visualizar_evento, name="visualizar_evento"),
    path('projetos/', views.projetos, name="projetos"),
    path('dowload_cartilha/', views.dowload_cartilha, name='dowload_cartilha'),
    path('sobre/', views.sobre, name="sobre"),
    path('doacao/', views.doacao, name="doacao"),
]
