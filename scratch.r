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

                           
                           
mydata <- read.csv("https://stats.idre.ucla.edu/stat/data/binary.csv")
## view the first few rows of the data
head(mydata)
mydata$rank <- factor(mydata$rank)
mylogit <- glm(admit ~ gre + gpa + rank, data = mydata, family = "binomial")
summary(mylogit)
confint(mylogit)
confint.default(mylogit)
exp(cbind(OR = coef(mylogit), confint(mylogit)))
                           

newdata2 <- with(mydata, data.frame(gre = rep(seq(from = 200, to = 800, length.out = 100),
                                              4), gpa = mean(gpa), rank = factor(rep(1:4, each = 100))))

newdata3 <- cbind(newdata2, predict(mylogit, newdata = newdata2, type = "link",
                                    se = TRUE))
newdata3 <- within(newdata3, {
  PredictedProb <- plogis(fit)
  LL <- plogis(fit - (1.96 * se.fit))
  UL <- plogis(fit + (1.96 * se.fit))
})

## view first few rows of final dataset
head(newdata3)
library(ggplot2)
ggplot(newdata3, aes(x = gre, y = PredictedProb)) + geom_ribbon(aes(ymin = LL,
                                                                    ymax = UL, fill = rank), alpha = 0.2) + geom_line(aes(colour = rank),
                                                                                                                      size = 1)

