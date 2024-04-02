# %%
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import normalize
import scipy
import matplotlib.pyplot as plt

# %%
th = np.linspace(0, np.pi, 100)
x = np.linspace(0, 10, 10)
plt.figure(figsize=(10,10))
for x in x:
    f = np.cos(x*np.sin(th))
    plt.plot(th,f,label='x = %d' % x)
plt.legend()
plt.title('Bessel Functions')
plt.show()

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

# %%
n_values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
N_values = [10 * 2**n for n in n_values]

trapz_value = []
simps_value = []
trapz_error = []
simps_error = []
true = []

for N in N_values:
    trapz_value.append(J0(3.83171, N, method='trapz'))
    simps_value.append(J0(3.83171, N, method='simps'))
    trapz_error.append( J0(3.83171, N, method='trapz') - scipy.special.j0(3.83171) )
    simps_error.append( J0(3.83171, N, method='simps') - scipy.special.j0(3.83171) )
    true.append(scipy.special.j0(3.83171))

# %%
plt.plot((N_values), (trapz_value), label='Trapezoidal Error')
plt.plot((N_values), (simps_value), label='Simpson Error')
plt.plot((N_values), (true), label='True Value')
plt.title('Value vs N')
plt.xlabel('N')
plt.ylabel('Value')
plt.legend()
plt.show()

# %%
# Convert N_values, trapz_error, and simps_error to logarithmic scale
log_N = np.log10(N_values)
log_trapz_error = np.log10(np.abs(trapz_error))
log_simps_error = np.log10(np.abs(simps_error))

# Reshape the data to fit the linear regression model
X = log_N.reshape(-1, 1)
y_trapz = log_trapz_error.reshape(-1, 1)
y_simps = log_simps_error.reshape(-1, 1)

# Fit linear regression models
reg_trapz = LinearRegression().fit(X, y_trapz)
reg_simps = LinearRegression().fit(X, y_simps)

# Get the slope of the linear regression models
slope_trapz = reg_trapz.coef_[0][0]
slope_simps = reg_simps.coef_[0][0]

plt.plot(np.log10(N_values), np.log10(np.abs(trapz_error)), label='Trapezoidal Error (slope = %.2f)' % slope_trapz)
plt.plot(np.log10(N_values), np.log10(np.abs(simps_error)), label='Simpson Error (slope = %.2f)' % slope_simps)
plt.title('Error vs N')
plt.xlabel('log(N)')
plt.ylabel('log(Error)')
plt.legend()
plt.show()

# %%



