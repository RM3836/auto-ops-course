from dash import Dash, html, dcc
import dash
# 声明Dash应用使用Dash页面
app = Dash(__name__, use_pages=True)
server = app.server
app.layout = html.Div([
   html.H1(children='系统监控数据报表',
           style={'textAlign': 'center'}),
   html.Div(children=
   [
       html.Span(
          dcc.Link(
            f"{page['title']} ", href=page["relative_path"]
          )
       )
       for page in dash.page_registry.values()
   ],
       style={
          'textAlign': 'right'}
   ),
# 嵌入Dash页面容器
   dash.page_container
])
# if __name__ == '__main__':
#    app.run_server(debug=True)
