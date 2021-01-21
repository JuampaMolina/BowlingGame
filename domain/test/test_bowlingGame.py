from src.bowlingGame import Bowling
import pytest

# https://www.bowlinggenius.com/


def test_rollNormal():
    assert Bowling('12345123451234512345').game_score() == 60
    assert Bowling('11111111111111111111').game_score() == 20


def test_rollGutterball():
    assert Bowling('-2345-2345-2345-2345').game_score() == 56
    assert Bowling('9-9-9-9-9-9-9-9-9-9-').game_score() == 90


def test_rollSpare():
    assert Bowling('1/34512/451234512/45').game_score() == 93
    assert Bowling('5/5/5/5/5/5/5/5/5/5/5').game_score() == 150 # arreglar


def test_rollStrike():
    assert Bowling('12X5123X1234X2345').game_score() == 82
    assert Bowling('12X5123XX34X2345').game_score() == 106

def test_perfectGame():
    assert Bowling('XXXXXXXXXXXX').game_score() == 300 # arreglar

def test_rollStrike_three():
    assert Bowling('12X5123X1234X2345').game_score() == 82
    assert Bowling('12X5123XX34X2345').game_score() == 106
    assert Bowling('12X51XXX34X2345').game_score() == 131
