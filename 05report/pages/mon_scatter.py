import dash
from dash import html, dcc
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
dash.register_page(__name__,title='查看散点图')
df = pd.read_csv('sysinfo.csv')
# 生成子图画布对象
fig = make_subplots(specs=[[{"secondary_y": True}]])

# 添加轨迹（图表）
fig.add_trace(
   go.Scatter(x=df["mon_time"] , y=df["cpu_percent"], name="CPU"),
   secondary_y=False,
)
fig.add_trace(
      go.Scatter(x=df["mon_time"] , y=df["mem_percent"], name="内存"),
      secondary_y=True,
)
# 为图表添加标题
fig.update_layout(
   title_text="系统监控数据统计图"
)
# 设置x轴标题
fig.update_xaxes(title_text="监测时间")
# 设置y轴标题
fig.update_yaxes(title_text="<b>CPU使用率</b>", secondary_y=False)
fig.update_yaxes(title_text="<b>内存使用率</b>", secondary_y=True)
layout = html.Div([
   dcc.Graph(
       id='cpu-mem',
       figure=fig
   )
])
