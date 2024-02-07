# QUADRATIC EQUATION CALCULATOR
#### Video Demo:  https://youtu.be/j1TJ9pYBgaU
#### Description:
## Overview
This project is a Python program that serves as a calculator for solving quadratic equations. The calculator takes an input quadratic equation in standard form (ax^2 + bx + c = 0), where 'a', 'b', and 'c' are coefficients, and provides the solutions for 'x' based on the quadratic formula. The solutions can be real or complex, and the program determines the nature of the roots. The other variations of the standard forms that are accepted by the program are: ax^2 + bx = 0, ax^2 + bx + c, and ax^2 + bx; any other formats will be rejected. Also, the program can tolerate any amount of whitespace in the input itself.

## Files and Their Functions

### `project.py`
This file contains the main functionality of the quadratic equation calculator. Here's a breakdown of the key components:

- **`InputError` Exception:** This exception is raised for invalid equation inputs during the execution of the program.

- **`is_valid_quadratic_equation_form(equation)` Function:**
  - Verifies whether the input is a valid quadratic equation according to the standard form.
  - Then it captures the coefficients 'a', 'b', and 'c' from the input equation.

- **`convert_to_numbers(coefficient_strings)` Function:**
  - Converts the captured coefficient strings into numerical values.
  - Checks and handles specific quadratic equation conditions, such as ensuring 'a' is not zero.

- **`compute(coefficient_numbers)` Function:**
  - Calculates the solutions for the quadratic equation based on the extracted coefficient values.
  - Determines the nature of the roots (real, repeated real, or complex conjugate).

- **`main()` Function:**
  - Takes user input for a quadratic equation.
  - Processes the input, performs the calculations, and prints the solutions along with a conclusion about the nature of the roots.

### `test_project.py`
This file contains unit tests using the `pytest` framework to ensure the correctness of the functions in `project.py`. The tests cover various cases for input validation, conversion of coefficients, and computation of solutions.

## Design Choices
1. **Regular Expressions:**
   - Regular expressions are used to validate the input quadratic equation and extract coefficients. This allows for a flexible and concise way to handle various input formats.

2. **Complex Number Support:**
   - The program uses the `cmath` module to handle complex numbers, ensuring accurate solutions for quadratic equations with complex roots.

3. **Error Handling:**
   - Custom exceptions (`InputError`) are employed to provide meaningful error messages in case of invalid equation input or specific conditions not met.

4. **Readability and User Interaction:**
   - The code uses f-strings for formatting output, making the results easy to read. User prompts and informative messages are included for a user-friendly experience.

## How to Use
1. Run the program using `python project.py`.
2. Enter a quadratic equation in standard form as prompted.
3. The program will display the solutions for 'x' and a conclusion about the nature of the roots.

## Testing
To run the provided unit tests, execute `python test_project.py`. The tests cover a range of valid and invalid inputs to ensure the robustness and correctness of the calculator.

Feel free to explore and modify the code for further enhancements or integration into other projects. Enjoy using the Quadratic Equation Calculator!
