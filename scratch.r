#1a
f11<-function(x)x^3-x+1
interval1<-seq(-5,5,length=20)
plot(interval1,f11(interval1),type="l");points(interval1,f11(interval1))
uniroot(f11,interval=c(-2,1))

#1b
f12<-function(x)x*exp(sqrt(x))-1
interval1<-seq(0,1,length=20)
plot(interval1,f12(interval1),type="l");points(interval1,f12(interval1))
uniroot(f12,interval=c(0,1))

#1c
f13<-function(x)x-(log(x))^2
interval1<-seq(0.1,2,length=20)
plot(interval1,f13(interval1),type="l");points(interval1,f13(interval1))
uniroot(f13,interval=c(0.1,2))

#2
bisect <- function(fun, x0, x1, eps){
  iterno <- 0
  repeat {
    iterno <- iterno +1
    x2 <- (x0 + x1) / 2
    if (fun(x2) * fun(x0) < 0) x1 <- x2
    else x0 <- x2
    if (abs(x1 - x0) < eps || abs(fun(x2)) < eps) break
    cat("****** Iter. No: ", iterno, " Current Iterate = ", x2, "\n")
  }
  return(x2)
}

#2a
f21<-function(x)exp(-x)-cos(x)
ivl<-seq(-1,1,length=20)
plot(ivl,f21(ivl),type="l");points(ivl,f21(ivl))
bisect(f21,-1,1,0.0001)

#2b
f22<-function(x)exp(x)-4*x^2
ivl<-seq(-1,1,length=20)
plot(ivl,f22(ivl),type="l");points(ivl,f22(ivl))
bisect(f22,-0.5,0,0.0001)

#3
f3<-function(x) (log(x))/(1+x)
df3<-function(x){
  (1/(x*(1+x)))-((log(x))/((1+x)^2))
}
ivl<-seq(1,5,length=20)
plot(ivl,df3(ivl),type="l")
bisect(df3,3.5,3.75,0.0000001);abline(h=0)
optimize(f=f3,c(3.5,3.75),maximum=TRUE)

#4
f4<- function(pars){
  pars[1]->x
  pars[2]->y
  f <- 20*x-x^2+30*y-y^2+x*y
  return (-f)
}
result<-optim(c(0,0),f4,gr=NULL);result
cat(paste("The maximum value of given function is",round(-result$value,3),", when x is", round(result$par[1],3) ,"and y is",round(result$par[2],3),"."))
