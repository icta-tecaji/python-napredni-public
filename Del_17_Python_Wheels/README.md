# Del 17: Python Wheels

- Wheels are a component of the Python ecosystem that helps to make package installs just work.
- A Python .whl file is essentially a ZIP (.zip) archive with a specially crafted filename that tells installers what Python versions and platforms the wheel will support.
- A wheel filename:
    - `{dist}-{version}(-{build})?-{python}-{abi}-{platform}.whl`
    - Primer: `cryptography-3.2.1-cp35-abi3-manylinux2010_x86_64.whl`
- Different Types of Wheels:
    - A **universal wheel** contains py2.py3-none-any.whl. It supports both Python 2 and Python 3 on any OS and platform. The majority of wheels listed on the Python Wheels website are universal wheels.
    - A **pure-Python wheel** contains either py3-none-any.whl or py2.none-any.whl. It supports either Python 3 or Python 2, but not both. It’s otherwise the same as a universal wheel, but it’ll be labeled with either py2 or py3 rather than the py2.py3 label.
    - A **platform wheel** supports a specific Python version and platform. It contains segments indicating a specific Python version, ABI, operating system, or architecture.

## Wheel vs Egg
- Wheel and Egg are both packaging formats that aim to support the use case of needing an install artifact that doesn’t require building or compilation, which can be costly in testing and production workflows.
- The Egg format was introduced by setuptools in 2004, whereas the Wheel format was introduced by PEP 427 in 2012.
- Wheel is currently considered the standard for built and binary packaging for Python.
