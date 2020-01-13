import matplotlib.pyplot as plt
import random
import numpy as np
from sklearn.preprocessing import LabelBinarizer


def plot_examples(X, df, ix_to_char):
    f = plt.figure(figsize=(25, 10))

    for i in ix_to_char:
        if i == 9 or i == 25:
            continue
        else:
            list_indices = df[df["label"] == i].index.values.tolist()
            idx = random.choice(list_indices)
            plot = f.add_subplot(5, 5, i + 1)
            plot.axis('Off')
            plot.set_title(f"Sign: {ix_to_char[i]}")
            plot.imshow(X[idx], cmap='gray')


