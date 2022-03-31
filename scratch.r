fun1<- function(x,a,b,c){
a*x*exp(-b*x)+c
}
fun2<- function(x,a,b,c){
-a*x*exp(-b*x)+c
}
a<-1
b<-2
c<- -0.1
x.seq<-seq(0,5,0.01)
y.seq<- fun2(x.seq,a,b,c)
plot(x.seq,y.seq,type="l")
abline(h=0)

optimize(f=fun2,interval=c(0,2),a,b,c)
optimize(f=fun1,interval=c(0,2),maximum=TRUE,a,b,c)

x<- c(0.164,0.117,1.880,0.424,0.280,0.353,0.574,0.096,1.081,0.693,1.449,1.181,0.364,0.359,2.173,0.374,0.192,1.617,2.070,1.922)
hist(x)
rug(x)

logL<-function(pars,x){
alpha<-pars[1]
beta<-pars[2]

n<- length(x)
res <- -n*log(gamma(alpha))-n*alpha*log(beta)-sum(x)/beta +(alpha-1)*sum(log(x))
return(-res)
}
alpha0<-1
beta0<-1
pars<-c(alpha0,beta0)
A<-optim(pars,logL,gr=NULL,x=x);A
