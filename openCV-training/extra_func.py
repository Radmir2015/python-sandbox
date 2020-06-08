from math import ceil
from itertools import zip_longest

from matplotlib import pyplot as plt


def draw_images(images, titles=[], amount=(1, 2), ticks=True, **imshow_args):
    y_amount = ceil(len(images) / sum(amount))
    x_amount = ceil(len(images) / y_amount)

    if amount[0] > amount[1]:
        y_amount, x_amount = x_amount, y_amount

    for im, t, inx in zip_longest(images, titles, range(len(images))):
        plt.subplot(y_amount, x_amount, inx + 1)
        plt.imshow(im, **imshow_args)

        if titles:
            plt.title(t)

        if ticks:
            plt.xticks([]), plt.yticks([])

    plt.show()
