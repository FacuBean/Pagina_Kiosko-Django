from django.contrib import admin

from .models import Perfil, Mensaje

admin.site.register(Perfil)

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    readonly_fields = ['remitente', 'contenido', 'fecha_envio']
    list_display = ['remitente', 'fecha_envio', 'respuesta', 'fecha_respuesta']
    fields = ['remitente', 'contenido',
              'fecha_envio', 'respuesta', 'fecha_respuesta']