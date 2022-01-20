d1 <- Sys.Date()
class(d1)
unclass(d1)
d1
d2 <- as.Date("1969-01-01")
unclass(d2)
t1 <- Sys.time()
t1
class(t1)
unclass(t1)
t2 <-as.POSIXlt(Sys.time())
class(t2)
unclass(t2)
t2
str(unclass(t2))
t2$min
weekdays(d1)
months(t1)
quarters(t2)
t3 <- "October 17, 1986 08:24"
strptime(t3, "%B %d, %Y %H:%M") ->t4
t4
class(t4)
Sys.time() > t1
Sys.time()-t1
difftime(Sys.time(), t1, units = 'days')

data(cars)
?cars
head(cars)
dim(cars);names(cars);summary(cars)
plot(cars)
plot(x = cars$speed, y = cars$dist)

plot(x = cars$speed, y = cars$dist, xlab = "Speed", ylab = "Stopping Distance")
plot(cars, main = "My Plot")
plot(cars, sub = "My Plot Subtitle")
plot(cars, col =6)
plot(cars, xlim = c(10,15))
plot(cars, pch = 2)
data(mtcars)
play()
dim(mtcars)
names(mtcars)
head(mtcars)
str(mtcars)
summary(mtcars)
nxt()
?boxplot
