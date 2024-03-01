from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MovieForm
from .models import Movie


def movies_page(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "movies/movie_list.html", {"page_obj": page_obj})


def movie_detail_page(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, "movies/movie_detail.html", {"movie": movie})


def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = MovieForm()

    return render(request, "movies/movie_form.html", {"form": form})


def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("movie_detail", pk=pk)
    else:
        form = MovieForm(instance=movie)

    return render(request, "movies/movie_form.html", {"form": form, "movie": movie})


def delete(request, pk):
    movie = Movie.objects.get(id=pk)

    if request.method == "POST":
        movie.delete()
        return redirect("movie_list")

    return render(request, "movies/movie_confirm_delete.html", {"movie": movie})
