import dash
from dash import html
import pandas as pd
dash.register_page(__name__, title='显示表格',path='/')
# 指定数据来源
df = pd.read_csv('sysinfo.csv')
# 定义生成Web表格的函数
def generate_table(dataframe,max_rows=10):
   return html.Table([
       html.Thead(                                   # 表头
          html.Tr([html.Th(col) for col in dataframe.columns])
       ),
       html.Tbody([                                  # 表体
          html.Tr([
             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
          ]) for i in range(min(len(dataframe), max_rows))
       ])
   ])
# 布局定义
layout = html.Div([
   html.H4(children='系统监控数据表格'),
   generate_table(df)                 # 重用组件
])
