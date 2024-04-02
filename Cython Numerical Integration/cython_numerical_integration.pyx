# cython: language_level=3
cimport cython
from libc.stdlib cimport RAND_MAX, rand
import numpy as np

@cython.boundscheck(False)  # Disable bounds checking for performance
@cython.wraparound(False)  # Disable negative indexing for performance

# %%
def J0(x, N=100, method='trapz'):
    if method == 'trapz':
        return J0_trapz(x,N)
    elif method == 'simps':
        return J0_simps(x,N)
    else:
        raise ValueError('Invalid method')

def J0_trapz(x, N):
    sum = 0
    a = 0
    b = np.pi
    h = (b-a)/N
    for n in range(N-1):
        sum += (( np.cos(x*np.sin(n*h)) + np.cos(x*np.sin((n+1)*h)) )*h)/2
    sum = sum/np.pi
    return sum

def J0_simps(x, N):
    sum = 0
    a = 0
    b = np.pi
    h = (b-a)/N
    for n in range(N-1):
        sum += (( np.cos(x*np.sin(n*h)) + 4*np.cos(x*np.sin((n+0.5)*h)) + np.cos(x*np.sin((n+1)*h)) )*h)/6
    sum = sum/np.pi
    return sum



