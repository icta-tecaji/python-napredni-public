import requests

URL = "https://drive.google.com/uc?export=download&id=0B6ZlG_Eygdj-c1kzcmUxN05VUXM"
SURVEY_NAME = "survey2017"

request = requests.get(URL)

with open(f"{SURVEY_NAME}.zip", "wb") as file:
    file.write(request.content)
