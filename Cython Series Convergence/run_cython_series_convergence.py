import numpy as np
from cython_harmonic_series import HarmonicSeries
import matplotlib.pyplot as plt

# Create an instance of HarmonicSeries
harmonic_series = HarmonicSeries()

# Define the range of N values
N_range = [2 ** n for n in range(9)]  # N = {1, 2, 4, 8, ..., 256}

# Create empty lists to store values
ascending_sums = []
descending_sums = []

for N in N_range:
    ascending_sums.append(harmonic_series.ascending_sum(N))
    descending_sums.append(harmonic_series.descending_sum(N))
asc_err = np.abs(ascending_sums - np.log(2))
des_err = np.abs(descending_sums - np.log(2))

plt.plot(np.log(N_range), np.log(asc_err), label="Ascending")
plt.plot(np.log(N_range), np.log(des_err), label="Descending")
plt.xlabel("N values")
plt.ylabel("Error")
plt.title("Error between ascending and descending convergence")
plt.legend()
plt.grid(True)
plt.show()





