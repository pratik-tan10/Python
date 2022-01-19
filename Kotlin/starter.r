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


###########################
vapply(flags, unique, numeric(1))
sapply(flags, class)
vapply(flags, class, character(1))
?tapply
sapply(flags, class)
table(flags$animate)
tapply(flags$animate, flags$landmass,mean)
tapply(flags$population,flags$red,summary)

###########################
a <-ls();a
class(plants)
dim(plants)
ncol(plants);nrow(plants)
ncol(plants)
object.size(plants)/1024^2
names(plants)
head(plants)
head(plants,10)
tail(plants, 15)
summary(plants)
table(plants$Active_Growth_Period)
str(plants)

###########################
sample(1:20,10)
LETTERS
sample(LETTERS)
sample(c(0,1),100,replace = TRUE, prob = c(0.3,0.7)) ->flips
flips
mean(flips)
flips2 <-rbinom(100,size = 1, prob = 0.7)
flips2
sum(flips2)
rnorm(10, mean = 100, sd =25)
rpois(5,10)
replicate(100, rpois(5,10)) -> my_pois
cm <- colMeans(my_pois)
hist(cm)
