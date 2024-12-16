
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_data(
    pplot: dict,
    title: str,
    ylabel: str = None,
    ylabel2: str = None,
    barnorm: bool = False,
    barmode: str = "stack",
    y_max_limit: float = None,
    annotation: dict = {},
):
    """Generical function used to plot data in the Plotly.

        Parameters
        ----------
        pplot : dict 
            Dictionary containing the data.
        title : str
            Plot title.
        ylabel : str
            y label in the left side of the plot
        ylable2 : str
            y label in the right side of the plot (secondary axis)
        barnorm : bool
            Normalize the axis number or not
        barmode : str
            Possible values stack, group, relative
        y_max_limit : float
            Max limit number in y axis
        annotation : dict
            Show texts inside the plot.
            {
                'note1' : {
                    'text': 'note to be showed',
                    'x': 0,
                    'y': 0,
                }
            }

        Returns
        -------
        pplot : dict
            Dictionary with transformed data ready to be used in plot_data function.
    """
    only_line = True
    stplotly = Stplotly(title)

    for p in pplot.keys():
        x = pplot["x"]
        if "y" in pplot[p]:
            y = pplot[p]["y"]

            if "percent" in pplot[p] and pplot[p]["percent"]:
                formt = "%{text:.0%}"
            else:
                formt = "%{text:.3s}"

        secondary_y = False
        if "secondary" in pplot[p]:
            secondary_y = pplot[p]["secondary"]

        if "points" in p:
            stplotly.add_trace(
                stplotly.get_points(x, y, pplot[p]["name"]), secondary_y=secondary_y
            )
        elif "line" in p:
            stplotly.add_trace(
                stplotly.get_line(x, y, pplot[p]["name"], formt), secondary_y=secondary_y
            )
        elif "bar" in p:
            stplotly.add_trace(stplotly.get_bar(x, y, pplot[p]["name"], formt))
            only_line = False
        elif "pie" in p:
            stplotly.add_trace(stplotly.get_pie(x, y))
            only_line = False
        elif "funnel" in p:
            stplotly.add_trace(stplotly.get_funnel(x, y, pplot[p]["name"]))
            only_line = False
        elif "histogram" in p:
            stplotly.add_trace(stplotly.get_histogram(x, y, pplot[p]["name"]))
            only_line = False

    stplotly.update_layout(ylabel, ylabel2, barnorm, barmode, y_max_limit)

    if only_line:
        stplotly.fig.update_layout(
            xaxis=dict(
                showline=True, linecolor="rgb(153, 204, 255)", linewidth=2,
            ),
        )

    for key in annotation.keys():
        stplotly.fig.add_annotation(
            text=annotation[key]["text"],
            x=annotation[key]["x"], y=annotation[key]["y"],
            showarrow=True, arrowhead=1,
            font=dict(
                size=14, color="white"
            ),
            bgcolor="blue",
        )

    return stplotly.fig


def prepare_multiple_columns_plot(
    df: pd.DataFrame,
    plot_type: str = "bar",
    percent: bool = False,
):
    """Transform a numeric table in the plotly data format. 

        Parameters
        ----------
        df : pd.DataFrame 
            Numeric table.
        plot_type : str
            Possible values: [line, bar]
        percent : bool
            Indicate if the numbers need to be showed in percent or not

        Returns
        -------
        pplot : dict
            Dictionary with transformed data ready to be used in plot_data function.
    """
    pplot = {
        "x": df.index,
    }
    i = 1
    for column in df.columns:
        pplot[plot_type + str(i)] = {
            "y": df[column], "name": column, "percent": percent,
        }
        i += 1

    return pplot


class Stplotly():

    def __init__(self, title):
        self.fig = make_subplots(specs=[[{"secondary_y": True}]])

        self.title = title
        self.secondary_y = False
        self.status_bar = False

    def get_line(self, x, y, name, formt):
        return go.Scatter(
            x=x, y=y, name=name, line_shape="spline",
            text=y, texttemplate=formt, mode="lines+markers+text", textposition="top right",
            textfont=dict(
                size=13, color="Salmon",
            )
        )

    def get_points(self, x, y, name):
        return go.Scatter(
            x=x, y=y, name=name, line_shape="spline"
        )

    def get_bar(self, x, y, name, formt):
        self.status_bar = True
        return go.Bar(
            x=x, y=y, name=name,
            text=y, texttemplate=formt, textposition="outside",
        )

    def get_pie(self, x, y):
        return go.Pie(
            labels=x, values=y, hole=.4, hoverinfo="label+value+percent+name",
        )

    def get_funnel(self, x, y, name):
        return go.Funnel(
            x=x, y=y, name=name, textinfo="value+percent previous",
        )

    def get_histogram(self, y, name):
        return go.Histogram(
            x=y, name=name, textposition="outside",
        )

    def add_trace(self, go_plot, secondary_y=False):
        if secondary_y:
            self.fig.add_trace(go_plot, secondary_y=True)
            self.secondary_y = True
        else:
            self.fig.add_trace(go_plot)

    def update_layout(
        self, ylabel=None, ylabel2=None, barnorm=False, barmode="stack", y_max_limit=None
    ):
        font_size = 13

        self.fig.update_layout(
            title=self.title,
            autosize=True,  # st.plotly_chart(use_container_width=True)
            # width=width, height=height,
            font=dict(
                family="Arial",  # size=20, #color="RebeccaPurple"
            ),
            showlegend=True,
            legend=dict(
                x=1.0, y=1.0, font_size=font_size
            ),
            xaxis=dict(
                showgrid=False, tickfont=dict(size=font_size),
            ),
            yaxis=dict(
                showgrid=False, tickfont=dict(size=font_size),
            ),
            yaxis_title=ylabel,
        )

        if self.status_bar:
            self.fig.update_layout(
                barmode=barmode,
            )

        if self.secondary_y:
            self.fig.update_layout(
                yaxis2=dict(
                    showgrid=False, tickfont=dict(size=font_size)
                ),
                yaxis2_title=ylabel2,
            )

        if barnorm:
            self.fig.update_layout(
                barnorm="percent"
            )

        if y_max_limit is not None:
            self.fig.update_layout(
                yaxis=dict(range=[0, y_max_limit])
            )
