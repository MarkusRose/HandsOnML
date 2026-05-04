from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
from matplotlib import colormaps
list(colormaps)


(train_X, train_y), (test_X, test_y) = mnist.load_data()

plt.imshow(train_X[0], cmap='grey')
plt.show()

