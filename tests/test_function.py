from src.function import *

def test_print_values(capsys):
    num1 = 1
    num2 = 2
    
    print_values(1,2)
    captured = capsys.readouterr()
    outputs = captured.out.split('\n')

    assert outputs[0] == "num_a: 1"
    assert outputs[1] == "num_b: 2"
    assert outputs[2] == "sum: 3"
