cimport cython
from libc.stdint cimport uint8_t
import numpy as np

# Turn off bounds checking in Cython. Bounds checking is a safety feature
# that prevents you from accessing memory outside of the bounds of an array.
# It's a common feature in many languages to prevent bugs and security issues.
# However, it does add some overhead because the program has to check the
# bounds every time it accesses the array.
@cython.boundscheck(False)
# Disable negative indexing in Cython. Negative indexing is a feature in
# Python where you can access elements from the end of a list or array by
# using negative numbers. For example, array[-1] would give you the last
# element in the array.
@cython.wraparound(False)
def mandelbrot(int width, int height, int max_iter):
    cdef int i, j, n
    cdef double cx, cy, zx, zy, zx_new
    cdef uint8_t[:, :] image = np.zeros((height, width), dtype=np.uint8)

    for i in range(width):
        cx = -2.0 + i * (3.0 / width)
        for j in range(height):
            cy = -1.5 + j * (3.0 / height)
            zx, zy = 0.0, 0.0

            for n in range(max_iter):
                zx_new = zx * zx - zy * zy + cx
                zy = 2.0 * zx * zy + cy
                zx = zx_new

                if zx * zx + zy * zy > 4.0:
                    break

            image[j, i] = <uint8_t>(n * 255 / max_iter)

    return np.asarray(image)