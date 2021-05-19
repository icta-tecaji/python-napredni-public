# Del 19: Uvod v concurrency in Parallelism

## PyPy
- A fast, compliant alternative implementation of Python. On average, PyPy is 4.2 times faster than CPython.
- https://www.pypy.org/
- Namestitev in uporaba: 
    - `pyenv install -v pypy3.7-7.3.4`
    - Zamenjava interpreterja v lokalni mapi: `pyenv local pypy3.7-7.3.4`

## Numba
- http://numba.pydata.org/
- Numba translates Python functions to optimized machine code at runtime using the industry-standard LLVM compiler library. Numba-compiled numerical algorithms in Python can approach the speeds of C or FORTRAN.


## Concurrency vs Parallelism
- `Concurrency` is the ability to run multiple tasks on the CPU at the same time. Tasks can start, run, and complete in overlapping time periods. In the case of a single CPU, multiple tasks are run with the help of context switching, where the state of a process is stored so that it can be called and executed later.
- `Parallelism`, meanwhile, is the ability to run multiple tasks at the same time across multiple CPU cores.

## Parallelism
- **Pre-emptive multitasking (threading)** -> The operating system decides when to switch tasks external to Python. (1 procesor)
- **Cooperative multitasking (asyncio)** -> The tasks decide when to give up control. (1 procesor)
- **Multiprocessing (multiprocessing)** -> The processes all run at the same time on different processors. (število procesov na računalniku)

## AsyncIO

## Threading

## Multiprocessing
