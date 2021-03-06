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

m5values = [0.432523, -0.123223, -0.231232, 0.001231, -0.23698, -0.41231]
df['m5'] = m5values
df

df.loc[pd.Timestamp('2017-01-07'),:] = [ ... ]
for i in range(7,10):
    df.loc[ pd.Timestamp('2017-01-0'+str(i)),:] = [ np.random.rand() for j in range(5) ]
df

df1 = pd.DataFrame( {'state': ['Washington', 'Oregon'], 'capital': ['Olympia', 'Salem']} )
print(df1)
df2 = pd.DataFrame( {'name': ['Washington', 'Oregon'], 'population':[7288000, 4093000]} )
print(df2

merged = df1.merge(df2, left_on='state', right_on='name')
merged

newMerged = merged.drop('name', axis=1)
newMerged

df > 0
	
df.m1 * 2 < 0.2
(df.m1 * 2 < 0.2).value_counts()
v1 = df.m1 * 2 < 0.2
print(v1)
v2 = df.m2 > 0
print(v2)
print(~v1)
print(v1 & v2)
print(v1 | v2)

df[ [True, False, True, False, True, False, True, False, True] ]
df[v1 &v2]
df[(df.m1*2<0.2) &(df.m2<0)]

