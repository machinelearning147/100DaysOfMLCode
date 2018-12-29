import numpy as np
import matplotlib.pyplot as plt


def plot_vector2d(vector2d, origin=[0, 0], **options):
    """
    plot a vector as arrow from origin to the given vector2d
    Args: vector2d
    returns: arrow plot
    """
    return plt.arrow(origin[0], origin[1], vector2d[0], vector2d[1],
              head_width=0.2, head_length=0.3, length_includes_head=True,
              **options)

