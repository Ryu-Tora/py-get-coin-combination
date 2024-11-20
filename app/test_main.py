from app.main import get_coin_combination


def test_when_zero_cents():
    assert get_coin_combination(0) == [0, 0, 0, 0]


def test_one_cent():
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_six_cents():
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_17_cents():
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_50_cents():
    assert get_coin_combination(50) == [0, 0, 0, 2]


def test_list():
    assert isinstance(get_coin_combination(1), list)
