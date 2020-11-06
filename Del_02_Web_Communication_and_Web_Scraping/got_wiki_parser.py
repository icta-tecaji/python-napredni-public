import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_page_soup(url: str, parser: str = "html.parser"):
    r = requests.get(url)
    html_contents = r.text
    html_soup = BeautifulSoup(html_contents, "html.parser")
    return html_soup


def get_citations(soup_obj, num_of_citations: int = 5) -> list:
    cites = soup_obj.find_all("cite", {"class": "citation"}, limit=num_of_citations)
    cite_list = []
    for citation in cites:
        text = citation.text
        link = citation.find("a").get("href")
        cite_list.append((text, link))
    return cite_list


def analyze_viewers_for_season(season: int, operation="sum"):
    if isinstance(season, int):
        if (season < 1) or (season > 8):
            raise ValueError("Season number must be 1-8.")
    else:
        raise ValueError("Season number must be 1-8.")

    if operation not in ["sum", "mean"]:
        raise ValueError("Operation must be sum or mean.")

    url_got = "https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes"
    tables = pd.read_html(url_got)
    season_table = tables[season]
    viewers = (
        season_table["U.S. viewers(millions)"].str.split("[").str[0].astype("float")
    )

    if operation == "sum":
        viewers_sum = viewers.sum()
        return round(viewers_sum, 2)
    elif operation == "mean":
        viewers_mean = viewers.mean()
        return round(viewers_mean, 2)


if __name__ == "__main__":
    url_got = "https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes"
    soup = get_page_soup(url=url_got)

    # citation = get_citations(soup, 3)
    # print(citation)

    print(analyze_viewers_for_season(6, "mean"))
