from name_func import get_full_name


def test_first_last_name():
    full_name = get_full_name("a", "b")

    assert full_name == "A B"


def test_first_last_middle_name():
    full_name = get_full_name("a", "b", "c")

    assert full_name == "A C B"
