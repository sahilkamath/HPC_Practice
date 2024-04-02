import math
from typing import Callable

import matplotlib.pyplot as plt

from cython_ODE_solver import Euler


# Function definition
def f(y, t):
    return -y


# Define initial conditions, start time, stop time, and step size
y0 = 1  # Initial condition
t0 = 0  # Start time
tf = 16  # Stop time
n_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dt_values = [16 / (2**n) for n in n_values]  # List of step sizes
err = []  # List to store error values

for dt in dt_values:

    # Create an object of the Euler class
    solver = Euler(f, y0, t0, tf, dt=dt)

    # Solving numerically
    t_values, y_values = solver.solve()

    y_analytic = [math.exp(-t) for t in t_values]

    # Plot the numerical solution, Comment this if required
    # plt.plot(t_values, y_values, label='Numerical solution')
    # plt.plot(t_values, y_analytic, label='Analytical solution')
    # plt.xlabel('t')
    # plt.ylabel('y')
    # plt.title('Numerical vs Analytical Solution of function')
    # plt.legend()
    # plt.grid(True)
    # plt.show()

    err.append(y_values[-1] - y_analytic[-1])

# Plot the error vs step size, Comment this if required
plt.plot(err, dt_values)
plt.gca().invert_xaxis()
plt.xlabel("Time Step Values")
plt.ylabel("Error")
plt.title("Error between numerical and analytical solution vs Time step")
plt.grid(True)
plt.show()
