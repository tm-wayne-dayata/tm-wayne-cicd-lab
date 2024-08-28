from src.function import *
import pytest

def test_print_values_valid_type_case(capsys):
    num1 = 1
    num2 = 2
    
    print_values(num1, num2)
    captured = capsys.readouterr()
    outputs = captured.out.split('\n')

    assert outputs[0] == "num_a: 1"
    assert outputs[1] == "num_b: 2"
    assert outputs[2] == "sum: 3"


def test_print_values_invalid_type_case(capsys):
    num1 = 'bad'
    num2 = 'input'
    
    with pytest.raises(TypeError):
        print_values(num1, num2)


def test_print_values_empty_case(capsys):
    num1 = None
    num2 = None
    
    with pytest.raises(TypeError):
        print_values(num1, num2)