# Del 06: Procesiranje podatkov

## Comprehensions
- List Comprehension: 
    - `new_list = [expression for member in iterable]`
    - `new_list = [expression for member in iterable (if conditional)]`
    - `new_list = [expression (if conditional) for member in iterable]`
- Dictionary Comprehension
    - `new_dict = {k: v for (k, v) in original_dict.items()`
- Deluje hitreje kot z normalnimi for zankami
- Primer pretvorbe for zanke v List Comprehension:

```python
# klasičen način
squares = []
for i in range(10):
    squares.append(i * i)

print(squares)

# List Comprehension
squares = [i * i for i in range(10)]
```

## Lambda funkcije
- Majhne anonimne funkcije
- Primer:
```python
# klasična funkcija
def add_one(x):
    return x + 1

# lambda funkcija
lambda x: x + 1
```

## Map, filter, reduce funkcije
- Več [tukaj](https://www.learnpython.org/en/Map,_Filter,_Reduce)

