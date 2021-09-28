import numpy as np
import pandas as pd

my_array = np.array([['Jon',25,1995,2016],['Maria',47,1973,2000],['Bill',38,1982,2005]])

df = pd.DataFrame(my_array, columns = ['Name','Age','Birth Year','Graduation Year'])

df['Age'] = df['Age'].apply(int)
df['Birth Year'] = df['Birth Year'].apply(int)
df['Graduation Year'] = df['Graduation Year'].apply(int)

print(df)
print(type(df))
print(df.dtypes)
