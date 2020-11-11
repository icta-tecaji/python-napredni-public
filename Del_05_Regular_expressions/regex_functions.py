import re
import pandas as pd


def read_data():
    hn = pd.read_csv("Del_05_Regular_expressions/data/hacker_news.csv")
    titles = hn["title"].to_list()
    titles_str = " ".join(titles)
    return titles_str


def validate_email(email: str) -> bool:
    pattern = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|
                    \\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9]
                    [0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\
                    [\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

    if re.match(pattern, email):
        return True
    else:
        return False


if __name__ == "__main__":
    # # Priprava podatkov
    # titles_str = read_data()

    # # MATCH metoda
    # print(re.match(r"danes", "danes je oblačen dan"))
    # print(re.match(r"je", "danes je oblačen dan"))

    # print(validate_email("dsdsd@gdf..vom"))

    # # FINDALL -> Find all matches of a pattern.
    # print(re.findall(r"[Py]ython\s?\d?\.\d?", titles_str))

    # # re.split(<REGEX>, str)
    # print(re.split(r"[Py]", "daens uporabljamo Pytohn ali python"))

    # # re.sub(<REGEX>, str)
    # print(re.sub(r"[Pp]ython", "PYTHON", "daens uporabljamo Python ali python"))

    # VAJA
    test_urls = [
        "https://www.amazon.com/Technology-Ventures-Enterprise-Thomas-Byers/dp/0073523429",
        "http://www.interactivedynamicvideo.com/",
        "http://www.nytimes.com/2007/11/07/movies/07stein.html?_r=0",
        "http://evonomics.com/advertising-cannot-maintain-internet-heres-solution/",
        "HTTPS://github.com/keppel/pinn",
        "Http://phys.org/news/2015-09-scale-solar-youve.html",
        "https://iot.seeed.cc",
        "http://www.bfilipek.com/2016/04/custom-deleters-for-c-smart-pointers.html",
        "http://beta.crowdfireapp.com/?beta=agnipath",
        "https://www.valid.ly?param",
    ]

    pattern = r"(?P<protocol>.+)://(?P<domain>[\w\.]+)/?(?P<path>.*)"

    for url in test_urls:
        comp = re.search(pattern, url)
        print(comp.group("protocol"))
        print(comp.group("domain"))
        print(comp.group("path"))
        print("---------------")
