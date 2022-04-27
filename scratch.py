arcpy.MakeFeatureLayer_management(r"C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch/al_tuscaloosa.gpkg/al_tuscaloosa.gpkg/main.al_tuscaloosa", "main.al_tuscaloosa")
arcpy.management.AddJoin("main.al_tuscaloosa", "ogc_fid", "zs", "ogc_fid", "KEEP_ALL")
arcpy.management.SelectLayerByAttribute("main.al_tuscaloosa", "NEW_SELECTION", "zs:MAJORITY IS NULL", None)
arcpy.env.workspace = "C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch"
arcpy.FeatureToPoint_management("main.al_tuscaloosa", "parcels_center.shp", 
                                "INSIDE")
###################################
import dash
from dash import dcc
from dash import html
import pandas as pd
 
# initialisation and manipulation of data
data = pd.read_csv("covid1.csv")
data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%d-%m-%Y')
app = dash.Dash(__name__)
 
# Initialising the application.
app.layout=html.Div(
    children=[
        html.H1(children="Covid cases and recovery",),
        html.P(
            children="First wave of covid",
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
        dcc.Graph(
            figure={
                "data":[
                    {
                        "x":data["Date"],
                        "y":data["Low"],
                        "type":"lines",
                    },
                ],
                "layout": {"title": "Day-wise lowest prices of index"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Close"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Day-wise closing prices of index"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Open"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Day-wise opening prices of index"},
            },
        ),
] )
 
# deploying server
if __name__ == "__main__":
    app.run_server(debug=True)
