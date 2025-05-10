import numpy as np
import matplotlib.pyplot as plt

# Control points (customize as needed)
P0 = np.array([0, 0])
P1 = np.array([1, 2])
P2 = np.array([3, 3])
P3 = np.array([4, 0])

def cubic_bezier(t, P0, P1, P2, P3):
    return (1 - t)**3 * P0 + 3 * (1 - t)**2 * t * P1 + 3 * (1 - t) * t**2 * P2 + t**3 * P3

# Generate points on the curve
t_values = np.linspace(0, 1, 100)
bezier_points = np.array([cubic_bezier(t, P0, P1, P2, P3) for t in t_values])

# Plotting
plt.plot(bezier_points[:, 0], bezier_points[:, 1], label='Cubic Bézier Curve')
plt.plot([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], 'ro--', label='Control Points')
plt.title("Cubic Bézier Curve")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
