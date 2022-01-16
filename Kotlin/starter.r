print('R for table join')
policies <- data.frame(Policy = c(1:9), State=c(rep("GA",3), rep("FL", 3), rep("AL", 3)), Limit=c(45060:45068))
policies

limits <- data.frame(State=c("FL","GA","AL"), regulatory_limit=c(40000,51000,62000))
limits

#Left Join
scored_policies<-merge(x=policies,y=limits,by="State",all.x=TRUE)
scored_policies

#A query
which(scored_policies$Limit > scored_policies$regulatory_limit)
#Natural Join or natural join
df1 = data.frame(CountryId = c(1:6), Product = c("Netflix","Hulu","HBOMax","DisneyPlus","AppleTV","AmazonPrime"))
df2 = data.frame(CountryId = c(2, 4, 6, 7, 8), State = c("India","Bangladesh","China","Pakistan","Bhutan")) 
df = merge(x=df1,y=df2,by="CountryId")
df
#Inner Join using dplyr
library(dplyr)
df = df1%>%inner_join(df2, by="CountryId")
#Outer Join
df = merge(x=df1,y=df2,by="CountryId",all=TRUE)
#Left outer Join
df = merge(x=df1,y=df2,by="CountryId",all.x=TRUE)
#Right outer join
df = merge(x=df1,y=df2,by="CountryId",all.y=TRUE)

##To download Landsat Images in R
### run this chunk from the console - line-by-line
#   install.package("devtools")
#   devtools::install_github("16EAGLE/getSpatialData")
## Load packages
library(getSpatialData)
library(raster)
library(sf)
library(sp)
library(tidyverse)

## Use st_read function from the  sf library
regions <- st_read("./datos/Montes.geojson")

str(regions)
# texts and labels
p <- ggplot(regions) +
  geom_sf(aes(fill = MPIO_NAREA), colour="white")

p + geom_sf_label(aes(label = MPIO_CNMBR), colour = "black", size = 2.0)
montes <-
  regions %>%
  summarise(area = sum(MPIO_NAREA))

# setting a seed to make a random sample reproducible, choose any number you want
set.seed(65)

# with argument name, exact argument order
runif(n = 9, min = 3, max = 6)

set.seed(65)

# without argument name, exact argument order
runif(9, 3, 6)

set.seed(65)

# with argument name, mixed argument order
runif(min = 3, max = 6, n = 9)

set.seed(65)

# without argument name, mixed argument order
runif(3, 6, 9) # this means n=3, max=9

set.seed(65)

# using only the first argument
runif(3)

set.seed(65)

# using arguments 1 and 3
runif(3,,4)



