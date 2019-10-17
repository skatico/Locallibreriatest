from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre


# Create your views here.

def index(request):
    #funcion vista para la pagina inicio del sitio

    #Genera contadores de algunos de los objetos principales
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    #libros disponibles (status - 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_author=Author.objects.count() #el all siempre esta por defecto

    #renderiza o reenviar la plantilla html index.html con los datos en la variable contexto
    #render=reenvia

    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_author':num_author},

    )


