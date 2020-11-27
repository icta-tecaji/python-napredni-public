# Del 13: Testiranje kode

## Testiranje

### unittest
- https://docs.python.org/3/library/unittest.html
- Metode za preverjanje:
    - `.assertEqual(a, b)` -> 	`a == b`
    - `.assertTrue(x)` -> `bool(x) is True`
    - `.assertFalse(x)` -> `bool(x) is False`
    - `.assertIs(a, b)` -> `a is b`
    - `.assertIsNone(x)` -> `x is None`
    - `.assertIn(a, b)` -> `a in b`
    - `.assertIsInstance(a, b)` -> `isinstance(a, b) `
- Zagon testiranja:
    - `python -m unittest -v <IME DATOTEKE>`
    - `python -m unittest discover`
    - `python -m unittest discover -s <IME_MAPE_S_TESTI>`

### pytest
- https://docs.pytest.org/en/stable/
- Namestitev: `python -m pip install pytest`

### Testiranje v več okoljih
- Tox is an application that automates testing in multiple environments.
- You might want to check that your application works on multiple versions of Python, or multiple versions of a package. 
- `python -m pip install tox`
- [Welcome to the tox automation project](https://tox.readthedocs.io/en/latest/)