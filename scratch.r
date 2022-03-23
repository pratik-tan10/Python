illit <- state.x77[,3]
murder <- state.x77[,5]
plot(illit, murder)
plot(illit, murder, type = "l")
x <- seq(-3, 3, length = 100)
plot(x, dnorm(x), type="l")
barplot(rep(1, 15), col = 1:15)
plot(illit, murder, pch = 3, xlab = "Illiteracy", ylab = "Murder Rate")
regout <- lsfit(illit, murder)
regout$coef
yhat <- regout$coef[1] + regout$coef[2] * illit
lines(illit, yhat, col = 6)
abline(coef = regout$coef, col = 6)

plot(illit, murder, type = "n", xlab = "Illiteracy", ylab="Murder Rate")
points(illit, murder, col = 4, pch = 8)
abline(coef = regout$coef, col = 6)

state.abb
text(illit, murder, state.abb, cex = 0.7, adj = c(-0.5, -0.5), col = 6)
text(0.5, 14, adj = 0, cex = 1.5, "Plot of Murder Rate vs. Illiteracy")
label <- paste("Mean Murder Rate = ", as.character(mean(murder)))
text(1.7, 3, adj = 0, label)
plot(illit, regout$resid, col = 4, pch = 19, ylab = "Residuals")
abline(h = 0, lty = 3, col = 2)

library("mvtnorm")
Mu <- c(1, 2)
s <- matrix(c(1, -1, -1, 4), ncol = 2)
x <- seq(-3, 5, length = 100)
y <- seq(-5, 9, length = 100)
z <- matrix(NA, length(x), length(y))
for (i in 1:length(x)){
	for (j in 1:length(y)){
		z[i,j] <- dmvnorm(c(x[i], y[j]), Mu, S)
	}
}
contour(x, y, z)
persp(x, y, z)
persp(x, y, z, theta = 70, phi = 50)
income <- state.x77[,2]
coplot(murder ~ illit | income)
