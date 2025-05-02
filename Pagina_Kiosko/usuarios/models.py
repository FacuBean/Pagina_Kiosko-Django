from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biografia = models.TextField(max_length=500, blank=True)
    enlace = models.URLField(max_length=200, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.usuario.username

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    respuesta = models.TextField(null=True, blank=True)
    fecha_respuesta = models.DateTimeField(null=True, blank=True)
    leido = models.BooleanField(default=False)

    def str(self):
        return f"{self.remitente} - {self.fecha_envio}"