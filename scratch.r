colnames(state.x77)
head(state.x77[,"Income"])
par(oma = c(5, 0, 0, 0), las = 2) 
plot(state.division,state.x77[,"Income"])

par(mfrow = c(2, 2), mar = rep(4, 4))
hist(rnorm(30,mean=4,sd=2))
plot(dexp(5),type = "l")
boxplot(rgamma(30,3,scale=2))
qqnorm(rchisq(30,df=3))

pairs(iris[,1:4], main = "Iris Data", pch = 20,
      col = unclass(iris$Species) + 2)
head(mtcars)
d<-mtcars[,c("mpg","disp","hp","drat","qsec")]
carsize <- cut(mtcars[,"wt"], c(0, 2.5, 3.5, 5.5), labels = c("Compact", "Midsize", "Large"))
pairs(mtcars[,c("mpg","disp","hp","drat","qsec")],main = "mtcars Data", pch = 20, col = unclass(carsize))

rg<- apply(matrix(rgamma(10000,scale=1,shape=2),ncol=10),1,mean)
par(mfrow = c(2, 2))
hist(rg)
plot(density(rg))
boxplot(rg)
qqnorm(rg)
