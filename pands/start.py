import pandas as pd
import numpy as np

dates = pd.date_range('20170101' , periods=6, freq='D')
dates
numbers = np.random.randn(6,4)
numbers
df = pd.DataFrame(numbers, index=dates, columns=['m1','m2','m3','m4'])
df

df.info()

print(len(df))          # gives you the number of rows
print(len(df.columns))  # gives you the number of columns

firstRows = df.head(2)
print(firstRows)
lastRows = df.tail(2)
print(lastRows)

someRows = df[3:5]    # gives you the 4th and 5th row
print(someRows)
thirdColumn = df.m3
print(thirdColumn)

columnsM3andM2 = df[ ['m3', 'm2'] ]
columnsM3andM2

someSubset = df[['m3', 'm2']][3:5]
someSubset

someSubset = df.iloc[2:4,1:3] 
print(someSubset)

someSubset = df.iloc[ [0,2,4], [1,3] ]
print(someSubset)

allRowsSomeColumns = df.iloc[ : , [1,3] ]
print(allRowsSomeColumns)

someSubset = df.loc[ [pd.Timestamp('2017-01-01'), pd.Timestamp('2017-01-03'), pd.Timestamp('2017-01-05')] , ['m2', 'm4'] ]
print(someSubset

	
df.loc['2017' , ['m2', 'm4'] ]

	
df.iloc[0,0] = 0.17

df.loc['2017-01-01', 'm1'] = 0.17

df

dfCopy = df.copy()
dfCopy.iloc[0,0] = 0
print(df)
print(dfCopy

df.iloc[ [0,4] , [0] ] = 1.2
print(df)

for row in df.itertuples(index=False):
    print(row)     # print entire row tuple
    print(row[0])  # print value from column with index 0
    print(row.m2)  # print value from column with name m2
    print('----------')
      
dfSorted = df.sort_values(by='m2', ascending=False)
dfSorted

