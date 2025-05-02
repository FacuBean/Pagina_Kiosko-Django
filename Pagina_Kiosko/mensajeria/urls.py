from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_general, name='chat'),
    path('chat/<int:cliente_id>/', views.chat_cliente, name='chat_cliente'),
]