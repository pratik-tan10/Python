# Download the shapefile. (note that I store it in a folder called DATA. You have to change that if needed.)
download.file("http://thematicmapping.org/downloads/TM_WORLD_BORDERS_SIMPL-0.3.zip" , destfile="world_shape_file.zip")
# You now have it in your current working directory, have a look!

# Unzip this file. You can do it with R (as below), or clicking on the object you downloaded.
system("unzip world_shape_file.zip")
#  -- > You now have 4 files. One of these files is a .shp file! (TM_WORLD_BORDERS_SIMPL-0.3.shp)

# Read this shape file with the rgdal library. 
library(rgdal)
my_spdf <- readOGR( 
  dsn= paste0(getwd(),"/world_shape_file") , 
  layer="TM_WORLD_BORDERS_SIMPL-0.3",
  verbose=FALSE
)

# Select Africa only
africa <- my_spdf[my_spdf@data$REGION==2 , ]
plot(my_spdf[my_spdf@data$REGION==150,])

# -- > Now you have a Spdf object (spatial polygon data frame). You can start doing maps!

# Plot
plot(africa , xlim=c(-20,60) , ylim=c(-40,40))
# library
library(dplyr)
library(ggplot2)

# Make sure the variable you are studying is numeric
africa@data$POP2005 <- as.numeric( africa@data$POP2005 )

# Distribution of the population per country?
africa@data %>% 
  ggplot( aes(x=as.numeric(POP2005))) + 
  geom_histogram(bins=20, fill='#69b3a2', color='white')
