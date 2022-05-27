library(tidyr)
library(rgdal)
library(leaflet)
library(RColorBrewer)

shift <- function(x, lag) {
  n <- length(x)
  xnew <- rep(NA, n)
  if (lag < 0) {
    xnew[1:(n-abs(lag))] <- x[(abs(lag)+1):n]
  } else if (lag > 0) {
    xnew[(lag+1):n] <- x[1:(n-lag)]
  } else {
    xnew <- x
  }
  return(xnew)
}


f<-function(df,d=7){
  b<-0*seq_along(df$day)
  for (i in seq_along(df$day)){
    b[i]<-mean(df$cases[max(i-d+1,1):i])
  }
  plot(df$day,df$cases,type="l",col="blue",xlab = "date",ylab="Number of New Cases")
  points(df$day,b,type="l",col="red")
}


#Read Covid data
download.file("https://covid19.who.int/WHO-COVID-19-global-data.csv", destfile="WHO-COVID-19-global-data.csv")
mcsv<-read.csv("WHO-COVID-19-global-data.csv")

gather(mcsv,key="cases",value="number",-c(1:4))->mcsv2
spread(mcsv2,ï..Date_reported,number)->mcsv3

for (jj in (4+1:(dim(mcsv3)[2]-4))){
  if(jj==5) mm<-tapply(mcsv3[,jj],mcsv3$cases,sum)
  else mm<- cbind(mm,tapply(mcsv3[,jj],mcsv3$cases,sum))
}

Cumulative_cases<-subset(mcsv3, cases=="Cumulative_cases")
Cumulative_deaths<-subset(mcsv3, cases=="Cumulative_deaths")
New_cases<-subset(mcsv3, cases=="New_cases")
New_deaths<-subset(mcsv3, cases=="New_deaths")

covid_table<-function (v1){
  nco<-v1[1,5:dim(v1)[2]]
  apply(nco,2,sum)->ncw
  v1[nrow(v1) + 1,1:4] <- c("WD","World","All",deparse(substitute(v1)))
  v1[nrow(v1),5:dim(v1)[2]] <- ncw
  v1
}

Cumulative_cases<-covid_table(Cumulative_cases)
Cumulative_deaths<-covid_table(Cumulative_deaths)
New_cases<-covid_table(New_cases)
New_deaths<-covid_table(New_deaths)

# Download the countries shapefile 
download.file("http://thematicmapping.org/downloads/TM_WORLD_BORDERS_SIMPL-0.3.zip" , destfile="world_shape_file.zip")
system("unzip world_shape_file.zip")

# Read this shape file with the rgdal library. 
world_spdf <- readOGR( 
  dsn= paste0(getwd(),"/world_shape_file") , 
  layer="TM_WORLD_BORDERS_SIMPL-0.3",
  verbose=FALSE
)
#Get dataframe
world_spdf@data->world_spdf_data_copy
#Change colnames
colnames(world_spdf_data_copy)[2]<-colnames(New_cases)[1]

map_covid<-function(wdata, dframe,ddate){
  wdata@data->x
  colnames(x)[2]<-colnames(dframe)[1]
  wdata@data= x %>% left_join(dframe, by="Country_code")
  colnames(wdata@data)<-make.names(colnames(wdata@data))

  #Color Brewing
  partdata<-wdata@data[,make.names(ddate)]
  mybins<-as.integer(quantile(partdata[partdata>0],seq(0,1,length=6),na.rm=TRUE))
  y<-mybins[duplicated(mybins)]
  mybins<-c(y, mybins[!mybins %in% y])
  mypalette <- colorBin( palette="YlOrBr", domain=wdata@data[,make.names(ddate)], na.color="transparent", bins=mybins)
  
  #Prepare tooltip
  titl<-gsub("_"," ",deparse(substitute(dframe)))
  mytext <- paste(
    "Country: ", wdata@data$NAME,"<br/>", 
    "Area: ", wdata@data$AREA, "<br/>", 
    titl,": ", wdata@data[,make.names(ddate)], 
    sep="") %>%
    lapply(htmltools::HTML)
  
  print(titl)
  leaflet(wdata) %>% 
    addTiles()  %>% 
    setView( lat=10, lng=0 , zoom=2) %>%
    addPolygons( 
      fillColor = ~mypalette(partdata), 
      stroke=TRUE, 
      fillOpacity = 0.9, 
      color="white", 
      weight=0.3,
      label = mytext,
      labelOptions = labelOptions( 
        style = list("font-weight" = "normal", padding = "3px 8px"), 
        textsize = "13px", 
        direction = "auto"
      )
    ) %>%
    addLegend( pal=mypalette, values=as.integer(partdata), opacity=0.9, title = titl, position = "bottomleft" )
}

