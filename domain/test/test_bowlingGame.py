from src.bowlingGame import Bowling
import pytest

# https://www.bowlinggenius.com/


def test_rollNormal():
    assert Bowling('12345123451234512345').game_score() == 60


def test_rollGutterball():
    assert Bowling('-2345-2345-2345-2345').game_score() == 56


def test_rollSpare():
    assert Bowling('1/34512/451234512/45').game_score() == 93


def test_rollStrike():
    assert Bowling('12X5123X1234X2345').game_score() == 82
    assert Bowling('12X5123XX34X2345').game_score() == 106
