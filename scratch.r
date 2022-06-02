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
library(e1071)
#create vector to store accuracies and set random number seed
accuracy <- rep(NA, 100)
set.seed(2)

#calculate accuracies for 100 training/test partitions
for (i in 1:100){
    df[, "train"] <- ifelse(runif(nrow(df))<0.8, 1, 0)
    trainset <- df[df$train == 1, ]
    testset <- df[df$train == 0, ]
    trainColNum <- grep("train", names(trainset))
    trainset <- trainset[, -trainColNum]
    testset <- testset[, -trainColNum]
    svm_model<- svm(y ~ ., data = trainset, type = "C-classification", kernel = "polynomial", degree = 2)
    pred_test <- predict(svm_model, testset)
    accuracy[i] <- mean(pred_test == testset$y)
}

#print average accuracy and standard deviation
mean(accuracy)
sd(accuracy)
#transform data
df1 <- data.frame(x1sq = df$x1^2, x2sq = df$x2^2, y = df$y)

#plot data points in the transformed space
plot_transformed <- ggplot(data = df1, aes(x = x1sq, y = x2sq, color = y)) + 
    geom_point()+ guides(color = FALSE) + 
    scale_color_manual(values = c("red", "blue"))

#add decision boundary and visualize
plot_decision <- plot_transformed + geom_abline(slope = -1, intercept = 0.64)
plot_decision
svm_model<- 
    svm(y ~ ., data = trainset, type = "C-classification", 
        kernel = "polynomial", degree = 2)

#measure training and test accuracy
pred_train <- predict(svm_model, trainset)
mean(pred_train == trainset$y)
pred_test <- predict(svm_model, testset)
mean(pred_test == testset$y)

#plot
plot(svm_model, trainset)
#tune model
tune_out <- 
    tune.svm(x = trainset[, -3], y = trainset[, 3], 
             type = "C-classification", 
             kernel = "polynomial", degree = 2, cost = 10^(-1:2), 
             gamma = c(0.1, 1, 10), coef0 = c(0.1, 1, 10))

#list optimal values
tune_out$best.parameters$cost
tune_out$best.parameters$gamma
tune_out$best.parameters$coef0
#Build tuned model
svm_model <- svm(y~ ., data = trainset, type = "C-classification", 
                 kernel = "polynomial", degree = 2, 
                 cost = tune_out$best.parameters$cost, 
                 gamma = tune_out$best.parameters$gamma, 
                 coef0 = tune_out$best.parameters$coef0)

#Calculate training and test accuracies
pred_train <- predict(svm_model, trainset)
mean(pred_train == trainset$y)
pred_test <- predict(svm_model, testset)
mean(pred_test == testset$y)

#plot model
plot(svm_model, trainset)

