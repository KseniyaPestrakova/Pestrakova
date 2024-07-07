from typing import Any


def log(filename: Any = None) -> Any:
    def decorator(func: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{func.__name__} {result}\n")
                        return result
                else:
                    print(f"{func.__name__} {result}")
                    return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{func.__name__} error:{e}. Inputs: {args},{kwargs}\n")
                else:
                    print(f"{func.__name__} error:{e}. Inputs: {args},{kwargs}\n")

        return wrapper

    return decorator


@log()
def my_function(x: Any, y: Any) -> Any:
    return x + y


my_function(1, 7)
my_function(5, "7")


@log(filename="mylog.txt")
def my_function_file(x: Any, y: Any) -> Any:
    return x + y


my_function(4, 5)
my_function(5, "7")
