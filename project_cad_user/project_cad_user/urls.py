
from django.urls import path
from app_cad import views

urlpatterns = [
    # rota, view, name de referencia
    # principal.com
    path('', views.page, name='page'),
    # principal.com/user
    # ligando o nome que está no html list-user a função view
    path('usuarios/', views.user, name='list_user')
]
