import numpy as np

class HarmonicSeries:
    """
    A class to calculate the partial sums of the harmonic series.
    """
    
    def ascending_sum(self, N) -> float:
        """
        Calculate the sum of the harmonic series in ascending order.

        Returns:
            float: The sum of the harmonic series.
        """
        ascending_sum = 0
        for n in range(1, N + 1):
            ascending_sum += ((-1) ** (n + 1)) / n
        return ascending_sum

    def descending_sum(self, N) -> float:
        """
        Calculate the sum of the harmonic series in descending order.

        Returns:
            float: The sum of the harmonic series.
        """
        descending_sums = 0
        for n in range(N - 1, 0, -1):
            descending_sums += ((-1) ** (n + 1)) / n
        return descending_sums