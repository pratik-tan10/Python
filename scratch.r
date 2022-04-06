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
