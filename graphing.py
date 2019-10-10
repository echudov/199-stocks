import matplotlib as matplotlib
import plotly.graph_objects as go
import numpy as np
import static


def dual_bar_chart(index_name, r_streaks, sim_streaks):
    labels = []
    simulated_streaks = sim_streaks[1:].copy()
    real_streaks = r_streaks[1:].copy()
    for i in range(len(real_streaks)):
        real_streaks[i] = int(real_streaks[i])
    while len(simulated_streaks) > len(real_streaks):
        real_streaks.append(0)
    while len(real_streaks) < len(simulated_streaks):
        simulated_streaks.append(0)

    for i in range(2, len(simulated_streaks) + 1):
        labels.append(i)

    fig = go.Figure(data=[
        go.Bar(name='Simulation', x=labels, y=simulated_streaks),
        go.Bar(name='Empirical', x=labels, y=real_streaks)
    ])

    fig.update_layout(
        barmode='group',
        title=go.layout.Title(
            text=index_name,
            font=dict(
                family="Courier New, monospace",
                size=24,
                color="#7f7f7f"
            )
        ),
        xaxis=go.layout.XAxis(
            title=go.layout.xaxis.Title(
                text="Length of Streak",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#7f7f7f"
                )
            )
        ),
        yaxis=go.layout.YAxis(
            title=go.layout.yaxis.Title(
                text="Quantity of Streaks",
                font=dict(
                    family="Courier New, monospace",
                    size=18,
                    color="#7f7f7f"
                )
            )
        )
    )

    fig.show()




