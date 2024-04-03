import time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        return result, time.time() - start_time
    return wrapper
@timing_decorator
def some_function(n):
    return sum(range(n))
result, time_taken = some_function(100000)
print(f"Result: {result}, Time Taken: {time_taken:.4f} seconds")
