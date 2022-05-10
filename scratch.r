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
draw.board <- function(game) {
    xo <- c("X", " ", "O") # Symbols
    par(mar = rep(1,4))
    plot.new()
    plot.window(xlim = c(0,30), ylim = c(0,30))
    abline(h = c(10, 20), col="darkgrey", lwd = 4)
    abline(v = c(10, 20), col="darkgrey", lwd = 4)
    text(rep(c(5, 15, 25), 3), c(rep(25, 3), rep(15,3), rep(5, 3)), xo[game + 2], cex = 4)
    # Identify location of any three in a row
    square <- t(matrix(game, nrow = 3))
    hor <- abs(rowSums(square))
    if (any(hor == 3)) 
        hor <- (4 - which(hor == 3)) * 10 - 5 
    else 
        hor <- 0
    ver <- abs(colSums(square))
    if (any(ver == 3)) 
        ver <- which(ver == 3) * 10 - 5 
    else
        ver <- 0
    diag1 <- sum(diag(square))
    diag2 <- sum(diag(t(apply(square, 2, rev)))) 
    # Draw winning lines
    if (all(hor > 0)) 
        for (i in hor) lines(c(0, 30), rep(i, 2), lwd = 10, col="red")
    if (all(ver > 0)) 
        for (i in ver) lines(rep(i, 2), c(0, 30), lwd = 10, col="red")
    if (abs(diag1) == 3) 
        lines(c(2, 28), c(28, 2), lwd = 10, col = "red")
    if (abs(diag2) == 3) 
        lines(c(2, 28), c(2, 28), lwd = 10, col = "red")
}
  


