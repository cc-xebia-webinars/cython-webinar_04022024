import matplotlib.pyplot as plt
from mandelbrot import mandelbrot

width, height = 800, 600
max_iter = 100

image = mandelbrot(width, height, max_iter)

plt.imshow(image, cmap="hot")
plt.axis("off")
plt.savefig("mandelbrot.png", bbox_inches="tight")
