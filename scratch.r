install.packages("rgdal");install.packages("RSQLite")
library(rgdal)
library(RSQLite)
dta <- src_sqlite("al_tuscaloosa.gpkg/al_tuscaloosa.gpkg") 
tbldata <- tbl(dta, "al_tuscaloosa") #Create a table from a data source
tbldf <- as.data.frame (tbldata) #Create a data frame
colnames(tbldf)
summary(tbldf[,-2])
apply(tbldf[,-2],2, function(x2) l-sum(is.na(x2)))->notNull
apply(tbldf[,-2],2, function(x2) sum(is.na(x2)))->SumNull
data.frame(notNull) ->notNulldf
data.frame(SumNull) ->sumNulldf
cbind(notNulldf,sumNulldf) ->exdf
save(exdf,file ="exdf.csv")
#-------------------------------
rv <- 1:10
rv2 <- 11:20

l <- list(a = rv, b = rv2) 
sapply(l, mean)
lapply(l, mean)
sapply(rv, function(f) f ^ 2)
