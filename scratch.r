library(data.table) df <- fread("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
df <- data.frame(df,header=TRUE,stringsAsFactors=FALSE)
library(dplyr)
df$Province.State <- sub("^$", NA, df$Province.State)
df <- transform(df, Province.State = ifelse(Province.State=="" | is.na(Province.State), Country.Region, Province.State))
#Replace all fields with 0 if the value is NA
df <- df %>% replace(.=="NA", 0) # replace with 0
df <- df[with(df, Country.Region %in% c("China","India","Pakistan","Iran")),]
dfCountryGroupSum <- aggregate(df[,c(5:ncol(df))],by=list(Category=df$Country.Region),FUN=sum)
head(dfCountryGroupSum[dfCountryGroupSum$Category=="China" ,c(1:5)])
# Category X1.22.2020 X1.23.2020 X1.24.2020 X1.25.2020
#28 China 548 643 920 1406
dfCountryGroupSum[dfCountryGroupSum$Category=="China" | dfCountryGroupSum$Category=="India",c(1:10)]
Category X1.22.20 X1.23.20 X1.24.20 X1.25.20 X1.26.20 X1.27.20 X1.28.20 X1.29.20 X1.30.20
37 China 548 643 920 1406 2075 2877 5509 6087 8141
80 India 0 0 0 0 0 0 0 0 1
head(dfCountryGroupSum[dfCountryGroupSum$Category %in% c("China","India"),c(1:5)])
