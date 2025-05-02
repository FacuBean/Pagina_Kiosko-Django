from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import registro, VistaLoginPersonalizado, VistaPerfil, editar_perfil, enviar_mensaje, ver_mis_mensajes

urlpatterns = [
    path('signup/', registro, name='signup'),
    path('login/', VistaLoginPersonalizado.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('perfil/', VistaPerfil.as_view(), name='perfil'),
    path('editar/', editar_perfil, name='editar_perfil'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='usuarios/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='usuarios/password_change_done.html'), name='password_change_done'),
    path('enviar-mensaje/', enviar_mensaje, name='enviar_mensaje'),
    path('mis-mensajes/', ver_mis_mensajes, name='ver_mis_mensajes'),
]
