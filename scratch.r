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

LOG <- lg <- ab <- numeric(length(x))
x <- seq(0.1, 1, by = 0.1)
i <- 0
while(i < 10) {
  i <- i + 1
  LOG[i] <- -0.076 + 0.281*x[i] - 0.238/(x[i] + 0.15)
  lg[i] <- log10(x[i])
  ab[i] <- abs(lg[i] - LOG[i])
  cat("i = ", i, "LOG = ", LOG, "log = ", lg, "abs = ", ab, fill = TRUE)
}
