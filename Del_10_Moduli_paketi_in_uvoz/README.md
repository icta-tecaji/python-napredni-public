# Del 10: Moduli, paketi in uvoz

Prednosti uporabe modulov v Python-u:
- Enostavnost
- Lažje vzdrževanje
- Ponovna uporabnost
- Ločeni imenski prostori (namespaces)

## Uporaba import stavka
Več možnnih načinov:
- `import <module_name>`
- `import <module_name>[, <module_name> ...]`
- `from <module_name> import <name(s)>`
- `from <module_name> import *` (ni priporočeno v produkciji)
- `from <module_name> import <name> as <alt_name>`
- `import <module_name> as <alt_name>`

Priporočila za razporejnje import stavkov:
- Imports should always be written at the top of the file, after any module comments and docstrings.
- Imports should be divided according to what is being imported. There are generally three groups:
    - standard library imports (Python’s built-in modules)
    - related third party imports (modules that are installed and do not  belong to the current application)
    - local application imports (modules that belong to the current application)
- Each group of imports should be separated by a blank space.

## importlib.resources
- Resources are files that live within Python packages
- This module leverages Python’s import system to provide access to resources within packages. If you can import a package, you can access resources within that package. Resources can be opened or read, in either binary or text mode.
- [Dokumentacija](https://docs.python.org/3.9/library/importlib.html#module-importlib.resources) importlib.resources – Resources

## Struktura Python aplikaciji
- CLI - One-Off Script:
```
    helloworld/
    │
    ├── .gitignore
    ├── helloworld.py
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    ├── setup.py
    └── tests.py
```

- CLI - Installable Single Package
```
    helloworld/
    │
    ├── helloworld/
    │   ├── __init__.py
    │   ├── helloworld.py
    │   └── helpers.py
    │
    ├── tests/
    │   ├── helloworld_tests.py
    │   └── helpers_tests.py
    │
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    └── setup.py
```

- CLI - Application with Internal Packages
```
    helloworld/
    │
    ├── bin/
    │
    ├── docs/
    │   ├── hello.md
    │   └── world.md
    │
    ├── helloworld/
    │   ├── __init__.py
    │   ├── runner.py
    │   ├── hello/
    │   │   ├── __init__.py
    │   │   ├── hello.py
    │   │   └── helpers.py
    │   │
    │   └── world/
    │       ├── __init__.py
    │       ├── helpers.py
    │       └── world.py
    │
    ├── data/
    │   ├── input.csv
    │   └── output.xlsx
    │
    ├── tests/
    │   ├── hello
    │   │   ├── helpers_tests.py
    │   │   └── hello_tests.py
    │   │
    │   └── world/
    │       ├── helpers_tests.py
    │       └── world_tests.py
    │
    ├── .gitignore
    ├── LICENSE
    └── README.md
```