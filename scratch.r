my_data <- data.frame(x1 = 1:5,
                      x2 = 2:6,
                      x3 = 3)
my_data

my_list <- list(1:5,
                letters[1:3],
                777)
my_list
apply(my_data, 1, sum)
apply(my_data, 2, sum)
lapply(my_list, length)
sapply(my_list, length) 
vapply(my_list, length, integer(1))  

input_values <- 1:10
input_values
input_factor <- rep(letters[1:5], 2)
input_factor
tapply(input_values, input_factor, sum) 
mapply(rep, times = 1:5, letters[1:5]) 
