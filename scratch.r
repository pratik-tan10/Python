library(spdep)
#library(sp)
library(rgdal)
library(sf)
setwd("C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch/al_tuscaloosa.gpkg")

st_read("al_tuscaloosa.gpkg")->nepal
nepal$uid<-paste0(nepal$uid0,"a")
row.names(nepal) <- paste0(nepal$uid0,"a")
nb <- poly2nb(nepal,row.names = row.names(nepal))
names(nb)<-row.names(nepal)

#Unlist the neighbor list
ul<-unlist(nb)
#This is to remove the last character that is added to the name after unlisting
names(ul)<-lapply(names(ul),function(x){strsplit(x,"a")[[1]][1]})

#Create list of all neighbors for each polygon and convert to dataframe
cmbd<-data.frame(cbind(names(ul),ul))
colnames(cmbd)<-c("Name","Neighbor")
nbrInfo<-data.frame(tapply(cmbd$Neighbor,cmbd$Name,function(x2)x2))
colnames(nbrInfo)<-"Neighbor"
