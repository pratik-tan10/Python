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
library(leaflet.extras)

leaflet() %>%
  addTiles() %>% 
  addSearchOSM() %>% 
  addReverseSearchOSM() 
m2 <- ipeds %>% 
        leaflet() %>% 
            # use the CartoDB provider tile
            addProviderTiles("CartoDB") %>% 
            # center on the middle of the US with zoom of 3
            setView(lat = 39.8282, lng = -98.5795, zoom= 3)

# Map all American colleges 
m2 %>% 
    addCircleMarkers() 
pal <- colorFactor(palette = c("red", "blue", "#9b4a11"), 
                   levels = c("Public", "Private", "For-Profit"))

m2 %>% 
    addCircleMarkers(radius = 2, label = ~name, color = ~pal(sector_label))
# Load the htmltools package
library(htmltools)

# Create data frame called public with only public colleges
public <- filter(ipeds, sector_label == "Public")  

# Create a leaflet map of public colleges called m3 
m3 <- leaflet() %>% 
        addProviderTiles("CartoDB") %>% 
        addCircleMarkers(data = public, radius = 2, label = ~htmlEscape(name),
                         color = ~pal(sector_label), group = "Public")

m3
# Create data frame called private with only private colleges
private <- filter(ipeds, sector_label == "Private")  

# Add private colleges to `m3` as a new layer
m3 <- m3 %>% 
        addCircleMarkers(data = private, radius = 2, label = ~htmlEscape(name),
                         color = ~pal(sector_label), group = "Private") %>% 
        addLayersControl(overlayGroups = c("Public", "Private"))

m3
# Create data frame called profit with only For-Profit colleges
profit <- filter(ipeds, sector_label == "For-Profit")  

# Add For-Profit colleges to `m3` as a new layer
m3 <- m3 %>% 
        addCircleMarkers(data = profit, radius = 2, label = ~htmlEscape(name),
                         color = ~pal(sector_label),   group = "For-Profit")  %>% 
        addLayersControl(overlayGroups = c("Public", "Private", "For-Profit"))  

# Center the map on the middle of the US with a zoom of 4
m4 <- m3 %>%
        setView(lat = 39.8282, lng = -98.5795, zoom = 4) 
        
m4
