---
title: "Bike Shares Daily"
output: 
  flexdashboard::flex_dashboard:
    orientation: columns
    vertical_layout: fill
runtime: shiny
---

```{r global, include=FALSE}
library(flexdashboard)
library(readr)
library(leaflet)
library(DT)
library(tidyverse)
library(lubridate)
library(plotly)

trips_df <- read_csv('http://s3.amazonaws.com/assets.datacamp.com/production/course_6961/datasets/sanfran_bikeshare_joined_oneday.csv') %>%
  mutate(duration_min = duration_sec / 60,
         start_hour = hour(start_date)) %>%
  filter(duration_min <= 8 * 60) # remove trips longer than 8 hours as suspicious data quality

```



Column {data-width=200 .sidebar}
-----------------------------------------------------------------------

```{r}

sliderInput("start_slider", 
            label = "Select trip start times to display (hour of day):",
            min = 0, 
            max = 24, 
            value = c(7,10), 
            step = 1)

show_trips_df <- reactive({

  trips_df %>%
    filter(start_hour >= input$start_slider[1] &
             start_hour <= input$start_slider[2])

})

```

Column {data-width=450}
-----------------------------------------------------------------------
### Origins

```{r}

  renderLeaflet({show_trips_df() %>%
    rename(latitude = start_latitude,
           longitude = start_longitude) %>%
    group_by(start_station_id, latitude, longitude) %>%
    count() %>%
    leaflet() %>%
    addTiles() %>%
    addCircles(radius = ~n)})


```

Column {data-width=350}
-----------------------------------------------------------------------

### Total Trips

```{r}

valueBox(prettyNum(trips_df %>%
                     nrow(), big.mark = ','), 
         icon = 'fa-bicycle')


```

### Trips by Duration

```{r}

trips_df %>%
    ggplot(aes(x = duration_min)) +
    theme_bw() +
    xlab('Trip Duration (min) \n') +
    ylab('# trips') +
    geom_histogram() 

```


