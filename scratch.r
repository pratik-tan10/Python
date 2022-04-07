#install.packages(c("spdep","sp"))
setwd("C:/Users/Research Lab/OneDrive - The University of Alabama/Rupesh/Shapefiles")
library(spdep)
#library(sp)
library(rgdal)

nepal <- readOGR("dummyLUNeig.shp", "dummyLUNeig")
row.names(nepal) <- as.character(nepal$DISTRICT)
nb <- poly2nb(nepal)
names(nb)<-row.names(nepal)

#nepal@data[["DISTRICT"]][nb[[1]]]
#nepal@data[["Area"]][nb[[1]]]
#nepal@data[["LUC"]][nb[[1]]]
#cbind(names(nb)[1],nepal@data[["DISTRICT"]][nb[[1]]],nepal@data[["LUC"]][nb[[1]]],nepal@data[["Area"]][nb[[1]]])


ul<-unlist(nb)
names(ul)<-lapply(names(ul),function(x){substr(x,1,nchar(x)-1)})
cmbd<-cbind(names(ul),ul)
cmbd2<-data.frame(cmbd)
colnames(cmbd2)<-c("Name","Neighbor")
nbrInfo<-data.frame(tapply(cmbd2$Neighbor,cmbd2$Name,function(x2)x2))
colnames(nbrInfo)<-"Neighbor"
#nepal@data[["NBR"]]<-nbrInfo
#head(nepal@data)
#nbrInfo[paste0("Lu_",1)]<-0

for( i in seq_along(unique(nepal@data[["LUC"]]))){
  nbrInfo[paste0("Lu_",i)]<-0
}

#nbrInfo
#as.integer(unlist(nbrInfo[1,1]))
#nepal@data[["LUC"]]

#nbrInfo$Lu_1[1]<-sum(subset(nepal@data[as.integer(unlist(nbrInfo[1,1])),2:3],LUC==1)$Area)

#Final function to compute area of each LU type
for(jj in seq_along(nepal@data[["DISTRICT"]])){
  for(kk in unique(nepal@data[["LUC"]])){
    nbrInfo[jj,1+kk]<-sum(subset(nepal@data[as.integer(unlist(nbrInfo[jj,1])),2:3],LUC==kk)$Area)
  }
}

#Export dataframe to csv
write.csv(nbrInfo[,-1],"nbrInfo.csv")
