# %%
import math
from typing import Callable

import matplotlib.pyplot as plt


# %%
class Euler:
    def __init__(
        self,
        f: Callable[[float, float], float],
        y0: float,
        t0: float,
        tf: float,
        dt=None,
        N=None,
    ):
        """
        Initialize the Euler solver.

        Parameters:
        - f: The function representing dy/dt = f(y, t)
        - y0: Initial condition
        - t0: Initial time
        - tf: Final time
        - dt: Time step size
        - N: Number of steps (alternative to dt)
        """
        self.f = f
        self.y0 = y0
        self.t0 = t0
        self.tf = tf
        self.dt = dt
        self.N = N

        if tf < t0:
            raise ValueError("Stop time should be greater than Start time")
        if dt is None and N is None:
            raise ValueError("Either dt or N must be specified")
        if dt is not None and N is not None:
            raise ValueError("Only one of dt or N should be specified")

        if dt is not None:
            self.N = int((tf - t0) / dt)
        else:
            self.dt = (tf - t0) / N

    def solve(self):
        """
        Solve the ODE using the Euler method.

        Returns:
        - t_values: Array of t values
        - y_values: Array of corresponding solution values

        Example:
        def f(y,t):
            return ty
        solver = Euler(f, 1, 0, 2, 0.1)
        x,y = solver.solve()
        """
        t_values = [self.t0]
        y_values = [self.y0]

        t = self.t0
        y = self.y0

        for _ in range(self.N):
            y = y + self.dt * self.f(y, t)
            t = t + self.dt
            t_values.append(t)
            y_values.append(y)

        return t_values, y_values
