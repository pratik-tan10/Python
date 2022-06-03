ui <- fluidPage(
  titlePanel("UFO Sightings"),
  sidebarPanel(
    selectInput("state", "Choose a U.S. state:", choices = unique(usa_ufo_sightings$state)),
    dateRangeInput("dates", "Choose a date range:",
      start = "1920-01-01",
      end = "1950-01-01"
    )
  ),
  # MODIFY CODE BELOW: Create a tab layout for the dashboard
  mainPanel(
    tabsetPanel(
      tabPanel("Plot", plotOutput("shapes")),
      tabPanel("Table", tableOutput("duration_table"))
    )
    
  )
)

server <- function(input, output) {
  output$shapes <- renderPlot({
    usa_ufo_sightings %>%
      filter(
        state == input$state,
        date_sighted >= input$dates[1],
        date_sighted <= input$dates[2]
      ) %>%
      ggplot(aes(shape)) +
      geom_bar() +
      labs(
        x = "Shape",
        y = "# Sighted"
      )
  })

  output$duration_table <- renderTable({
    usa_ufo_sightings %>%
      filter(
        state == input$state,
        date_sighted >= input$dates[1],
        date_sighted <= input$dates[2]
      ) %>%
      group_by(shape) %>%
      summarize(
        nb_sighted = n(),
        avg_duration_min = mean(duration_sec) / 60,
        median_duration_min = median(duration_sec) / 60,
        min_duration_min = min(duration_sec) / 60,
        max_duration_min = max(duration_sec) / 60
      )
  })
}

shinyApp(ui, server)
