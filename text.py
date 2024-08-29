def decorayer_func(func):
    def wrapper_func(*args, **kwargs):
        print(f'Starting function: {func.__name__}')
        result = func(*args, **kwargs)
        print(f'Finished function: {func.__name__}')
        return result
    return wrapper_func
@decorayer_func
def my_func(text):
    return text.upper()

print(my_func('hello'))  # Output: STARTING FUNCTION: my_func

