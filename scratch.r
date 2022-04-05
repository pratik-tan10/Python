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


# Palette of 30 colors
library(RColorBrewer)
my_colors <- brewer.pal(9, "Reds") 
my_colors <- colorRampPalette(my_colors)(30)

# Attribute the appropriate color to each country
class_of_country <- cut(africa@data$POP2005, 30)
my_colors <- my_colors[as.numeric(class_of_country)]

# Make the plot
plot(africa , xlim=c(-20,60) , ylim=c(-40,40), col=my_colors ,  bg = "#A6CAE0")
