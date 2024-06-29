import matplotlib.pyplot as plt
import numpy.typing as npt
import numpy as np
import matplotlib.axes as mpla
import matplotlib.figure as mplf

class MinimalBoxPlot(object):
    """Create a minimal boxplot a la Tufte (2001) p. 125

    The "box" extends from the first quartile (Q1) to the third
    quartile (Q3) of the data, with a dot at the median.
    The whiskers extend from the box to the farthest data point
    lying within 1.5x the inter-quartile range (IQR) from the box.
    The plot maximizes the data to ink ratio.

    .. code-block:: none

        |   Q1-1.5IQR 
        |
        |
        |
        |   Q1


        .   median

        |   Q3
        |
        |
        |    Q3+1.5IQR


    Methods
    -------
    minimal: creates boxplot using similar syntax to original matplotlib implementation

    to_minimal: converts existing boxplot to minimal boxplot

    """


    def minimal(ax:mpla.Axes, x: npt.ArrayLike, positions: npt.ArrayLike, width:np.float64, color:str='k', lw:np.float64=1.5):
        """
        Parameters
        ----------
        ax: plt.axes._axes.Axes

        x: np.typing.ArrayLike

        positions: np.typing.ArrayLike

        width: np.float64

        color: str
        
        """
        # get statistics
        medians = np.median(x, axis=0)
        q1 = np.percentile(x, 25, axis=0)
        q3 = np.percentile(x, 75, axis=0)
        iqr = q3 - q1
        lower_whiskers = q1 - 1.5 * iqr
        upper_whiskers = q3 + 1.5 * iqr

        for i, pos in enumerate(positions):

        # plot the quartile boxes
            ax.add_patch(plt.Rectangle((pos - width/2, q1[i]), width, q3[i] - q1[i], color='white', alpha=0.5))
            
            # plot the whiskers
            ax.plot([pos, pos], [lower_whiskers[i], q1[i]], color=color, lw=lw)
            ax.plot([pos, pos], [q3[i], upper_whiskers[i]], color=color, lw=lw)
            
            # plot the median as a dot
            ax.plot(pos, medians[i], 'o', color=color)

        # adjust x-axis
        ax.set(xticks=positions)

    def to_minimal(figure:mplf.Figure, BP):
        """
        Parameters
        ----------
        figure: plt.figure.Figure

        BP: dict
            Dictionary output returned from original plot generation
            See https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html
        """

        # get current acis
        ax = figure.gca()

        # remove unnecessary elements
        for _, box in enumerate(BP["boxes"]):
            box.set_visible(False)
        for _, cap in enumerate(BP["caps"]):
            cap.set_visible(False)

        # get some data
        x_vals = []
        y_vals = []
        for i, m in enumerate(BP["medians"]):

            x = m.get_xdata()
            if x[0] in x_vals:
                continue
            else:
                x_vals.append(x[0])
            y = m.get_ydata()
            if y[0] in y_vals:
                continue
            else:
                y_vals.append(y[0])

            m.set_visible(False)

        # additional info
        positions = np.add(x_vals, 0.75) # for some reason, x positions are offset by 0.75 units
        color = BP["whiskers"][0].get_color()
        ax.set(xticks=positions)

        # plot new medians
        ax.scatter(positions, y_vals, marker='o', color=color)

        return mplf.Figure
