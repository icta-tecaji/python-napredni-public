# Del 21: Fast API
- FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- https://fastapi.tiangolo.com/


## Priprava okolja
- Python lokalna verzija: `pyenv local 3.9.5`
- Ustvarjanje novega virtualnega okolja: `python -m venv .venv`
- Aktivacija virtualnega okolja: `source .venv/bin/activate`
- Ustvarimo `requirements_dev.txt` in `requirements.txt`
- Namesitmo vse potrebne pakete: `pip install -r requirements_dev.txt`
- Dodamo `.vscode` mapo
- Dodamo `.gitignore`

## Zagon aplikacije
- `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

## Zagon aplikacije (Docker)
- Namestimo Docker s pomočjo skripte:
    - `chmod +x install_docker.sh`
    - `./install_docker.sh`
- Zaženemo aplikacijo:
    - `docker-compose up --build`
- Povezava do baze (v novem terminalu):
    - `docker-compose exec db psql --username=firstapp --dbname=firstapp`
    - Podtakovne baze: `\l`
    - `\c firstapp`
    - `\dt`
    - `SELECT * FROM users;`

## Gradiva
- [Dockerizing FastAPI with Postgres, Uvicorn, and Traefik](https://testdriven.io/blog/fastapi-docker-traefik/)
- [Developing a Single Page App with FastAPI and React](https://testdriven.io/blog/fastapi-react/)
- [Securing FastAPI with JWT Token-based Authentication](https://testdriven.io/blog/fastapi-jwt-auth/)
- [Asynchronous Tasks with FastAPI and Celery](https://testdriven.io/blog/fastapi-and-celery/)
