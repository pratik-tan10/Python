import dask.dataframe as dd

usecols = ['dropoff_x','dropoff_y','pickup_x','pickup_y','dropoff_hour','pickup_hour','passenger_count']
%time df = dd.read_parquet('data/nyc_taxi_wide.parq')[usecols].persist()
df.tail()

import numpy as np
import holoviews as hv
from holoviews import opts
from holoviews.element.tiles import StamenTerrain
hv.extension('bokeh')

plot_width  = int(750)
plot_height = int(plot_width//1.2)
x_range, y_range =(-8242000,-8210000), (4965000,4990000)
plot_options = hv.Options(width=plot_width, height=plot_height, xaxis=None, yaxis=None)

samples = df.sample(frac=1e-4)
tiles = StamenTerrain().redim.range(x=x_range, y=y_range)
points = hv.Points(samples, ['dropoff_x', 'dropoff_y'])
(tiles * points)

tiles * hv.Points(df.sample(frac=1e-3), ['dropoff_x', 'dropoff_y'])
tiles * hv.Points(df.sample(frac=1e-2), ['dropoff_x', 'dropoff_y']).opts(size=1, alpha=0.1)

import datashader as ds
from datashader import transfer_functions as tf
from datashader.colors import Greys9
Greys9_r = list(reversed(Greys9))[:-2]
