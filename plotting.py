import numpy as np
import matplotlib.pyplot as plt
from drill_objects import DrillShape, DrillSet


def plot_shape(shape: DrillShape):
    fig, ax = plt.subplots()
    ax.set_xlim(-80, 80)
    ax.set_ylim(0, 84)

    ax.set_xticks(range(-80, 81, 4))
    ax.set_yticks(range(0, 85, 4))

    ax.set_xlabel('Steps left/right')
    ax.set_ylabel('Steps front/back')

    ax.grid()

    xs = [p.horizontal for p in shape.positions]
    ys = [p.vertical for p in shape.positions]

    ax.scatter(xs, ys, s=5, color='black')
    for x, y, p in zip(xs, ys, shape.performers):
        ax.text(x, y, p[0], va='center', ha='center', size=15)
        ax.text(x, y, p[1:], va='top', ha='center', size=10)
    plt.show()

    return ax


def plot_set(dset: DrillSet):
    fig, ax = plt.subplots()
    ax.set_xlim(-80, 80)
    ax.set_ylim(0, 84)

    ax.set_xticks(range(-80, 81, 4))
    ax.set_yticks(range(0, 85, 4))

    ax.set_xlabel('Steps left/right')
    ax.set_ylabel('Steps front/back')

    ax.grid()
    for shape in dset.shapes:
        xs = [pos.horizontal for pos in shape.positions]
        ys = [pos.vertical for pos in shape.positions]

        ax.scatter(xs, ys, s=5, color='black')
        for x, y, p in zip(xs, ys, shape.performers):
            ax.text(x, y, p[0], va='center', ha='center', size=15)
            ax.text(x, y, p[1:], va='top', ha='center', size=10)

    plt.show()

    return ax
