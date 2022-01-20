import pytest
from main import withdraw, deposit


@pytest.fixture()
def check(yeild):
    print("test about to start...!!")
    yeild

    print("Testing is completed..!!")


def test_withdraw(check):
    assert withdraw(5000) == 0


def test_deposit(check):
    assert deposit(100) == 200
