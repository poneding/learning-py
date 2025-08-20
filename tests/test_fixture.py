import pytest


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


@pytest.fixture
def user():
    return User(1, "dp")


def test_get_name(user):
    assert user.name == "dp"


def test_user_id(user):
    assert user.id == 1
