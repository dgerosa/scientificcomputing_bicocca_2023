"""functions for generating the Mandelbrot set"""

import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(nx, xmin=-2.0, xmax=2.0, ymin=-2.0, ymax=2.0, max_iter=10):
    """create a mandlebrot set with a resolution
    nxxnx"""

    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymin, ymax, nx)

    xv, yv = np.meshgrid(x, y, indexing="ij")

    c = xv + 1j * yv

    z = np.zeros((nx, nx), dtype=np.complex128)

    m = np.zeros((nx, nx), dtype=int)

    for i in range(max_iter):
        z = z**2 + c

        m[np.logical_and(np.abs(z) > 2, m == 0)] = i

    fig, ax = plt.subplots()
    fig.set_size_inches = (8, 8)
    im = ax.imshow(np.transpose(m), origin="lower",
                   extent=[xmin, xmax, ymin, ymax])

    fig.colorbar(im, ax=ax)

    return fig
