import dask.dataframe as dd

usecols = ['dropoff_x','dropoff_y','pickup_x','pickup_y','dropoff_hour','pickup_hour','passenger_count']
%time df = dd.read_parquet('data/nyc_taxi_wide.parq')[usecols].persist()
df.tail()

import numpy as np
import holoviews as hv
from holoviews import opts
from holoviews.element.tiles import StamenTerrain
hv.extension('bokeh')
