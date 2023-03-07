from django.urls import path

from . import views

app_name = "receitas"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>/', views.editar_receita, name='editar_receita'),
    path('gravar_receita', views.gravar_receita, name='gravar_receita'),
    path('<int:receita_id>/atualizar', views.atualizar_receita, name='atualizar_receita'),
    path('criar_receita', views.criar_receita, name='criar_receita'),
    path('<int:receita_id>/deletar', views.deletar_receita, name='deletar_receita'),
]