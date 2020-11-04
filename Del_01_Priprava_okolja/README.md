# Del 01: Priprava okolja

## VS Code
- https://code.visualstudio.com/
- [VS Code Remote Development](https://code.visualstudio.com/docs/remote/remote-overview)
- [Working with Jupyter Notebooks in Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)
- [Using Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)
- [Remote development on a raspberry pi with ssh and VSCode](https://medium.com/@pythonpow/remote-development-on-a-raspberry-pi-with-ssh-and-vscode-a23388e24bc7)


## Pyenv (Linux, Mac)
- Orodje za upravljanje z več Python verzijami
- https://github.com/pyenv/pyenv
- Za Windows: https://github.com/pyenv-win/pyenv-win (osnovna podpora)
- Virtualna oklja s pomočjo pyenv -> [tutorial](https://realpython.com/intro-to-pyenv/#virtual-environments-and-pyenv)


### Namestitev
- `sudo apt-get update`
- `sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl`
- `curl https://pyenv.run | bash`
- Dodamo v `~/.bashrc`:
```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
- `exec "$SHELL"`

### Uporaba
- Seznam verzij, ki jih je možno namestiti:
    - `pyenv install --list`
- Namestitev:
    - `pyenv install -v <PYTHON_VERSION>`
- Seznam nameščenih verzij:
    - `pyenv versions`
- Izbira globalne verzije:
    - `pyenv global <PYTHON_VERSION>`
- Izbira lokalne verzije:
    - `pyenv local <PYTHON_VERSION>`

## venv — Creation of virtual environments
- https://docs.python.org/3/library/venv.html
- Ustvarjanje novega virtualnega okolja:
    - `python -m venv .venv`
- Aktivacija virtualnega okolja:
    - `source .venv/bin/activate`
- Deaktivacija virtualnega okolja:
    - `deactivate`

## pip - The Python Package Installer
- Posodobitetv pip-a:
    - `python -m pip install --upgrade pip`
- Namestitev paketov v datoteki `requirements.txt`:
    - `pip install -r requirements.txt`
- posodobitev paketov v datoteki `requirements.txt`:
    - `pip install --upgrade -r requirements.txt`
