from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H1('性能测试得分：'),
    html.Br(),
    dcc.Dropdown(id='server', options=[{'label': 'A01', 'value': 'A01'},
                                       {'label': 'A02', 'value': 'A02'},
                                       {'label': 'B01', 'value': 'B01'},
                                       {'label': 'B02', 'value': 'B02'}],
                 value='A01'),
    html.P(id='score')
])
score_dict = {'A01': 95, 'A02': 78, 'B01': 82, 'B02': 66}
@app.callback(
    Output(component_id='score', component_property='children'),
    Input(component_id='server', component_property='value')
)
def getScore(server):
    return score_dict[server]


if __name__ == '__main__':
    app.run_server(debug=True)
