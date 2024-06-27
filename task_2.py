import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Define the function to be integrated
def f(x):
    return x ** 2

# Define the integration boundaries
a = 0  # Lower bound
b = 2  # Upper bound

# Plot the function and shaded area
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Graph of integration of f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()

# Monte Carlo Integration
N = 10000  # Number of random points
random_x = np.random.uniform(a, b, N)
function_values = f(random_x)
monte_carlo_integral = (b - a) * np.mean(function_values)
print("Monte Carlo Integral:", monte_carlo_integral)

# Verification using quad function
result, error = spi.quad(f, a, b)
print("Quad Integral:", result)
print("Error Estimate:", error)
