import pytest
from helpers.wallet import InsufficientAmount, Wallet


@pytest.fixture
def empty_wallet():
    """Returns a Wallet instance with zero balance"""
    return Wallet()


@pytest.fixture
def wallet():
    """Returns a Wallet instance with balance of 20"""
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)


@pytest.mark.parametrize("earned, spent, expected", [(30, 10, 20), (20, 2, 18)])
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected


def test_add():
    assert 15 + 13 == 100, "failed"


@pytest.mark.xfail
def test_add_2():
    assert 15 + 13 == 28, "failed"


@pytest.mark.skip
def test_add_3():
    assert 100 + 200 == 400, "failed"


@pytest.mark.skip
def test_add_4():
    assert 100 + 200 == 300, "failed"
