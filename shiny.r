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

trips_df <- read_csv('https://assets.datacamp.com/production/repositories/1448/datasets/1f12031000b09ad096880bceb61f6ca2fd95e2eb/sanfran_bikeshare_joined_oneday.csv') %>%
  mutate(duration_min = duration_sec / 60)

```

Global Sidebar {.sidebar}
====================

Column {data-width=200 .sidebar}
-----------------------------------------------------------------------

```{r}

sliderInput("duration_slider", label = "Select maximum trip duration to display (in minutes):",
            min = 0, max = 120, value = 15, step = 5, dragRange = TRUE)

sliderInput("duration_bin", label = "Select # of minutes to bin trip durations:",
           min = 1, max = 15, value = 1, step = 1)

show_trips_df <- reactive({

  trips_df %>%
    filter(duration_sec <= input$duration_slider * 60)

})
```

Column {data-width=450}
-----------------------------------------------------------------------

### Origins

```{r}

renderLeaflet({
  show_trips_df() %>%
    rename(latitude = start_latitude,
           longitude = start_longitude) %>%
    group_by(start_station_id, latitude, longitude) %>%
    count() %>%
    leaflet() %>%
    addTiles() %>%
    addCircles(radius = ~n)
})

```


Column {data-width=350}
-----------------------------------------------------------------------

### Total Trips

```{r}

renderValueBox({
  valueBox(prettyNum(show_trips_df() %>%
                       nrow(), big.mark = ','), 
           icon = 'fa-bicycle')
})

```

### Trips by Start Time

```{r}

renderPlot({show_trips_df() %>%
    mutate(hour = hour(start_date)) %>%
    group_by(hour) %>%
    summarize(`Trips Started` = n()) %>%
    ggplot(aes(x = hour, y = `Trips Started`)) +
    theme_bw() +
    ylab('Trips Started \n') +
    geom_bar(stat = 'identity') 
})

```

Duration
====================

### Trip Durations

```{r}

renderPlot({show_trips_df() %>%
  mutate(`Trip Duration (min)` = duration_sec / 60) %>%
  ggplot(aes(x = `Trip Duration (min)`)) +
  theme_bw() +
  geom_histogram(binwidth = input$duration_bin) +
  ylab('# Trips')
})

```
