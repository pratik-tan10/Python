colnames(state.x77)
head(state.x77[,"Income"])
par(oma = c(5, 0, 0, 0), las = 2) 
plot(state.division,state.x77[,"Income"])

par(mfrow = c(2, 2), mar = rep(4, 4))
hist(rnorm(30,mean=4,sd=2))
plot(dexp(5),type = "l")
boxplot(rgamma(30,3,scale=2))
qqnorm(rchisq(30,df=3))

pairs(iris[,1:4], main = "Iris Data", pch = 20,
      col = unclass(iris$Species) + 2)
head(mtcars)
d<-mtcars[,c("mpg","disp","hp","drat","qsec")]
carsize <- cut(mtcars[,"wt"], c(0, 2.5, 3.5, 5.5), labels = c("Compact", "Midsize", "Large"))
pairs(mtcars[,c("mpg","disp","hp","drat","qsec")],main = "mtcars Data", pch = 20, col = unclass(carsize))

rg<- apply(matrix(rgamma(10000,scale=1,shape=2),ncol=10),1,mean)
par(mfrow = c(2, 2))
hist(rg)
plot(density(rg))
boxplot(rg)
qqnorm(rg)

# Load and plot the scanned map
require(raster)
iraq.img <- brick("iraq_oil_2003.jpg")
plotRGB(iraq.img)

# Load images with the (pre-classified) training data
training.ppl.img <- brick("iraq_pipelines_train.jpg")
training.noppl.img <- brick("iraq_nopipelines_train.jpg")

# Put training data into data frame
training.ppl.df <- data.frame(getValues(training.ppl.img))
names(training.ppl.df) <- c("r", "g", "b")
# Remove white background pixels
training.ppl.df <- training.ppl.df[(training.ppl.df$r < 254 & training.ppl.df$g < 254 & training.ppl.df$b < 254),]
# Create new variable indicating pipeline pixels
training.ppl.df$pipeline <- "P"
# Do the same for the non-pipeline image
training.noppl.df <- data.frame(getValues(training.noppl.img))
# etc...
