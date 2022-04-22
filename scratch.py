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
 
from PIL import Image 
# your loop here
img = Image.open('img.png') 
img = img.convert("RGBA") 
datas = img.getdata() 
newData = [] 
for item in datas: 
    if item[0] == 255 and item[1] == 255 and item[2] == 255: 
        newData.append((255, 255, 255, 0)) 
    else: 
        newData.append(item) 

img.putdata(newData) 
img.save("mod_img1.png", "PNG")
 
background = Image.open("mod_img1.png") 
foreground = Image.open("mod_img2.png") 

background.paste(foreground, (0, 0), foreground) 
background.show()

###################################
URL = "https://comms.info.nearmap.com/rs/133-OSS-335/images/nearmap-on-screens.jpg"
from urllib import request

response = request.urlretrieve(URL, "someImg.jpg")
  
