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
# Create data split object
loans_split <- initial_split(loans_df, 
                   strata = loan_default)

# Build training data
loans_training <- loans_split %>% 
  training()

# Build test data
loans_test <- loans_split %>% 
  testing()
dt_model <- decision_tree() %>% 
  # Specify the engine
  set_engine("rpart") %>% 
  # Specify the mode
  set_mode("classification")
# Create a workflow
loans_dt_wkfl <- workflow() %>% 
  # Include the model object
  add_model(dt_model) %>% 
  # Include the recipe object
  add_recipe(loans_recipe)

# Train the workflow
loans_dt_wkfl_fit <- loans_dt_wkfl %>% 
  last_fit(split = loans_split)

# Calculate performance metrics on test data
loans_dt_wkfl_fit %>% 
  collect_metrics()
# Create cross validation folds
set.seed(290)
loans_folds <- vfold_cv(loans_training, v = 5,
                       strata = loan_default)

# Create custom metrics function
loans_metrics <- metric_set(roc_auc, sens, spec)

# Fit resamples
loans_dt_rs <- loans_dt_wkfl %>% 
  fit_resamples(resamples = loans_folds,
                metrics = loans_metrics)

# View performance metrics
loans_dt_rs %>% 
  collect_metrics()

# Detailed cross validation results
dt_rs_results <- loans_dt_rs %>% 
  collect_metrics(summarize = FALSE)

# Explore model performance for decision tree
dt_rs_results %>% 
  group_by( .metric ) %>% 
  summarize(min = min(.estimate),
            median = median(.estimate),
            max = max(.estimate))
# Set tuning hyperparameters
dt_tune_model <- decision_tree(cost_complexity = tune(),
                               tree_depth = tune(),
                               min_n = tune()) %>% 
  # Specify engine
  set_engine('rpart') %>% 
  # Specify mode
  set_mode('classification')

# Create a tuning workflow
loans_tune_wkfl <- loans_dt_wkfl %>% 
  # Replace model
  update_model(dt_tune_model)

loans_tune_wkfl
# Hyperparameter tuning with grid search
set.seed(214)
dt_grid <- grid_random(parameters(dt_tune_model),
                       size = 5)

# Hyperparameter tuning
dt_tuning <- loans_tune_wkfl %>% 
  tune_grid(resamples = loans_folds,
            grid = dt_grid,
            metrics = loans_metrics)

# View results
dt_tuning %>% 
  collect_metrics()

# Collect detailed tuning results
dt_tuning_results <- dt_tuning %>% 
  collect_metrics(summarize = FALSE)

# Explore detailed ROC AUC results for each fold
dt_tuning_results %>% 
  filter(.metric == "roc_auc") %>% 
  group_by(id) %>% 
  summarize(min_roc_auc = min(.estimate),
            median_roc_auc = median(.estimate),
            max_roc_auc = max(.estimate))
# Display 5 best performing models
dt_tuning %>% 
  show_best(metric = 'roc_auc', n = 5)

# Select based on best performance
best_dt_model <- dt_tuning %>% 
  # Choose the best model based on roc_auc
  select_best(metric = 'roc_auc')

# Finalize your workflow
final_loans_wkfl <- loans_tune_wkfl %>% 
  finalize_workflow(best_dt_model)

final_loans_wkfl
# Train finalized decision tree workflow
loans_final_fit <- final_loans_wkfl %>% 
  last_fit(split = loans_split)

# View performance metrics
loans_final_fit %>% 
  collect_metrics()

# Create an ROC curve
loans_final_fit %>% 
  # Collect predictions
  collect_predictions() %>%
  # Calculate ROC curve metrics
  roc_curve(truth = loan_default, .pred_yes) %>%
  # Plot the ROC curve
  autoplot()
