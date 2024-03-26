import math
from Implicit_ODE_Solver import Euler
from typing import Callable
import matplotlib.pyplot as plt

# Function definition
def f(y, t):
    return -y

# Define initial conditions, start time, stop time, and step size
y0 = 1  # Initial condition
t0 = 0  # Start time
tf = 16  # Stop time
dt = 0.01  # Step size

# Create an object of the Euler class
solver = Euler(f, y0, t0, tf, dt=dt)

# Solving numerically
t_values, y_values = solver.solve()

y_analytic = [math.exp(-t) for t in t_values]

# Plot the numerical solution
plt.plot(t_values, y_values, label='Numerical solution')
plt.plot(t_values, y_analytic, label='Analytical solution')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Numerical vs Analytical Solution of function')
plt.legend()
plt.grid(True)
plt.show()


