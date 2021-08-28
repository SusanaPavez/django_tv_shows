from django.shortcuts import render, redirect
from core.models import *
from django.contrib import messages

def tv_show(request):
    if request.method == 'GET':
        context = {
            'tvshows': TvShow.objects.all(),
        }
        return render(request, 'shows.html', context)


def add_show(request):

    # Esto muestra la página como tal
    if request.method == 'GET':
        context = {
            'add_show': 'hola',
        }
        return render(request, 'add_show.html', context)

    # Esto es para agregar un show a la lista
    if request.method == 'POST':
        # Envia formulario y luego redirige
        print(request.POST) 

        titulo = request.POST['title'] 
        cadena = request.POST['network']
        fecha_lanzamiento = request.POST['release_date']
        descripcion = request.POST['description']

        shows = TvShow.objects.create(
            title = titulo,
            network = cadena,
            release_date = fecha_lanzamiento,
            description = descripcion
            )
        # redirige a la página principal en modo GET
        return redirect('/')



def display_show(request, id):
    da_show = TvShow.objects.get(id=id)

    if request.method == 'GET':
        context = {
            'id' : id,
            'da_show' : da_show
        }
        return render(request, 'display_show.html', context)



def edit_show(request, id):
    
    da_show = TvShow.objects.get(id=id)

    if request.method == 'GET':
        context = {
            'id' : id,
            'da_show' : da_show
        }
        return render(request, 'edit_show.html', context)
    

    if request.method == 'POST':

        edit_title = request.POST['title']
        edit_network = request.POST['network']
        edit_release_date = request.POST['release_date']
        edit_description = request.POST['description']

    
    return redirect('display_show.html')


    
def delete_show(request, id):
    
    da_show = TvShow.objects.get(id=id)
    da_show.delete()

    return redirect('/')