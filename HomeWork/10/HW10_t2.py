def logger(message):
    if not isinstance(message, str):
        raise TypeError("logger argument must be a string")
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator
@logger('This function will sum 2 ints')
def plus(x, y):
    return x + y
# Try 1
result = plus(10, 20)
print(result)
