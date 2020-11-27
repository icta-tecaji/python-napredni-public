# Del 16: Code quality and styling

## Style Guides - PEP 8/PEP 257
- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)

### Naming Styles
- **Function** -	Use a lowercase word or words. Separate words by underscores to improve readability: `function`, `my_function`
- **Variable** - Use a lowercase single letter, word, or words. Separate words with underscores to improve readability:	`x`, `var`, `my_variable`
- **Class** - Start each word with a capital letter. Do not separate words with underscores. This style is called camel case: `Model`, `MyClass`
- **Method** - Use a lowercase word or words. Separate words with underscores to improve readability: `class_method`, `method`
- **Constant** - Use an uppercase single letter, word, or words. Separate words with underscores to improve readability: `CONSTANT`, `MY_CONSTANT`, `MY_LONG_CONSTANT`
- **Module** - Use a short, lowercase word or words. Separate words with underscores to improve readability: `module.py`, `my_module.py`
- **Package** - Use a short, lowercase word or words. Do not separate words with underscores: `package`, `mypackage`

### Linters & formaters
- **Flake8** (PyFlakes, pycodestyle (formerly pep8), Mccabe)
- **Pylint**: Checks for errors, tries to enforce a coding standard, looks for code smells
- **Black**: Formats Python code without compromise