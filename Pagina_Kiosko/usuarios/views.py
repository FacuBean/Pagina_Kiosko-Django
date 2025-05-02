from django.shortcuts import render, redirect
from .forms import FormularioRegistroPersonalizado, PerfilForm, MensajeForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import Mensaje

class VistaPerfil(LoginRequiredMixin, TemplateView):
    template_name = 'usuarios/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil'] = self.request.user.perfil
        return context

class VistaLoginPersonalizado(LoginView):
    template_name = 'usuarios/login.html'

def registro(request):
    if request.method == 'POST':
        form_user = FormularioRegistroPersonalizado(request.POST)
        form_perfil = PerfilForm(request.POST, request.FILES)

        if form_user.is_valid() and form_perfil.is_valid():
            user = form_user.save()

            if not hasattr(user, 'perfil'):
                perfil = form_perfil.save(commit=False)
                perfil.usuario = user
                perfil.save()
            else:
                perfil = user.perfil
                form_perfil = PerfilForm(
                    request.POST, request.FILES, instance=perfil)
                if form_perfil.is_valid():
                    form_perfil.save()
            messages.success(
                request, 'Cuenta creada exitosamente. Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form_user = FormularioRegistroPersonalizado()
        form_perfil = PerfilForm()

    return render(request, 'usuarios/signup.html', {'form_user': form_user, 'form_perfil': form_perfil})


@login_required
def editar_perfil(request):
    perfil = request.user.perfil

    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=perfil)

    return render(request, 'usuarios/editar_perfil.html', {'form': form})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            messages.success(request, "Mensaje enviado al dueño del kiosco.")
            return redirect('perfil')
    else:
        form = MensajeForm()
    return render(request, 'usuarios/enviar_mensaje.html', {'form': form})


@login_required
def ver_mis_mensajes(request):
    mensajes = Mensaje.objects.filter(
        remitente=request.user).order_by('-fecha_envio')

    mensajes.filter(respuesta__isnull=False, leido=False).update(leido=True)

    return render(request, 'usuarios/ver_mis_mensajes.html', {'mensajes': mensajes})


@login_required
def perfil(request):
    tiene_respuestas_no_leidas = Mensaje.objects.filter(
        remitente=request.user, respuestaisnull=False, leido=False).exists()
    return render(request, 'usuarios/perfil.html', {
        'usuario': request.user,
        'tiene_respuestas_no_leidas': tiene_respuestas_no_leidas,
    })