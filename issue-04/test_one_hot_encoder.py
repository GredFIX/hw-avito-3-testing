import pytest
import one_hot_encoder


def test_standart_work():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_empty_list():
    actual = one_hot_encoder.fit_transform([])
    expected = []
    assert actual == expected


def test_one_city():
    cities = ['Moscow']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [('Moscow', [1])]
    assert actual == expected


def test_empty():
    with pytest.raises(TypeError):
        one_hot_encoder.fit_transform()
