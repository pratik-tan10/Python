data(Cars93, package = "MASS")
sum = 0
for (each in Cars93[,"Horsepower"]){
  sum = sum+ each
}
m = sum/length(Cars93[,"Horsepower"])
mean(Cars93[,"Horsepower"])
tapply(Cars93[,"EngineSize"],list(Cars93[,"Type"],Cars93[,"Origin"]),median)
sweep(Cars93[,c("Min.Price","Price","Max.Price")],2,apply(Cars93[,c("Min.Price","Price","Max.Price")],2,median))

plot(rnorm(10), 20+rnorm(10), type = "n", xlab = "Illiteracy", ylab="Murder Rate")
points(seq(-1,1,length=10),seq(19,21,length =10), col = 4, pch = 8)
height2 <- list("gender"=c(1,1, 1, 1, 1, 2, 2, 2, 2, 2), "height" = c(178, 175, 182, 193, 171, 159, 167, 173, 153, 160))
plot(height2$gender,height2$height)
gender2<- factor(height2$gender)
plot(gender2,height2$height)
