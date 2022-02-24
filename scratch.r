sum = 0
for (i in x$Horsepower){
  sum<-sum + i
}
average <- sum/length(x$Horsepower)
average

sweep(x[,c("Min.Price","Price","Max.Price")],2, colMeans(x[,c("Min.Price","Price","Max.Price")]))

x <- Cars93
c(median(x[,"Min.Price"]),median(x[,"Price"]), median(x[,"Max.Price"])) ->mdn
head(x)
for ( i in 1:dim(x)[1]){
  for (j in 1:3){
    x[i,j+3] <- x[i,j+3] - mdn[j]
  }
}
head(x)
