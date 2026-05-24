from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
app = Dash(__name__)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
df = pd.read_csv('sysinfo.csv')
# print(df)
# fig = px.scatter(df, x="mon_time" , y="mem_percent",title="tu",
#
#
#                  log_x=True, size_max=60)
fig = make_subplots(specs=[[{"secondary_y": True}]])

fig.a
# Add traces
fig.add_trace(
    go.Scatter(x=df["mon_time"] , y=df["cpu_percent"], name="CPU"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=df["mon_time"] , y=df["mem_percent"], name="内存"),

    secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="Double Y Axis Example"
)

# Set x-axis title
fig.update_xaxes(title_text="检测时间")

# Set y-axes titles
fig.update_yaxes(title_text="<b>CPU占用百分比</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>内存占用百分比</b>", secondary_y=True)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)