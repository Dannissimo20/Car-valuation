import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"[START] {func.__name__}")
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"[END] {func.__name__} | Time: {elapsed:.6f} sec")
        
        return result

    return wrapper