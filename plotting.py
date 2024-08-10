import numpy as np
import matplotlib.pyplot as plt
from drill_objects import DrillShape, DrillSet


def plot_shape(shape: DrillShape, ax=None):
    if not ax:
        fig, ax = plt.subplots()
        fig.suptitle('SET!')

        ax.set_xlim(-80, 80)
        ax.set_ylim(0, 84)

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


def plot_set(dset: DrillSet, ax=None):
    performers = dset.get_all_performers()
    xdata = []
    ydata = []

    for shape in dset.shapes:
        for pos in shape.positions:
            xdata += [pos.horizontal]
            ydata += [pos.vertical]

    if ax:
        fig = ax.get_figure()

        ax.cla()
    else:
        fig, ax = plt.subplots()
        fig.suptitle('SET!')

    ax.set_xlim(-80, 80)
    ax.set_ylim(0, 84)

    ax.set_xticks(range(-80, 81, 4))
    ax.set_yticks(range(0, 85, 4))

    ax.set_xticks(range(-80, 81), minor=True)
    ax.set_yticks(range(0, 85), minor=True)

    ax.set_xlabel('Steps left/right')
    ax.set_ylabel('Steps front/back')

    ax.grid(linewidth=.5, which='minor')
    ax.grid(linewidth=1, which='major')

    ax.vlines(range(-80, 81, 8), 0, 84, color='black')
    ax.hlines([0, 28, 56, 83.95], -80, 80, color='black')

    points = ax.scatter(xdata, ydata, s=5, color='black')

    for x, y, p in zip(xdata, ydata, performers):
        ax.text(x, y, p[0], va='center', ha='center', size=15)
        ax.text(x, y, p[1:], va='top', ha='center', size=10)

    fig.canvas.draw()
    fig.canvas.flush_events()

    return fig, ax, points

