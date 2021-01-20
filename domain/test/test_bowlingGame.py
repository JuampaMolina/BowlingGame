from domain.src.bowlingGame import Bowling
import pytest

def test_normal():
    assert Bowling.normal('1')
