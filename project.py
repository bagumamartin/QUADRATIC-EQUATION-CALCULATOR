import re
import cmath

# Custom error implentation idea: https://ioflood.com/blog/python-throw-exception/#:~:text=Throwing%20exceptions%20in%20Python%20can,from%20the%20base%20Exception%20class.
class InputError(Exception):
    pass


def main():
    equation = input("Enter a quadratic equation according to standard format (ax^2+bx+c=0) in that order, the '=0' can be omitted\nEquation: ")
    try:
        x1, x2, conclusion = compute(convert_to_numbers(is_valid_quadratic_equation_form(equation)))
        # Superscript implementation idea: https://stackoverflow.com/questions/8651361/how-do-you-print-superscript
        formated_equation = re.sub(r"\s*\^2", "\u00b2", re.sub(r"(?:=\s*0\s*)$", "", equation))
        # Subcript implementation idea: https://stackoverflow.com/questions/24391892/printing-subscript-in-python
        output =    f"""
                    The solution for {formated_equation}=0 is

                    x\u2081 = {x1}
                    x\u2082 = {x2}
                    Conclusion: {conclusion}
                    """
    except InputError as error:
        output = error
    except ValueError as error:
        output = error
    print(output)


def is_valid_quadratic_equation_form(equation):
    """
    Verify whether the input is a valid quadratic equation form. Then capture the coefficients and the intercept.
    """

    if coefficients := re.search(r"^\s*([+-]?\s*\d*)\s*x\s*\^2\s*([+-]\s*\d*)\s*x(?:\s*([+-]\s*\d*)\s*)?(?:=\s*0\s*)?$", equation, re.IGNORECASE):
        coefficients = coefficients.group(1), coefficients.group(2), coefficients.group(3)
        return coefficients
    else:
        raise InputError("Invalid equation")


def convert_to_numbers(coefficient_strings):
    """
    Convert the captured strings into numbers. Then verify some quadratic equation conditions.
    """
    a, b, c = coefficient_strings
    if a:
        if a == "-":
            a = -1
        a = int(a)
    else:
        a = 1
    if a == 0:
        raise ValueError('The a coefficient cannot be 0')
    if b:
        if b == "-":
            b = -1
        b = int(b)

    if c:
        c = int(c)
    else:
        c = 0

    return a, b, c


def compute(coefficient_numbers):
    """
    Calculate the solution according to the extracted coefficient values
    """
    # Idea implementaion inspiration: https://www.programiz.com/python-programming/examples/quadratic-roots
    a, b, c = coefficient_numbers
    discriminant = (b**2) - (4*a*c)
    first_value = (-b-cmath.sqrt(discriminant))/(2*a)
    second_value = (-b+cmath.sqrt(discriminant))/(2*a)

    if discriminant > 0: deduction = "There are two distinct real roots."
    elif discriminant == 0: deduction = "There is a single repeated real root."
    else: deduction = "There are two complex conjugate roots."

    return first_value, second_value, deduction



if __name__ == "__main__":
    main()
