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
    minimal: creates boxplot using similar syntax to original matplotlib

    tominimal: converts existing boxplot to minimal

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

    def tominimal(figure:mplf.Figure):

        # get axes
        ax = figure.gca()
        
        return ax.figure
