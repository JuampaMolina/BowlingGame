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
    assert Bowling('5/5/5/5/5/5/5/5/5/5/5').advance_roll() == 150
    assert Bowling('5/324/5/343152424152').advance_roll() == 82
    assert Bowling('3/4/5/3/1/421/8/2/6/7').advance_roll() == 136


def test_rollStrike():
    assert Bowling('12X5123X1234X2345').advance_roll() == 82
    assert Bowling('12X5123XX34X2345').advance_roll() == 106


def test_perfectGame():
    assert Bowling('XXXXXXXXXXXX').advance_roll() == 300


def test_rollStrike_three():
    assert Bowling('12X5123X1234X2345').advance_roll() == 82
    assert Bowling('12X5123XX34X2345').advance_roll() == 106
    assert Bowling('12X51XXX34X2345').advance_roll() == 131


def test_pau():
    assert Bowling('32611661144527814225').advance_roll() == 71
    assert Bowling('12345123451234512345').advance_roll() == 60
    assert Bowling('5/5/5/5/5/5/5/5/5/5/5').advance_roll() == 150
    assert Bowling('5/324/5/343152424152').advance_roll() == 82
    assert Bowling('3/4/5/3/1/421/8/2/6/7').advance_roll() == 136
    assert Bowling('9-9-9-9-9-9-9-9-9-9-').advance_roll() == 90
    assert Bowling('2-452763----4245326-').advance_roll() == 55
    assert Bowling('X24X17332542143517').advance_roll() == 88
    assert Bowling('42X4225X5224524536').advance_roll() == 90
    assert Bowling('3518X54X24X71X31').advance_roll() == 111
    assert Bowling('X6-52X7-4245722662').advance_roll() == 93
    assert Bowling('X-471X-84215724571').advance_roll() == 90
    assert Bowling('X-/42X-/5215423681').advance_roll() == 112
    assert Bowling('X--42X--5234411836').advance_roll() == 63
    assert Bowling('XX6272X6235721662').advance_roll() == 119
    assert Bowling('XX5326XX52523651').advance_roll() == 130
    assert Bowling('XXXXXXXXXXXX').advance_roll() == 300
    assert Bowling('XX-625XX-5136235').advance_roll() == 109
    assert Bowling('625/6353X436/2441-5').advance_roll() == 93
    assert Bowling('2/6/X639/6/-4XXXXX').advance_roll() == 184


"""     assert Bowling('4/X-/4/-/XX7/4/7/X').advance_roll() == 182
    assert Bowling('26X3/4281X422/5/2/5').advance_roll() == 121
    assert Bowling('5/3/X9---2/4/XXX4/').advance_roll() == 169
    assert Bowling('XX4/4/3/XX2-1-XX9').advance_roll() == 157
    assert Bowling('317/4/-79/532/X4/XXX').advance_roll() == 148
    assert Bowling('X7/326/XX5/435/XXX').advance_roll() == 174
    assert Bowling('13635/6/8/X6/545/X7/').advance_roll() == 151
    assert Bowling('4/6/XX9/X8/XXXXX').advance_roll() == 235
 """
