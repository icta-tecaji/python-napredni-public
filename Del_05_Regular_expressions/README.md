# Del 05: Regular Expressions

- Regular expressions are used to identify whether a pattern exists in a given sequence of characters (string) or not.
- Spletno orodje za pomoč: https://regexr.com/
- V pythonu uporabimo vgrajen modul `re` -> https://docs.python.org/3/library/re.html
- [Cheatsheet](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)

## Glavne metode modula re:
- `match()`: Determine if the RE matches at the beginning of the string
- `search()`: Scan through a string, looking for any location where this RE matches.
- `findall()`: Find all substrings where the RE matches, and returns them as a list.
- `finditer()`: Find all substrings where the RE matches, and returns them as an iterator.
- `re.split()`: Split string at each match.
- `re.sub()`: Replace one or many matches with a string.
- `re.fullmatch()`: If the whole string matches the regular expression pattern, return a corresponding match object.

