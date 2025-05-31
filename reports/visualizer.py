import matplotlib.pyplot as plt
import numpy as np

def plot_ddt(ddt: np.ndarray, title="Difference Distribution Table"):
    plt.figure(figsize=(6, 5))
    plt.imshow(ddt, cmap='Blues', interpolation='nearest')
    plt.title(title)
    plt.xlabel("Output Difference")
    plt.ylabel("Input Difference")
    plt.colorbar()
    plt.show()

def plot_lat(lat: np.ndarray, title="Linear Approximation Table"):
    plt.figure(figsize=(6, 5))
    plt.imshow(np.abs(lat), cmap='hot', interpolation='nearest')
    plt.title(title)
    plt.xlabel("Output Mask")
    plt.ylabel("Input Mask")
    plt.colorbar(label="Bias")
    plt.show()

def plot_equations(equations):
    print("Symbolic equations:")
    for eq in equations:
        print(eq)

