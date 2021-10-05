from ipywidgets import widgets 
from IPython.display import display 
 
def onButtonClick(b):
    print("Button " + b.description + " has been clicked")
 
for i in range(1,4):
    button = widgets.Button(description=str(i))
    display(button)
    button.on_click(onButtonClick)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
conda install -n base -c conda-forge widgetsnbextension
conda install -n AC36 -c conda-forge ipywidgets

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
logo <- stack(system.file("external/rlogo.grd", package="raster"))
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
