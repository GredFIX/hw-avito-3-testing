## Запуск тестов pytest

```bash
pytest -v
```

## Результат выполнения

```bash
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/gredfix/testing/issue-04
plugins: Faker-6.6.0
collecting ... collected 4 items

test_one_hot_encoder.py::test_standart_work PASSED                       [ 25%]
test_one_hot_encoder.py::test_empty_list PASSED                          [ 50%]
test_one_hot_encoder.py::test_one_city PASSED                            [ 75%]
test_one_hot_encoder.py::test_empty PASSED                               [100%]

============================== 4 passed in 0.04s ===============================
```
