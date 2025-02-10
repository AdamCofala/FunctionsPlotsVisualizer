# Polynomial and Function Plotter

This Python script allows users to visualize different types of mathematical functions using the Turtle graphics module.

## Features
- **Polynomial functions**: Plots polynomial functions based on user input.
- **Homographic functions**: Plots rational functions with a given denominator polynomial.
- **Square root functions**: Plots functions of the form \( y = b \sqrt{P(x)} \).
- **Graphical interface**: Uses Turtle to display a coordinate system and function plots.

## Requirements
- Python 3.x
- Turtle module (included with standard Python installation)

## How to Use
1. Run the script.
2. Choose the type of function you want to plot:
   - `1` for polynomial functions
   - `2` for homographic functions
   - `3` for square root functions
   - `4` to exit
3. Enter the coefficients of the polynomial from the highest to the lowest degree.
4. The function graph will be drawn in the Turtle window.
5. After plotting, you can select another function type or exit.

## Controls
- The graph window can be closed manually.
- After each function plot, the terminal prompts for the next action.

## Example Usage
```sh
python GraphicCalc.py
```

### Sample Polynomial Input
If the user chooses option `1` (polynomial function):
```
Stopien wielomianu: 2
a2=3
a1=4
a0=5
```
This represents the function: \( y = 3x^2 + 4x + 5 \).

## Notes
- The coordinate system is scaled for better visualization.
- The screen clears after each function plot.
- The script runs in a loop until the user chooses to exit.

## License
This project is open-source and available under the MIT License.
