from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Mensaje
from .forms import MensajeForm

@login_required
def chat_general(request):
    user = request.user
    superusers = User.objects.filter(is_superuser=True)

    mensajes = Mensaje.objects.filter(
        Q(emisor=user, receptor__in=superusers) |
        Q(emisor__in=superusers, receptor=user)
    ).order_by('fecha_envio')

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = user
            mensaje.receptor = superusers.first()  # Primer superusuario
            mensaje.save()
            return redirect('chat_general')
    else:
        form = MensajeForm()

    return render(request, 'chat.html', {
        'mensajes': mensajes,
        'form': form,
        'cliente': user,
    })

@login_required
def chat_cliente(request, cliente_id):
    if not request.user.is_superuser:
        return redirect('chat_general')

    cliente = get_object_or_404(User, id=cliente_id)
    mensajes = Mensaje.objects.filter(
        Q(emisor=request.user, receptor=cliente) |
        Q(emisor=cliente, receptor=request.user)
    ).order_by('fecha_envio')

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.receptor = cliente
            mensaje.save()
            return redirect('chat_cliente', cliente_id=cliente.id)
    else:
        form = MensajeForm()

    return render(request, 'chat.html', {
        'mensajes': mensajes,
        'form': form,
        'cliente': cliente,
    })
