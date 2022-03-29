library(datasets)
with(airquality, plot(Wind,Ozone))
title(main = "Ozone and Wind in New York City")

with(airquality,plot(Wind,Ozone, main = "Ozone and Wind in New York City"))
with(subset(airquality,Month==5),point(Wind,Ozone,col="blue"))

with(airquality,plot(Wind,Ozone, main = "Ozone and Wind in New York City", type="n"))
with(subset(airquality,Month==5),point(Wind,Ozone,col="blue"))
with(subset(airquality,Month!=5),point(Wind,Ozone,col="red"))
legend("topright",pch=1,col=c("blue","red"),legend=c("May","Other Months"))
