from src.bowlingGame import Bowling
import pytest

# https://www.bowlinggenius.com/


def test_rollNormal():
    assert Bowling('12345123451234512345').advance_roll() == 60
    assert Bowling('11111111111111111111').advance_roll() == 20


def test_rollGutterball():
    assert Bowling('-2345-2345-2345-2345').advance_roll() == 56
    assert Bowling('9-9-9-9-9-9-9-9-9-9-').advance_roll() == 90


def test_rollSpare():
    assert Bowling('1/34512/451234512/45').advance_roll() == 93
#    assert Bowling('5/5/5/5/5/5/5/5/5/5/5').advance_roll() == 150


def test_rollStrike():
    assert Bowling('12X5123X1234X2345').advance_roll() == 82
    assert Bowling('12X5123XX34X2345').advance_roll() == 106


""" 
def test_perfectGame():
    assert Bowling('XXXXXXXXXXXX').advance_roll() == 300 """


def test_rollStrike_three():
    assert Bowling('12X5123X1234X2345').advance_roll() == 82
    assert Bowling('12X5123XX34X2345').advance_roll() == 106
    assert Bowling('12X51XXX34X2345').advance_roll() == 131
