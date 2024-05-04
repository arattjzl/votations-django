from django.shortcuts import render, redirect
from .models import Candidato, Partido, Votacion
from .forms import FormCandidato, FormPartido, FormVotacion, FormFiltrosCandidato, FormFiltrosPartido
from django.core.paginator import Paginator
import datetime

# Create your views here.
def bienvenida(request):
    return render(request, 'bienvenida.html')

def nuevo_partido(request):
    if request.method == 'POST':
        form = FormPartido(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_partidos')
    else:
        form = FormPartido()

    context = {'form': form}
    return render(request, 'nuevo_partido.html', context)

def lista_partidos(request):
    partidos = Partido.objects.all()

    if request.method == 'POST':
        form = FormFiltrosPartido(request.POST)

        nombre = request.POST.get('nombre', None)
        descripcion = request.POST.get('descripcion', None)
        
        if nombre:
            partidos = partidos.filter(nombre__contains=nombre)

        if descripcion:
            partidos = partidos.filter(descripcion__contains=descripcion)

    else:
        form = FormFiltrosPartido()
    
    cuantos = 3

    paginator = Paginator(partidos, cuantos)

    page_number = request.GET.get('page')
    partidos = paginator.get_page(page_number)

    context = {
        'partidos': partidos,
        'form': form,
        }
    return render(request, 'lista_partidos.html', context)

def editar_partido(request, id):
    partido = Partido.objects.get(id = id)
    if request.method == 'POST':
        form = FormPartido(request.POST, instance=partido)
        if form.is_valid():
            form.save()
            return redirect('lista_partidos')
    else:
        form = FormPartido(instance=partido)
    context = {'form': form}

    return render(request, 'editar_partido.html', context)


def eliminar_partido(request, id):
    partido = Partido.objects.get(id=id)
    candidatos = Candidato.objects.filter(partido=partido)
    for candidato in candidatos:
        candidato.delete()
    
    partido.delete()
    return redirect('lista_partidos')
    

def nuevo_candidato(request):
    if request.method == 'POST':
        form = FormCandidato(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['imagen']
            form.imagen = image
            form.save()
            return redirect('lista_candidatos')
    else:
        form = FormCandidato()
    
    context = {'form': form}
    return render(request, 'nuevo_candidato.html', context)

def lista_candidatos(request):
    candidatos = Candidato.objects.all()

    if request.method == 'POST':
        form = FormFiltrosCandidato(request.POST)

        nombre = request.POST.get('nombre', None)
        apellido_pat = request.POST.get('apellido_pat', None)
        apellido_mat = request.POST.get('apellido_mat', None)
        partido = request.POST.get('partido', None)
        
        if nombre:
            candidatos = candidatos.filter(nombre__contains=nombre)

        if apellido_pat:
            candidatos = candidatos.filter(apellido_pat__contains=apellido_pat)
        
        if apellido_mat:
            candidatos = candidatos.filter(apellido_mat__contains=apellido_mat)

        if partido:
            candidatos = candidatos.filter(partido__contains=partido)

    else:
        form = FormFiltrosCandidato()
    
    cuantos = 3

    paginator = Paginator(candidatos, cuantos)

    page_number = request.GET.get('page')
    candidatos = paginator.get_page(page_number)

    context = {
        'candidatos': candidatos,
        'form': form,
        }
    return render(request, 'lista_candidatos.html', context)

def editar_candidato(request, id):
    candidato = Candidato.objects.get(id = id)
    if request.method == 'POST':
        form = FormCandidato(request.POST, request.FILES or None, instance=candidato)
        if form.is_valid():
            form.save()
            return redirect('lista_candidatos')
    else:
        form = FormCandidato(instance=candidato)
    context = {'form': form}

    return render(request, 'editar_candidato.html', context)

def eliminar_candidato(request, id):
    candidato = Candidato.objects.get(id=id)
    candidato.delete()
    return redirect('lista_candidatos')

def votacion(request):
    candidatos = Candidato.objects.all()
    context = {
        'candidatos': candidatos
        }
    return render(request, 'votacion.html', context)

def voto(request, id):
    candidato = Candidato.objects.get(id=id)
    votacion = Votacion()
    votacion.candidato = candidato
    votacion.fecha_hora = datetime.datetime.now()
    votacion.save()
    return redirect('conteo_votos')

def conteo_votos(request):
    votos = Votacion.objects.all()
    candidato_votos = []
    candidatos = Candidato.objects.all()
    for candidato in candidatos:
        num_votos = votos.filter(candidato=candidato).count()    
        candidato_votos.append(num_votos)
    
    todo = {}
    for candidato, voto in zip(candidatos, candidato_votos):
        todo[candidato] = voto

    context = {
        'candidatos': todo
    }
    return render(request, 'conteo_votos.html', context)

def grafica (request):
    votos = Votacion.objects.all()
    candidato_votos = []
    candidatos = Candidato.objects.all()
    for candidato in candidatos:
        num_votos = votos.filter(candidato=candidato).count()    
        candidato_votos.append(num_votos)
    
    todo = {}
    for candidato, voto in zip(candidatos, candidato_votos):
        todo[candidato] = voto

    context = {
        'candidatos': todo
    }
    return render(request,'grafica.html',context)