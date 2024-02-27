import time
from typing import Dict, List

import requests
from bs4 import BeautifulSoup

API_KEY_OMDB = "ff3e7091"
BASE_URL = "http://www.omdbapi.com/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}
url_imdb_top = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"


def create_soup(url) -> BeautifulSoup:
    sessinon = requests.Session()
    response = sessinon.get(url=url, headers=headers)

    if response.status_code == 200:

        html_content = response.text
        return BeautifulSoup(html_content, "html.parser")

    else:
        raise requests.HTTPError(f"Error: {response.status_code}")


def get_imdb_ids_top(url) -> List[str]:
    soup = create_soup(url=url)

    links: List[str] = soup.find_all("a", class_="ipc-title-link-wrapper", href=True)

    imdb_ids: List[str] = []

    for link in links:
        href = link["href"]
        if "title/tt" in href:
            parts: List[str] = href.split("/")
            imdb_id: str = parts[2].split("?")[0]
            imdb_ids.append(imdb_id)
    print(len(imdb_ids))

    return imdb_ids


def get_movies(url: str, api_key: str, imdb_ids: List[str]) -> Dict[str, str]:

    params = {
        "apikey": api_key,
    }

    for imdb_id in imdb_ids[:10]:

        params["i"] = imdb_id
        response = requests.get(url, params=params)

        if response.status_code == 200:
            movie_data = response.json()

        print(
            f"Tittle: {movie_data['Title']}\n"
            f"Director: {movie_data['Director']}\n"
            f"Actors: {movie_data['Actors']}\n"
            f"_____________"
        )

        time.sleep(3)

    return movie_data


imdb_ids = get_imdb_ids_top(url_imdb_top)
get_movies(url=BASE_URL, api_key=API_KEY_OMDB, imdb_ids=imdb_ids)
