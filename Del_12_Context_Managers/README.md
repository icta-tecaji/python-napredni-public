# Del 12: Context Managers

- A context manager, in Python, is a resource acquisition and release mechanism that prevents resource leak and ensures startup and cleanup (exit) actions are always done.
- Sintaksa:
```python
with something_that_returns_a_context_manager() as my_resource:
    do_something(my_resource)
    ...
    print('done using my_resource')
```
- Klasičen primer je odpiranje datotek
- [contextlib — Utilities for with-statement contexts](https://docs.python.org/3/library/contextlib.html)

