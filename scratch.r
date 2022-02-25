myMedian<- function (x,y,z) {
  a = x-y; b = y-z; c = x-z
  if(a*b > 0){ ans<- y;}
  else if(a*c >0) { ans<- z;}
  else {ans<- x;}
  ans
}

myMedian(-1,-100,-17)
myMedian(21,100,38)

rs = rnorm(20, mean = 2, sd = sqrt(4));rs
M <-matrix(rs,4,5,TRUE);M
M<-ifelse(M<2,0,M); M

myDot<- function(x,y){
sum = 0
for (i in 1: length(x)){
  sum<- sum+ x[i]*y[i]
}
sum
}

x<- c(3,7,5); y<- c(7,6,2)
myDot(x,y)


x <- 2.345
n <- 0
comp <- 0
repeat{
  n <- n + 1
  strt <- (-1)^(n - 1)
  pow <- x^(2*(n - 1))
  dvidor <- factorial(2*(n - 1))
  term <- (strt*pow)/dvidor
  comp <- comp + term
  if(abs((cos(x) - comp)/cos(x))*100 < 0.00001) break
}
comp
cos(x)

x <- seq(0.1, 1, by=0.1)
i <- 0
while(i<length(x)){
  if(i==0){cat(sprintf("  x     Computed     From R  Absolute Difference\n"))}
  i <- i+1
  calculated<- -0.076 + 0.281*x[i] - 0.238/(x[i] + 0.15)
  fromR<- log10(x[i])
  difference <- abs(calculated-fromR)
  #print(c(calculated, fromR, difference))
  cat(sprintf("%*.2f,%*.6f, %*.6f, %*.6f\n",5,x[i],10,calculated,10,fromR,10,difference))
}

data(Cars93, package = "MASS")
myMatrix <- Cars93[,c("Min.Price", "Max.Price", "MPG.city", "MPG.highway", "EngineSize", "Length", "Weight")]
head(myMatrix)
cars.stats<-list("Cars.Means" = apply(myMatrix,2, mean),
                 "Cars.Std.Errors" = apply(myMatrix,2, function(x2) sd(x2)/sqrt(length(x2))),
                 "Cars.CI.99" =apply(myMatrix,2,
                                     function(x2){
                                       lim<- 2.576*sd(x2)/sqrt(length(x2));
                                       me<-mean(x2);
                                       rbind(me-lim,me+lim)
                                       }))
cars.stats



apply(iris3,c(3,2),mean)
apply(iris3, 2, mean)
sapply(1:dim(iris3)[3], function(i) var(iris3[,,i]), simplify="array")


tapply(state.x77[,"Income"],state.region,mean)
tapply(state.x77[,"Illiteracy"],state.division,max)

cbind(state.abb,data.frame(state.x77),state.region) ->combd
tapply(combd[,"state.abb"],combd[,"state.region"],function(x2) length(x2))

tapply(rownames(state.x77),combd[,"state.region"],function(x2) x2)
state.size <- cut(state.x77[,"Population"],
                  breaks = c(0, 2000,10000, Inf), labels = c("Small", "Medium", "Large"))
tapply(combd[,"HS.Grad"],list(state.region,state.size),median)
