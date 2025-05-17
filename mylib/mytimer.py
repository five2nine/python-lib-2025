from contextlib import contextmanager
from typing import Any, Generator

@contextmanager
def elapsed_timer() -> Generator[None, Any, None]:
    import time
    start: float = time.time()
    yield
    end: float = time.time()
    print(f"Elapsed time: {end - start}")
