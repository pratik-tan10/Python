#install.packages(c("spdep","sp"))
setwd("drive:/some/location/on/disk")
library(spdep)
#library(sp)
library(rgdal)

#Read input data
nepal <- readOGR("dummyLUNeig.shp", "dummyLUNeig")
row.names(nepal) <- as.character(nepal$DISTRICT)
#DISTRICT is the unique identifier
nb <- poly2nb(nepal)
names(nb)<-row.names(nepal)

#Unlist the neighbor list
ul<-unlist(nb)
#This is to remove the last character that is added to the name after unlisting
names(ul)<-lapply(names(ul),function(x){substr(x,1,nchar(x)-1)})

#Create list of all neighbors for each polygon and convert to dataframe
cmbd<-data.frame(cbind(names(ul),ul))
colnames(cmbd)<-c("Name","Neighbor")
nbrInfo<-data.frame(tapply(cmbd$Neighbor,cmbd$Name,function(x2)x2))
colnames(nbrInfo)<-"Neighbor"

#Add columns indicating lu class to polygons, LUC is the column containing LU class info
for( i in seq_along(unique(nepal@data[["LUC"]]))){
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

### Get the library.
library(plotrix)

# Create data for the graph.
x <-  c(21, 62, 10,53)
lbl <-  c("London","New York","Singapore","Mumbai")

# Give the chart file a name.
png(file = "3d_pie_chart.jpg")

# Plot the chart.
pie3D(x,labels = lbl,explode = 0.1, main = "Pie Chart of Countries ")

# Save the file.
dev.off()
