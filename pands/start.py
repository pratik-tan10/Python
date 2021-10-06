import pandas as pd
import numpy as np

dates = pd.date_range('20170101' , periods=6, freq='D')
dates
numbers = np.random.randn(6,4)
numbers
df = pd.DataFrame(numbers, index=dates, columns=['m1','m2','m3','m4'])
df
