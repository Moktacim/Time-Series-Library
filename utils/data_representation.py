import matplotlib.pyplot as plt 
import os, sys


def save_visualization(data):
    batch_x, batch_y, batch_x_mark, batch_y_mark = data[0]
    import matplotlib.pyplot as plt 

    plt.figure()
    name = os.path.splitext(data.data_path)[0]
    for i in range(batch_x_mark.shape[1]):
        plt.plot(batch_x[:, i])
        plt.plot(batch_y[:, i])
        plt.savefig(os.path.join('plots', f'{name}_data.png'))
    
    plt.figure()
    for i in range(batch_x_mark.shape[1]):
        plt.plot(batch_x_mark[:, i])
        plt.plot(batch_y_mark[:, i])
        plt.savefig(os.path.join('plots', f'{name}_mark.png'))

from pylab import * 
def visual_pos_enc(data):
    """adopted from Scientific Visualization: Python + Matplotlib
    https://raw.githubusercontent.com/rougier/scientific-visualization-book/master/code/rules/rule-5-right.py
    """

    batch_x, batch_y, batch_x_mark, batch_y_mark = data[0]
    figure(figsize=(8, 10), dpi=80)
    subplot(211)
    for i in range(batch_x.shape[1]):
        plot(batch_x[:, i], color="blue", linewidth=1.5, linestyle="-", label=f"$x_{i}$")
        plot(batch_y[:, i], color="red", linewidth=1.5, linestyle="-", label=f"$y_{i}$")

    ax = gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.spines["bottom"].set_position(("data", 0))
    ax.yaxis.set_ticks_position("left")
    ax.spines["left"].set_position(("data", 0))

    xlim(batch_x.min() * 1.1, batch_x.max() * 1.1)
    xticks(
        [0, 10, 20, 30, 40],
        [r"$0$", r"$10$", r"$20$", r"$30$", r"$40$"],
    )

    ylim(batch_y.min() * 1.1, batch_y.max() * 1.1)
    yticks([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, +2], [r"$-2$", r"$-1.5$",
                                                      r"$-1$", r"$-0.5$",
                                                      r"$0$", r"$0.5$",
                                                      r"$1$", r"$1.5$",
                                                      r"$2$"])
    # legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.65))


    subplot(212)
    for i in range(batch_x_mark.shape[1]):
        plot(batch_x_mark[:, i], color="red", linewidth=1.5, linestyle="-", label=f"$mark_{i}$")
        plot(batch_y_mark[:, i], color="red", linewidth=1.5, linestyle="-", label=f"$mark_{i}$")

    ax = gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.xaxis.set_ticks_position("bottom")
    ax.spines["bottom"].set_position(("data", 0))
    ax.yaxis.set_ticks_position("left")
    ax.spines["left"].set_position(("data", 0))

    xlim(batch_x_mark.min() * 1.1, batch_x_mark.max() * 1.1)
    xticks(
        [0, 10, 20, 30, 40],
        [r"$0$", r"$10$", r"$20$", r"$30$", r"$40$"],
    )

    ylim(batch_y_mark.min() * 1.1, batch_y_mark.max() * 1.1)
    # yticks([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, +2], [r"$-2$", r"$-1.5$",
    #                                                   r"$-1$", r"$-0.5$",
    #                                                   r"$0$", r"$0.5$",
    #                                                   r"$1$", r"$1.5$",
    #                                                   r"$2$"])

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.65))

    savefig(f"plots/{os.path.splitext(data.data_path)[0]}.pdf")