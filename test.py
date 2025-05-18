import main
import pytest

def test_method():
    assert main.sum(2, 3) == 5
    assert main.sum(-1, 1) == 0
    assert main.sum(0, 0) == 0
    assert main.sum(1.5, 2.5) == 4.0
    assert main.sum(-1.5, 1.5) == 0.0
    assert main.sum(1, -1) == 0