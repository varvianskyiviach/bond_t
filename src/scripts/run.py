import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

url_imdb_top = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
url_omdb = "http://www.omdbapi.com/"
API_KEY_OMDB = os.getenv("API_KEY_OMDB")


def main():

    try:
        from task import fill_database_from_data
        from utils import get_imdb_ids_top, get_movies

    except Exception as e:
        print(f"An error occurred while importing : {e}")

    else:
        imdb_ids = get_imdb_ids_top(url_imdb_top)
        movies_data = get_movies(url=url_omdb, api_key=API_KEY_OMDB, imdb_ids=imdb_ids)
        fill_database_from_data(movies_data)


if __name__ == "__main__":
    main()
