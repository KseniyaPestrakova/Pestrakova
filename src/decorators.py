def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a') as f:
                        f.write(f'{func.__name__} {result}\n')
                        return result
                else:
                    print(f'{func.__name__} {result}')
                    return result
            except Exception as e:
                if filename:
                    with open(filename, 'a') as f:
                        f.write(f'{func.__name__} error:{e}. Inputs: {args},{kwargs}\n')
                else:
                    print(f'{func.__name__} error:{e}. Inputs: {args},{kwargs}\n')

        return wrapper
    return decorator


@log() #filename="mylog.txt"
def my_function(x, y):
    return x + y

my_function(1, 7)
my_function(1, 8)
my_function(5, 7)
my_function(5, '7')
