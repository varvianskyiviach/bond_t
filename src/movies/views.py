from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Movie

# from django.shortcuts import render

# # def movie_detail_page(request, pk):
# #     movie = Movie.objects.get(pk=pk)
# #     return render(request, 'movies/movie_detail.html', {"movie": movie})


class MovieListView(ListView):
    model = Movie
    template_name = "movies/movie_list.html"


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie_detail.html"


class MovieCreateView(CreateView):
    model = Movie
    fields = ["title", "release_year", "directors", "actors"]
    template_name = "movies/movie_form.html"
    success_url = reverse_lazy("movie_list")


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ["title", "release_year", "directors", "actors"]
    template_name = "movies/movie_form.html"
    success_url = reverse_lazy("movie_list")


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = "movies/movie_confirm_delete.html"
    success_url = reverse_lazy("movie_list")
