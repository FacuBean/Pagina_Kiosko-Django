from .models import Mensaje


def mensajes_con_respuesta(request):
    if request.user.is_authenticated:
        mensajes_con_rta = Mensaje.objects.filter(
            remitente=request.user,
            respuesta__isnull=False,
            leido=False
        ).count()
        return {'mensajes_con_respuesta': mensajes_con_rta}
    return {}
