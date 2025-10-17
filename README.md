# Simple GUI Calculator using Tkinter

## Overview
This is a simple graphical user interface (GUI) calculator built using Python's Tkinter library. It supports basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/). The calculator features a clean interface with numeric buttons, operator buttons, a clear button, and a decimal point button.

## Features
- **Basic Operations**: Perform addition, subtraction, multiplication, and division.
- **Error Handling**: Displays "Error" for invalid expressions (e.g., division by zero).
- **Clear Functionality**: Reset the display and expression.
- **Chaining Calculations**: After evaluating, the result can be used for further operations.
- **User-Friendly Interface**: Buttons are uniformly styled with red background and black text on a light green window.

## Requirements
- Python 3.x
- Tkinter (included with standard Python installations)

## How to Run
1. Save the code in a file named `simple_calculator.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the file.
4. Run the command: `python simple_calculator.py`.
5. The calculator window will appear.

## Usage
- Click numeric buttons (0-9) to input numbers.
- Click operator buttons (+, -, *, /) to input operations.
- Click '.' to add a decimal point.
- Click '=' to evaluate the expression.
- Click 'Clear' to reset the calculator.

## Code Explanation
- **Class Structure**: The calculator logic is encapsulated in a `SimpleCalculator` class for better organization.
- **Display**: Uses a `StringVar` linked to an `Entry` widget for input/output.
- **Buttons**: Created dynamically with a helper method `_create_button` for consistency.
- **Expression Handling**: Builds an expression string and evaluates it using `eval()` with basic error catching.
- **Layout**: Uses grid layout for button placement, with adjusted geometry to fit all elements properly.

## Improvements from Original
- Wrapped in a class for modularity and to avoid global variables.
- Adjusted window height to accommodate the decimal button without overlap.
- Added padding to buttons for better spacing.
- Improved error handling to catch all exceptions.
- Allowed result to be used for further calculations (chaining).
- Justified display text to the right for a more natural calculator feel.

## Limitations
- Does not support advanced operations like exponents or parentheses.
- Uses `eval()`, which is simple but not secure for untrusted input (safe here as input is controlled).
- No keyboard input support.
