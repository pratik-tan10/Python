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
