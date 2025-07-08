from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.views import LoginView 
from django.contrib.auth.decorators import login_required

def index(request):
    movies = Movie.objects.order_by('name') # Obtiene todos los objetos Movie
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movies': movies}, request))


def movie_details(request, movie_id): 
    movie = get_object_or_404(Movie, Id=movie_id) 

    template = loader.get_template('movie_details.html')
    context = {
        'movie': movie # Pasa el objeto Movie completo a la plantilla
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies:index')  # Redirige a la lista de películas después de guardar
    else:
        form = MovieForm()
        
    return render(request, 'movie_form.html', {'form': form})

@login_required
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, Id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'movie_form.html', {'form': form})
@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, Id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    

class CustomLoginView(LoginView):
    template_name = 'login_form.html'
    