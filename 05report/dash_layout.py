# 导入所需的库，每个库都为应用程序提供了一个构建模块
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# 创建Dash类的实例，以初始化应用程序
app = Dash(__name__)
# 预设样式（字典形式）
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
# 定义数据来源，DataFrame是一个表格型的数据结构
df = pd.DataFrame({
    "服务器": ["A01", "A02", " A03", "B01", "B02", "B03"],
    "得分": [95, 78, 92, 82, 66, 88],
    "部门": ["信息部", "信息部", "信息部", "业务部", "业务部", "业务部"]
})
# 绘制柱状图
fig = px.bar(df, x="服务器", y="得分", color="部门", barmode="stack")
# 更改柱状图样式
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
# app对象的layout属性使用由Dash组件组成的树结构定义应用程序的外观
app.layout = html.Div(
    style={'backgroundColor': colors['background']},  # 全局样式（字典形式）
    children=[
        html.H1(
            children='服务器性能测试',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(children='测试结果报告', style={
            'textAlign': 'center',
            'color': colors['text']
        }),
        # 图形组件
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)  # 运行Dash应用程序
