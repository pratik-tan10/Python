# Create two vectors of different lengths.
v1 <- c(5,9,3)
v2 <- c(10,11,12,13,14,15)
column.names <- c("COL1","COL2","COL3")
row.names <- c("ROW1","ROW2","ROW3")
matrix.names <- c("Matrix1","Matrix2")

# Take these vectors as input to the array.
result <- array(c(v1,v2),dim = c(3,3,2),dimnames = list(row.names,column.names,
   matrix.names))
print(result)
