import unittest
import one_hot_encoder


class TestOneHot(unittest.TestCase):
    def test_standart_work(self):
        cities = ["Moscow", "New York", "Moscow", "London"]
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ("Moscow", [0, 0, 1]),
            ("New York", [0, 1, 0]),
            ("Moscow", [0, 0, 1]),
            ("London", [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_not_zero(self):
        cities = ["Moscow"]
        actual = one_hot_encoder.fit_transform(cities)
        expected = [("Moscow", [2])]
        self.assertNotEqual(actual, expected)

    def test_list(self):
        cities = ["London"]
        actual = one_hot_encoder.fit_transform(cities)
        expected = [("London", [1])]
        self.assertIsNot(actual, expected)

    def test_empty(self):
        with self.assertRaises(TypeError):
            one_hot_encoder.fit_transform()
