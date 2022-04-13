#install.packages(c("spdep","sp"))
setwd("C:/Users/Research Lab/OneDrive - The University of Alabama/Rupesh/Shapefiles")
library(spdep)
#library(sp)
library(rgdal)
library(sf)

setwd("C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch/al_tuscaloosa.gpkg")
#Read input data
#nepal <- readOGR("dummyLUNeig.shp", "dummyLUNeig")
##row.names(nepal) <- as.character(nepal$DISTRICT)
#DISTRICT is the unique identifier
##nb <- poly2nb(nepal)
##names(nb)<-row.names(nepal)


``
st_read("al_tuscaloosa.gpkg")->nepal
nepal$uid<-paste0(nepal$uid0,"a")
row.names(nepal) <- paste0(nepal$uid0,"a")
nb <- poly2nb(nepal,row.names = row.names(nepal))
names(nb)<-row.names(nepal)
``
#Unlist the neighbor list
ul<-unlist(nb)
#This is to remove the last character that is added to the name after unlisting
names(ul)<-lapply(names(ul),function(x){strsplit(x,"a")[[1]][1]})

#Create list of all neighbors for each polygon and convert to dataframe
cmbd<-data.frame(cbind(names(ul),ul))
colnames(cmbd)<-c("Name","Neighbor")
nbrInfo<-data.frame(tapply(cmbd$Neighbor,cmbd$Name,function(x2)x2))
colnames(nbrInfo)<-"Neighbor"

#above this works
#Add columns indicating lu class to polygons, LUC is the column containing LU class info
for( i in seq_along(unique(nepal@data[["LUC"]]))){
  nbrInfo[paste0("Lu_",i)]<-0
}
for( i in seq_along(unique(nepal$LUC))){
  nbrInfo[paste0("Lu_",i)]<-0
}

#Final function to compute area of each LU type
for(jj in seq_along(nepal@data[["DISTRICT"]])){
  for(kk in unique(nepal@data[["LUC"]])){
    nbrInfo[jj,1+kk]<-sum(subset(nepal@data[as.integer(unlist(nbrInfo[jj,1])),2:3],LUC==kk)$Area)
  }
}

#Export dataframe to csv
write.csv(nbrInfo[,-1],"nbrInfo.csv")
