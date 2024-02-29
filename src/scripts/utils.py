from typing import Dict, List

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}


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


def get_movies(url: str, api_key: str, imdb_ids: List[str]) -> List[Dict[str, str]]:

    params: dict = {
        "apikey": api_key,
    }
    results: List[Dict] = []

    for imdb_id in imdb_ids:

        params["i"] = imdb_id
        response = requests.get(url, params=params)

        if response.status_code == 200:
            result = response.json()
            results.append(result)

        try:
            print(
                f"Tittle: {result['Title']}\n"
                f"Director: {result['Director']}\n"
                f"Actors: {result['Actors']}\n"
                f"Year: {result['Year']}\n"
                f"_____________"
            )
        except KeyError as e:

            print(f"KeyError: {e} - Some key is missing in the result dictionary.")
            continue

    return results
