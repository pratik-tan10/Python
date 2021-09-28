import numpy as np
import pandas as pd

my_array = np.array([[11,22,33],[44,55,66]])

df = pd.DataFrame(my_array, columns = ['Column_A','Column_B','Column_C'], index = ['Item_1', 'Item_2'])

print(df)
print(type(df))
