import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv("dados.csv")

fig = px.bar(df, x="DT_MEDICAO", y="UMD_INS", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Umidade'),

    html.Div(children='''
        umidade do ar
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
