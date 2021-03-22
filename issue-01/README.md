## Запуск тестов doctest

```bash
python3 -m doctest -o NORMALIZE_WHITESPACE -v morse.py
```

## Результат теста

```bash
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode(SOS)
Expecting:
    Traceback (most recent call last):
        ...
    NameError: name 'SOS' is not defined
ok
Trying:
    encode('NUZHDENKO') # doctest: +ELLIPSIS
Expecting:
    '-. ..- --.. ... -.- ---'
ok
2 items had no tests:
    morse
    morse.decode
1 items passed all tests:
   3 tests in morse.encode
3 tests in 3 items.
3 passed and 0 failed.
Test passed.
```
