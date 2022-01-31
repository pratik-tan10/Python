rep(c(1,3,6),c(6,6,6))
rep(c(1,2,3,4,5),5:1)
rep(c(1,3,6),c(3,1,6))
#------------------------
attach(Orange)
r <- sum((age-mean(age))*(circumference - mean(circumference)))/sqrt(sum((age - mean(age))**2)*sum((circumference - mean(circumference))**2))
r
cor(age,circumference)

#----------------------------------------------------
s <- c( 4.5, 7.3, 0.017, 12, 15, 8.4, 8.9)
sum(sqrt(abs(s-mean(s))))
max((s - median(s))**2)

abs(round(sqrt(s),2)**2-s)
#---------------------------------------------------------
1.4826*median(abs(chickwts$weight-median(chickwts$weight)))
mad(chickwts$weight)
