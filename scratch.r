library(datasets)
with(airquality, plot(Wind,Ozone))
title(main = "Ozone and Wind in New York City")

with(airquality,plot(Wind,Ozone, main = "Ozone and Wind in New York City"))
with(subset(airquality,Month==5),point(Wind,Ozone,col="blue"))

with(airquality,plot(Wind,Ozone, main = "Ozone and Wind in New York City", type="n"))
with(subset(airquality,Month==5),point(Wind,Ozone,col="blue"))
with(subset(airquality,Month!=5),point(Wind,Ozone,col="red"))
legend("topright",pch=1,col=c("blue","red"),legend=c("May","Other Months"))

with(airquality,plot(Wind,Ozone, main = "Ozone and Wind in New York City", pch=20))
model<-lm(Ozone~Wind,airquality)
abline(model,lwd=2)

par(mfrow=c(1,3),mar=c(4,4,2,1),oma=c(0,0,2,0))
wigh(airquality,{plot(Wind,Ozone,main="Ozone and Wind")
                 plot(Solar.R,Ozone,main="Ozone and Solar Radiation")
                 plot(Temp,Ozone,main="Ozone and Temperature")
                 mtext("Ozone and Weather in New York City", outer=TRUE
                 })
