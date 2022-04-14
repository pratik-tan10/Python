import dash
from dash import dcc
from dash import html
import pandas as pd

data = pd.read_csv("myLog.csv")
 
data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%d-%m-%Y')

app = dash.Dash(__name__)
 
app.layout=html.Div(
    children=[
        html.H1(children="Nifty 50 Crash and Recovery",),
        html.P(
            children="Analyzing day wise high and low prices of Nifty50 when first wave of Covid-19 hit.",
        ),
        dcc.Graph(
            figure={
                "data":[
                    {
                        "x":data["Date"],
                        "y":data["High"],
                        "type":"lines",
                    },
                ],
                "layout":{"title":"Day-wise highest prices of index"},
                    },
        ),
]
if __name__ == "__main__":
    app.run_server(debug=True)
