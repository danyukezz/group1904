import pytest
from faker import Faker
from hw25_1 import Account, AccountType

fake_gen = Faker(locale='uk_UA')


class TestCurrentAccount:
    @pytest.fixture
    def current_account():
        return Account(AccountType.CURRENT)


class TestDepositAccount:
    @pytest.fixture
    def deposit_account():
        return Account(AccountType.DEPOSIT)
