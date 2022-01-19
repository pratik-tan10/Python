Sys.Date()
mean(c(2,4,5))
submit()
boring_function("My first function!")
boring_function
my_mean(c(4,5,10))
remainder(5)
remainder(11,5)
remainder(divisor = 11, num = 5)
remainder(4, div=2)
args(remainder)
evaluate(sd, c(1.4,3.6,7.9,8.8))
evaluate(function(x){x+1},6)
evaluate(function(x){x[length(x)]},c(8,4,0))
paste("Programming", "is","fun!")


head(flags)
dim(flags)
viewinfo()
class(flags)
cls_list <- lapply(flags, class)
cls_list
class(cls_list)
as.character(cls_list)
cls_vect<-sapply(flags, class)
class(cls_vect)
sum(flags$orange)
flag_colors<-flags[,11:17]
head(flag_colors)
lapply(flag_colors, sum)
sapply(flag_colors, sum)
sapply(flag_colors, mean)
flag_shapes <-flags[,19:23]
lapply(flag_shapes, range)
sapply(flag_shapes, range) ->shape_mat
shape_mat
class(shape_mat)
unique(c(3,4,5,5,5,6,6))
unique_vals<-lapply(flags, unique)
unique_vals
sapply(unique_vals,length)
sapply(flags, unique)
lapply(unique_vals, function(elem)elem[2])
