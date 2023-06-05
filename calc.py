import sympy
from sympy import symbols, diff, solve, sympify
import matplotlib.pyplot as plt
import numpy as np

# Get the function and variable from the user
function = sympify(input("Enter the function: "))

variable = input("Enter the variable to optimize with respect to: ")

# Define the symbol
x = symbols(variable)

# Calculate the derivative of the function
derivative = diff(function, x)

# Find the critical points by solving the derivative equation
critical_points = solve(derivative, x)

# Find the values of the function at the critical points
values = [function.subs(x, point) for point in critical_points]

# Find the maximum and minimum values
maximum = max(values)
minimum = min(values)

# Print the results
print("Derivative:", derivative)
print("Critical Points:", critical_points)
print("Function Values at Critical Points:", values)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)

# Specify the range for the plot (e.g., -10 to 10 for x-axis, -5 to 5 for y-axis)
x_range = np.linspace(-5, 5, 400)

# Create a function for numpy from the sympy expression
f_lambdified = sympy.lambdify(x, function, "numpy")

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x_range, f_lambdified(x_range), label=str(function))

# Plot the critical points
for point in critical_points:
    plt.plot(point, function.subs(x, point), 'ro')

plt.xlim([-5, 5])
plt.ylim([-3, 3])
plt.xlabel(variable)
plt.ylabel('f(' + variable + ')')
plt.title('Function and its Critical Points')
plt.legend()
plt.grid(True)
plt.show()



#2*x**2 + 3*x**3