# Khalig

Projeto voltado para a análise de dados, dando ênfase, no ínicio, para leituras de dados metereológicos.

<div align="center">
<img src="https://user-images.githubusercontent.com/93950853/140828507-f2764517-2752-4580-8dbd-7ef7852b44f3.png" width="700px" />
</div>

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


### Projeto feito por:

* André Vinicius
* Gabriel Xavier
* Hayla Almeida
* Kevin Lucas
* Lyanh Vinícios
