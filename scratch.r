x <- c(0.103, 0.528, 0.221, 0.260, 0.091,
            1.314, 1.732, 0.244, 1.981, 0.273,
            0.461, 0.366, 1.407, 0.079, 2.266)

# Histogram of the data
hist(x)
# install.packages(MASS)
library(MASS)

boxcox(lm(x ~ 1))
# Transformed data
new_x <- log(x)

# Histogram
hist(new_x)
shapiro.test(new.x)
# install.packages(MASS)
library(MASS)

b <- boxcox(lm(x ~ 1))

# Exact lambda
lambda <- b$x[which.max(b$y)] # -0.02
new_x_exact <- (x ^ lambda - 1) / lambda
