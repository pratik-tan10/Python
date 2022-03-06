connection <- url("http://biostat.jhsph.edu/~jleek/contact.html")
htmlCode <- readLines(connection)
close(connection)
c(nchar(htmlCode[10]), nchar(htmlCode[20]), nchar(htmlCode[30]), nchar(htmlCode[100]))

url <- "https://d396qusza40orc.cloudfront.net/getdata%2Fwksst8110.for"
lines <- readLines(url, n = 10)
w <- c(1, 9, 5, 4, 1, 3, 5, 4, 1, 3, 5, 4, 1, 3, 5, 4, 1, 3)
colNames <- c("filler", "week", "filler", "sstNino12", "filler", "sstaNino12", "filler", "sstNino3", "filler", "sstaNino3", "filler", "sstNino34", "filler", "sstaNino34", "filler", "sstNino4", "filler", "sstaNino4")
d <- read.fwf(url, w, header = FALSE, skip = 4, col.names = colNames)
d <- d[, grep("^[^filler]", names(d))]
sum(d[, 4])
?read.fwf
connection <- url("https://d396qusza40orc.cloudfront.net/getdata%2Fwksst8110.for")
lines <- readLines(connection, n = 10)
w <- c(1, 9, 5, 4, 1, 3, 5, 4, 1, 3, 5, 4, 1, 3, 5, 4, 1, 3)
colNames <- c("filler", "week", "filler", "sstNino12", "filler", "sstaNino12", "filler", "sstNino3", "filler", "sstaNino3", "filler", "sstNino34", "filler", "sstaNino34", "filler", "sstNino4", "filler", "sstaNino4")
d <- read.fwf(url, w, header = FALSE, skip = 4, col.names = colNames)
d <- d[, grep("^[^filler]", names(d))]
sum(d[, 4])

pairs(state.x77)
pairs(state.x77[,2:6])
pairs(state.x77[,2:6], panel = function(x, y){points(x, y); lines(lowess(x, y))})
stars(mtcars, cex = 0.5)
murder<-state.x77[,5]
illit<-state.x77[,3]
income <- state.x77[,2]
coplot(murder ~ illit | income)


library(MASS)
parcoord(state.x77)
parcoord(state.x77[, c(4, 6, 2, 5, 3)])

install.packages("mvtnorm")
library("mvtnorm")
Mu <- c(1, 2)
S <- matrix(c(1, -1, -1, 4), ncol = 2)
x <- seq(-3, 5, length = 100)
y <- seq(-5, 9, length = 100)
z <- matrix(NA, length(x), length(y))
for (i in 1:length(x)){
  for (j in 1:length(y)){
    z[i,j] <- dmvnorm(c(x[i], y[j]), Mu, S)
  }
}
contour(x, y, z)
persp(x, y, z)
persp(x, y, z, theta = 70, phi = 50)
