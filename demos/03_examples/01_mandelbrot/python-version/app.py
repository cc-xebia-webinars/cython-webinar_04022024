import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(width: int, height: int, max_iter: int) -> np.array:
    image = np.zeros((height, width), dtype=np.uint8)

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

            image[j, i] = n * 255 // max_iter

    return image


width, height = 800, 600
max_iter = 100

image = mandelbrot(width, height, max_iter)

plt.imshow(image, cmap="hot")
plt.axis("off")
plt.savefig("mandelbrot.png", bbox_inches="tight")
