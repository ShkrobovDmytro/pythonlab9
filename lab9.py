import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np

x_points = [0.7, 0.8, 1.2, 1.5, 1.7]
y = [4.54, 6.14, 5.43, 3.72, 4.18]
spl = UnivariateSpline(x_points, y)  # Побудова сплайна
xs = np.linspace(0.7, 1.7, 100)
plt.plot(x_points, y, 'ro', xs, spl(xs), 'g')
plt.show()

