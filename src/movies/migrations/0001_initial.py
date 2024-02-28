# Generated by Django 4.1.13 on 2024-02-27 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("tittle", models.CharField(max_length=255, unique=True)),
                ("release_year", models.PositiveIntegerField()),
                ("actors", models.ManyToManyField(related_name="acted_movies", to="movies.person")),
                ("directors", models.ManyToManyField(related_name="directed_movies", to="movies.person")),
            ],
        ),
    ]
