# Del 07: Generatorji

- Python generatorji generirajo vrednosti eno po eno, namesto, da bi vrnili vse vrednosti na enkrat.
- Generator je funkcija, ki namesto returna vsebuje `yield`
- Primer:
```python
# countdown funkcija -> na klasični način de deluje po želji
def countdown(num):
    print('Starting')
    while num > 0:
        return num
        num -= 1
    print('Stop')

# funkcija s pomočjo generatorjev
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1
    print('Stop')


```