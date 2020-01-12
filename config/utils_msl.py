import matplotlib.pyplot as plt
import random
import numpy as np
from sklearn.preprocessing import LabelBinarizer

def plot_examples(X, y, ix_to_char):
    f = plt.figure(figsize=(25, 10))
    i = 0
    while i < len(ix_to_char):
        idx, label = random.choice(list(enumerate(y)))
        if i == label:
            plot = f.add_subplot(4, 6, i+1)
            plot.axis('Off')
            plot.set_title(f"Sign: {ix_to_char[i]}")
            plot.imshow(X[idx], cmap='gray')
            i += 1

        elif i == 9:
            plot = f.add_subplot(4, 6, i + 1)
            plot.axis('Off')
            plot.set_title(f"Sign {ix_to_char[i]} is missing")
            plot.imshow(np.zeros((28, 28)), cmap='gray')
            i += 1

