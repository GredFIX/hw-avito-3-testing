import pytest
import morse


@pytest.mark.parametrize(
    "s,exp",
    [
        ("... --- ...", "SOS"),
        ("-- .- ..", "MAI"),
        (".--. -.-- - .... --- -.", "PYTHON"),
    ],
)
def test_decode(s, exp):
    assert morse.decode(s) == exp
