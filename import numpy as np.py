import numpy as np
import matplotlib.pyplot as plt

# Define the logistic function
def f(x):
    return 1 / (1 + np.exp(-x))

# Generate x values
x = np.linspace(-10, 10, 400)

# Compute f(x) values
y = f(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r'$f(x) = \frac{1}{1 + e^{-x}}$', color='blue')
plt.title('Logistic Function Curve')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

# Show the plot
plt.show()