set.seed(0)
d<- rnorm(20,mean = 2,sd=sqrt(2))
M <-matrix(d,4,5,TRUE)
sum(M<2)
M[which(M<2)]
MM <-M; MM[which(MM<2)]<-0; MM
MN <-M; ifelse(MN[,c(1,3)]<2,0,MN[,c(1,3)]) -> MN[,c(1,3)]; MN
X <- cbind(MN,c(1,2,3,4));X
sum(X^2)
sum(diag(t(X)%*%(X)))
ev<-eigen(t(X)%*%(X))$values;ev;sum(ev)
X-rep(colMeans(X),rep(nrow(X),ncol(X)))
##############################
A<- matrix(c(4.5,−2.1,6.3,2.7,1.6,−2.6,3.6,8.4,5.2,8.3,2.5,1.7,3.7,−4.4,3.7,3.8,5.8,5.2,1.9,−4.2),4,5,TRUE)
A
A<-matrix(scan("mat.txt"),ncol=5,byrow=TRUE);A
y<-A[3,2:4];y
d <- B %*% y; y
W <-cbind(c(9.4,10.5,-11.5),B);W
a<- solve(P)%*%d;a
a<-solve(P,d);a
Q <-solve(P); Q
##############################
A[ifelse((which(A==max(A))%%4==0),4,which(A==max(A))%%4),]
A[ifelse((which(A==max(A))%%nrow(A)==0),nrow(A),which(A==max(A))%%nrow(A)),]
A[,ceiling(which(A==min(A))/4)]
A[,ceiling(which(A==min(A))/nrow(A))]

##############################
Cars93[Cars93$MPG.highway<25&Cars93$Weight>3500,c("Model","Min.Price","Max.Price","MPG.highway","Weight")]
