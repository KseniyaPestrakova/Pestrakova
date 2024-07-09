from typing import Any

from src.decorators import log, my_function_file


def test_log_without_filename(capsys: Any) -> None:
    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    my_function(4, 5)
    captured = capsys.readouterr()
    assert captured.out == "my_function 9\n"


def test_log_without_filename_error(capsys: Any) -> None:
    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    my_function(5, "7")
    captured = capsys.readouterr()
    assert captured.out == (
        "my_function error:unsupported operand type(s) for +: 'int' and 'str'. Inputs: (5, " "'7'),{}\n"
    )


def test_log_result_with_filename() -> None:
    @log(filename="mylog.txt")
    def my_function_file(x: Any, y: Any) -> Any:
        return x + y

    result = my_function_file(4, 5)
    assert result == 9


@log(filename="mylog.txt")
def test_log_with_filename() -> None:

    my_function_file(4, 5)
    with open("mylog.txt", "r", encoding="utf-8") as f:
        result = f.read()
        assert result == "my_function_file 9\n"


@log(filename="mylog.txt")
def test_log_with_filename_error() -> None:

    my_function_file(4, "5")
    with open("mylog.txt", "r", encoding="utf-8") as f:
        result = f.read()
        assert result == (
            "my_function_file error:unsupported operand type(s) for +: 'int' and 'str'. Inputs: (4, " "'5'),{}\n"
        )
