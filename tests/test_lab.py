import random

def test_ok():
    assert 1 + 1 == 2

def test_sometimes():
    assert random.random() < 0.9
