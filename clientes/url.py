
from django.contrib import admin
from django.urls import path
from clientes.views import clientes_page,novo_cliente
from clientes.views import person_update, person_delete
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('list', clientes_page, name='list-cli'),
    path('novo', novo_cliente, name='nov-cli'),
    path('update/<int:id>/', person_update, name='atualizar'),
    path('delete/<int:id>/', person_delete, name='del'),
]
