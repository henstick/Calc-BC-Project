from sympy import symbols, diff, solve, sympify

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
