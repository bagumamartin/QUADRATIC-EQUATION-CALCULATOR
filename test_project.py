import pytest
from project import InputError, is_valid_quadratic_equation_form, convert_to_numbers, compute


def main():
    test_is_valid_quadratic_equation_form()
    test_convert_to_numbers()
    test_compute()


def test_is_valid_quadratic_equation_form():
    assert is_valid_quadratic_equation_form("x^2+3x+5") == ("", "+3", "+5")
    assert is_valid_quadratic_equation_form("x^2+3x+5=0") == ("", "+3", "+5")
    assert is_valid_quadratic_equation_form("2x^2+3x+5") == ("2", "+3", "+5")
    assert is_valid_quadratic_equation_form("2x^2+3x+5=0") == ("2", "+3", "+5")
    assert is_valid_quadratic_equation_form("x^2+3x") == ("", "+3", None)
    assert is_valid_quadratic_equation_form("x^2+3x=0") == ("", "+3", None)
    assert is_valid_quadratic_equation_form("2x^2+3x") == ("2", "+3", None)
    assert is_valid_quadratic_equation_form("2x^2+3x=0") == ("2", "+3", None)
    with pytest.raises(InputError):
        is_valid_quadratic_equation_form("x+3x+5")
    with pytest.raises(InputError):
        is_valid_quadratic_equation_form("x^2+3+5")
    with pytest.raises(InputError):
        is_valid_quadratic_equation_form("2x+3x+5")
    with pytest.raises(InputError):
        is_valid_quadratic_equation_form("3x^2+3x+5=1")
    with pytest.raises(InputError):
        is_valid_quadratic_equation_form("Hello World!")
    with pytest.raises(InputError):
        is_valid_quadratic_equation_form("")


def test_convert_to_numbers():
    assert convert_to_numbers(("", "+3", "+5")) == (1, 3, 5)
    assert convert_to_numbers(("-", "+3", "+5")) == (-1, 3, 5)
    assert convert_to_numbers(("", "-", "+5")) == (1, -1, 5)
    assert convert_to_numbers(("3", "+3", "+5")) == (3, 3, 5)
    assert convert_to_numbers(("", "+3", None)) == (1, 3, 0)
    assert convert_to_numbers(("2", "+3", None)) == (2, 3, 0)
    with pytest.raises(ValueError):
        convert_to_numbers(("0", "+3", "+5"))
    with pytest.raises(ValueError):
        convert_to_numbers(("+0", "+3", "+5"))
    with pytest.raises(ValueError):
        convert_to_numbers(("-0", "+3", "+5"))
    with pytest.raises(ValueError):
        convert_to_numbers(("0", "+3", None))


def test_compute():
    assert compute((2, 3, 0)) == ((-1.5+0j), 0j, 'There are two distinct real roots.')
    assert compute((1, -1, 5)) == ((0.5-2.179449471770337j), (0.5+2.179449471770337j), 'There are two complex conjugate roots.')
    assert compute((1, -6, 9)) == ((3+0j), (3+0j), 'There is a single repeated real root.')


if __name__ == '__main__':
    main()
