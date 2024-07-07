from typing import Any


def log(filename: Any = None) -> Any:
    """Логирует выполнение функции: выводит наименование использованной функции и результат в случае успешного
     выполнения, а в случае ошибки выводит тип возникшей ошибки и входные параметры"""
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
                    print(f"{func.__name__} error:{e}. Inputs: {args},{kwargs}")

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function_file(x: Any, y: Any) -> Any:
    '''Выводим функцию для проверки работы декоратора'''
    return x + y
