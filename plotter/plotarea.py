# from __future__ import division
import pandas as pd
# import seaborn as sns
# import numpy as np
from bokeh.charts import Area
from bokeh.plotting import output_file, show

# sns.set_palette('dark')

# orange, green, blue, yellow
# colors = ["#F38C17", "#67BA67", "#92B1CA", "#F5E254"]


def plot(concdf, outputfile="test.html"):
    # divide by 60 for time
    # get x val to be time
    # data = concdf.set_index(['Times'])
    # data = concdf
    # area = Area(data, legend='top_right',
    #             title="Plasma Concentration over Time",
    #             xlabel="Time", ylabel="Concentration", color=colors)
    # newtime = concdf
    # newtime["Times"] = map(lambda x: x/60, concdf["Times"])

    data = pd.melt(concdf, id_vars="Times")

    area = Area(data, x="Times", y="value", legend='top_right',
                title="Plasma Concentration over Time",
                xlabel="Hour", ylabel="Concentration", color="variable")
    output_file(outputfile, title="Concentraion Plot")
    show(area)
    return


def plot_stacked(concdf, outputfile="test.html"):
    # divide by 60 for time
    # get x val to be time
    data = concdf.set_index(['Times'])
    area = Area(data, legend='top_right', stack=True,
                title="Plasma Concentration over Time",
                xlabel="Time", ylabel="Concentration")
    output_file(outputfile, title="Concentraion Plot")
    show(area)
    return
