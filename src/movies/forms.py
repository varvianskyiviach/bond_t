from django import forms

from .models import Movie, Person


class MovieForm(forms.ModelForm):
    new_director_name = forms.CharField(max_length=255, required=False)
    new_actor_name = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Movie
        fields = ["title", "release_year"]

    def save(self, commit=True):
        movie_instance = super().save(commit=False)

        if not self.instance.pk:
            movie_instance.save()

        new_director_name = self.cleaned_data.get("new_director_name")
        new_actor_name = self.cleaned_data.get("new_actor_name")

        if new_director_name:
            new_director_names = [name.strip() for name in new_director_name.split(",")]
            for name in new_director_names:
                director, created = Person.objects.get_or_create(name=name)
                movie_instance.directors.add(director)

        if new_actor_name:
            new_actor_names = [name.strip() for name in new_actor_name.split(",")]
            for name in new_actor_names:
                actor, created = Person.objects.get_or_create(name=name)
                movie_instance.actors.add(actor)

        if commit:
            movie_instance.save()

        return movie_instance
