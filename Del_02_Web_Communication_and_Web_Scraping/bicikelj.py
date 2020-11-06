from make_request import get_api_data


def parse_biciklej_stations(data: dict) -> list:
    postaje = []
    for _, postaja in data["markers"].items():
        postaje.append(postaja["fullAddress"])
    return postaje


def parse_bicikelj_available_bikes(data: dict) -> int:
    # avail_bikes = 0
    # for _, postaja in data["markers"].items():
    #     avail_bikes = avail_bikes + int((postaja["station"]["available"]))

    # return avail_bikes
    return sum(
        [int(postaja["station"]["available"]) for _, postaja in data["markers"].items()]
    )


def parse_bicikelj_free_spots(data: dict) -> int:
    avail_bikes = 0
    for _, postaja in data["markers"].items():
        avail_bikes = avail_bikes + int((postaja["station"]["free"]))

    return avail_bikes


if __name__ == "__main__":
    bicikelj_url = "https://opendata.si/promet/bicikelj/list/"
    data = get_api_data(bicikelj_url)

    postaje = parse_biciklej_stations(data)
    print(postaje)

    prosta_kolesa = parse_bicikelj_available_bikes(data)
    print(prosta_kolesa)

    prosta_mesta = parse_bicikelj_free_spots(data)
    print(prosta_mesta)