#Makemap
datalist<-list(New_cases=New_cases,Cumulative_deaths=Cumulative_deaths,New_deaths=New_deaths,Cumulative_cases=Cumulative_cases)

map_covid(world_spdf,Cumulative_cases,"2022-02-02")

#To convert valid colnames to date
as.Date(substring("X2020.01.02",2,11),"%Y.%m.%d")
t(mcsv3[5,5:dim(mcsv3)[2]])->ax3t
data.frame(day = as.Date(rownames(ax3t),"%Y-%m-%d"),cases=ax3t[,1])->ax3t
f(ax3t)

colnames(mcsv3)<-cn


##############################
# Compute the counts of all trees by hood
tree_counts <- count(trees, hood)

# Take a quick look
head(tree_counts)

# Remove the geometry
tree_counts_no_geom <- st_set_geometry(tree_counts, NULL)

# Rename the n variable to tree_cnt
tree_counts_renamed <- rename(tree_counts_no_geom, tree_cnt = n)
  
# Create histograms of the total counts
hist(tree_counts_renamed$tree_cnt)
# Compute areas and unclass
areas <- unclass(st_area(neighborhoods))

# Add the areas to the neighborhoods object
neighborhoods_area <- mutate(neighborhoods, area = areas)

# Join neighborhoods and counts
neighborhoods_counts <- left_join(neighborhoods_area, 
                            tree_counts_renamed, by = "hood")

# Replace NA values with 0
neighborhoods_counts <- mutate(neighborhoods_counts, 
                            tree_cnt = ifelse(is.na(tree_cnt), 
                                              0, tree_cnt))

# Compute the density
neighborhoods_counts <- mutate(neighborhoods_counts, 
                               tree_density = tree_cnt/area)
# Confirm that you have the neighborhood density results
head(neighborhoods)

# Transform the neighborhoods CRS to match the canopy layer
neighborhoods_crs <- st_transform(neighborhoods, crs = crs(canopy, asText = T))

# Convert neighborhoods object to a Spatial object
neighborhoods_sp <- as(neighborhoods_crs, "Spatial")

# Compute the mean of canopy values by neighborhood
canopy_neighborhoods <- extract(canopy, neighborhoods_sp, fun = mean)

# Add the mean canopy values to neighborhoods
neighborhoods_avg_canopy <- mutate(neighborhoods, avg_canopy = canopy_neighborhoods)
# Load the ggplot2 package
library(ggplot2)

# Create a histogram of tree density (tree_density)
ggplot(neighborhoods, aes(x = tree_density)) + 
  geom_histogram(color = "white")

# Create a histogram of average canopy (avg_canopy)
ggplot(neighborhoods, aes(x = avg_canopy)) + 
  geom_histogram(color = "white")

# Create a scatter plot of tree_density vs avg_canopy
ggplot(neighborhoods, aes(x = tree_density , y = avg_canopy)) + 
    geom_point() + 
    stat_smooth()

# Compute the correlation between density and canopy
cor(neighborhoods$tree_density, neighborhoods$avg_canopy)
# Plot the tree density with default colors
ggplot(neighborhoods) + 
  geom_sf(aes(fill = tree_density))

# Plot the tree canopy with default colors
ggplot(neighborhoods) + 
  geom_sf(aes(fill = avg_canopy))
  
# Plot the tree density using scale_fill_gradient()
ggplot(neighborhoods) + 
  geom_sf(aes(fill = tree_density)) + 
  scale_fill_gradient(low = "#edf8e9", high = "#005a32")

# Plot the tree canopy using the scale_fill_gradient()
ggplot(neighborhoods) + 
  geom_sf(aes(fill = avg_canopy)) +
  scale_fill_gradient(low = "#edf8e9", high = "#005a32")
