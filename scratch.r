#install.packages(c("spdep","sp"))
library(spdep)
#library(sp)
library(rgdal)
library(sf)
setwd("Location/al_tuscaloosa.gpkg")

st_read("al_tuscaloosa.gpkg")->nepal
nepal$uid<-paste0(nepal$uid0,"a")
nepal$LUC<- sample(rep(1:5,length(nepal$uid)/3),length(nepal$uid))
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

#above this works
#Add columns indicating lu class to polygons, LUC is the column containing LU class info
for( i in seq_along(unique(nepal$LUC))){
  nbrInfo[paste0("Lu_",i)]<-0
}

for( i in seq_along(unique(nepal$LUC))){
  nbrInfo[paste0("Lu_",i)]<-0
}

#Final function to compute area of each LU type
for(jj in nepal$uid0){
  for(kk in unique(nepal$LUC)){
    #nbrInfo[jj,1+kk]<-sum(subset(nepal[as.integer(unlist(nbrInfo[jj,1])),2:3],LUC==kk)$Area)
    nbrInfo[jj,1+kk]<-sum(subset(nepal[as.integer(nbrInfo[jj,1][[1]]),c("area","LUC")],LUC==kk)$area)
  }
}


#cbind()

#Export dataframe to csv
write.csv(nbrInfo[,-1],"nbrInfo0.csv")
