"""

"""

import sys
from functools import wraps
import time
from typing import Callable, Iterable, Iterator
from concurrent.futures import ThreadPoolExecutor
from collections import deque

class Timer:
    """This context manager allows timing blocks of code."""
    def __enter__(self):
        self._timer = time.time()
        return self

    def __exit__(self, *args):
        self.elapsed = time.time() - self._timer


def threaded_map(fn: Callable, data: Iterable, max_workers: int = None) -> Iterator:
    with ThreadPoolExecutor(max_workers = max_workers) as executor:
        return executor.map(fn, data)
    
    
ignore_pattern = re.compile(r'__?.+(__)?')

def show_attrs(obj):
    """Prints all available attrs of obj"""
    deque(map(print, filter(lambda attr: not re.fullmatch(ignore_pattern, attr), dir(obj))), maxlen=0)


def retryable(
            f: Callable = None,
            *,
            max_tries: int = 1,
            wait_time: Callable = (lambda t: 0.1),
            err_msg: str = None,
            verbose: bool = True
        ) -> Callable:
    def decorator(g):
        @wraps(g)
        def wrapper(*args,**kwargs):
            err = None
            for try_i in range(max_tries + 1):
                try:
                    return g(*args, **kwargs)
                except Exception as e:
                    err = e
                    if verbose: warning(err_msg or f'exhausted retries when attempting to run "{f.__name__}"' + ' -- trying again')
                    time.sleep(wait_time(try_i))
            if verbose: warning(err_msg or f'exhausted retries when attempting to run "{f.__name__}"')
            raise err
        return wrapper

    if f:
        return decorator(f)
    else:
        return decorator
    
    
def count(data: Iterable) -> dict:
    """Counts number of occurrences for each item in list."""
    return {el: list(data).count(el) for el in set(data)}
    
    
def warning(msg: str) -> None:
    """Prints warning."""
    print(f'WARNING: {msg}')


def fatal_error(msg: str) -> None:
    """Prints error and exits program."""
    print(f'ERROR: {msg}')
    print('Exiting...')
    sys.exit()


def make_title(msg: str) -> str:
    """Returns basic title string."""
    return (
        f'+{(len(msg) + 2)*"="}+\n'
        f'| {msg} |\n'
        f'+{(len(msg) + 2)*"="}+'
    )
