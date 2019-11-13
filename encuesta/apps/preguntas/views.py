from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.preguntas.forms import PreguntasForm
from apps.preguntas.models import Encuesta
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, 'preguntas/index.html')


def encuesta_view(request):
    if request.method == 'POST':
        form = PreguntasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preguntas:listar')
        else:
            return redirect('preguntas:error')
    else:
        form = PreguntasForm()

    return render(request, 'preguntas/preguntas_form.html',{'form':form})


def testview(request):
    return render(request, 'preguntas/prueba_error.html')


def listar_encuesta(request):
    encuestas = Encuesta.objects.all().order_by('id')
    contexto = {'encuestas':encuestas}
    return render(request,'preguntas/encuesta_list.html',contexto)

def editar_encuesta(request, id_encuesta):
    encuesta = Encuesta.objects.get(id=id_encuesta)
    if request.method == 'GET':
        form = PreguntasForm(instance=encuesta)
    else:
        form = PreguntasForm(request.POST, instance=encuesta)
        if form.is_valid():
            form.save()
        return redirect('preguntas:listar_encuestas')
    return render(request, 'preguntas/preguntas_form.html',{'form':form})


def eliminar_encuesta(request, id_encuesta):
    encuesta = Encuesta.objects.get(id=id_encuesta)
    if request.method == 'POST':
        encuesta.delete()
        return redirect('preguntas:listar_encuestas')
    return render(request, 'preguntas/encuesta_delete.html',{'encuesta':encuesta})


class EncuestaList(ListView):
    model = Encuesta
    template_name = 'preguntas/encuesta_list.html'    


class EncuestaCreate(CreateView):
    model = Encuesta
    form_class = PreguntasForm
    template_name = 'preguntas/preguntas_form.html'
    success_url = reverse_lazy('preguntas:listar_encuestas')


class EncuestaUpdate(UpdateView):
    model = Encuesta
    form_class = PreguntasForm
    template_name = 'preguntas/preguntas_form.html'
    success_url = reverse_lazy('preguntas:listar_encuestas')


class EncuestaDelete(DeleteView):
    model = Encuesta
    template_name = 'preguntas/encuesta_delete.html'
    success_url = reverse_lazy('preguntas:listar_encuestas')