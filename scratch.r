mydata<-data.frame(x=c(0,2,4,15,48,75,122),y=c(123,116,113,100,87,84,77))
library(ggplot2)
qplot(x,y,data=mydata,geom="line")
f <- function(x, a, b) {
  a * exp(b *-x)
}
x <- seq(0:100)
y <- f(seq(0:100), 1,1)
qplot(x,y, geom="line")
fit <- nls(y~f(x,a,b,c), data=data.frame(mydata), start=list(a=1, b=30, c=-0.3))
x <- seq(0,120)
fitted.data <- data.frame(x=x, y=predict(fit, list(x=x)))
                          ggplot(mydata, aes(x, y)) + geom_point(color="red", alpha=.5) + geom_line(alpha=.5) + geom_line(data=fitted.data)
                          
