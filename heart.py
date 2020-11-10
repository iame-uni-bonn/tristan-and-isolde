import matplotlib.pyplot as plt
import numpy as np


def plot_heart():
    fig = plt.figure()

    x = np.linspace(-2, 2, 1000)
    y1 = np.sqrt(1 - (abs(x) - 1) ** 2)
    y2 = -3 * np.sqrt(1 - (abs(x) / 2) ** 0.5)

    plt.fill_between(x, y1, color="red")
    plt.fill_between(x, y2, color="red")
    plt.xlim([-2.5, 2.5])
    plt.text(
        0,
        -0.4,
        "1solde",
        fontsize=24,
        fontweight="bold",
        color="white",
        horizontalalignment="center",
    )
    plt.axis("off")

    return fig


if __name__ == "__main__":
    heart_fig = plot_heart()
    heart_fig.show()
