from ipywidgets import widgets 
from IPython.display import display 
 
def onButtonClick(b):
    print("Button " + b.description + " has been clicked")
 
for i in range(1,4):
    button = widgets.Button(description=str(i))
    display(button)
    button.on_click(onButtonClick)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#If the code above shows error in anaconda prompt run the following lines
'''conda install -n base -c conda-forge widgetsnbextension
conda install -n AC36 -c conda-forge ipywidgets'''

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
#Species distribution model in DISMO package of R
'''logo <- stack(system.file("external/rlogo.grd", package="raster"))
v <- extract(logo, pts)
bc <- bioclim(v)
p1 <- predict(logo, bc)
p2 <- predict(logo, bc, tails=c('both', 'low', 'high'))

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
tmin <- c(10,12,14,16,18,20,22,21,19,17,15,12)
tmax <- tmin + 5
prec <- c(0,2,10,30,80,160,80,20,40,60,20,0)
biovars(prec, tmin, tmax)
tmn = tmx = prc = brick(nrow=1, ncol=1)
tmn <- setValues(tmn, t(matrix(c(10,12,14,16,18,20,22,21,19,17,15,12))))
tmx <- tmn + 5
prc <- setValues(prc, t(matrix(c(0,2,10,30,80,160,80,20,40,60,20,0))))
b <- biovars(prc, tmn, tmx)
as.matrix(b)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
calc.deviance(obs, pred, weights = rep(1,length(obs)),
family="binomial", calc.mean = TRUE)


r <- raster(system.file("external/rlogo.grd", package="raster"))
#presence data
pts <- matrix(c(17, 42, 85, 70, 19, 53, 26, 84, 84, 46, 48, 85, 4, 95, 48, 54, 66,
74, 50, 48, 28, 73, 38, 56, 43, 29, 63, 22, 46, 45, 7, 60, 46, 34, 14, 51, 70, 31, 39, 26), ncol=2)
train <- pts[1:12, ]
test <- pts[13:20, ]
ch <- circleHull(train)
predict(ch, test)
plot(r)
plot(ch, border='red', lwd=2, add=TRUE)
points(train, col='red', pch=20, cex=2)
points(test, col='black', pch=20, cex=2)
pr <- predict(ch, r, progress='')
plot(pr)
points(test, col='black', pch=20, cex=2)
points(train, col='red', pch=20, cex=2)
# to get the polygons:
p <- polygons(ch)
p
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
## S4 method for signature 'matrix'
circles(p, d, lonlat, n=360, r=6378137, dissolve=TRUE, ...)
## S4 method for signature 'SpatialPoints'
circles(p, d, lonlat, n=360, r=6378137, dissolve=TRUE, ...)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
r <- raster(system.file("external/rlogo.grd", package="raster"))
#presence data
pts <- matrix(c(17, 42, 85, 70, 19, 53, 26, 84, 84, 46, 48, 85, 4, 95, 48, 54, 66,
74, 50, 48, 28, 73, 38, 56, 43, 29, 63, 22, 46, 45, 7, 60, 46, 34, 14, 51, 70, 31, 39, 26), ncol=2)
train <- pts[1:12, ]
test <- pts[13:20, ]
cc <- circles(train, lonlat=FALSE)
predict(cc, test)
plot(r)
plot(cc, border='red', lwd=2, add=TRUE)
points(train, col='red', pch=20, cex=2)
points(test, col='black', pch=20, cex=2)'''
