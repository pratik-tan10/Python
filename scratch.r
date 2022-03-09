data(Cars93, package = "MASS")
sum = 0
for (each in Cars93[,"Horsepower"]){
  sum = sum+ each
}
m = sum/length(Cars93[,"Horsepower"])
mean(Cars93[,"Horsepower"])
tapply(Cars93[,"EngineSize"],list(Cars93[,"Type"],Cars93[,"Origin"]),median)
sweep(Cars93[,c("Min.Price","Price","Max.Price")],2,apply(Cars93[,c("Min.Price","Price","Max.Price")],2,median))
