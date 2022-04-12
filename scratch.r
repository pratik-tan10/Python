library(shiny)
library(leaflet)
library(shinydashboard)
ui<-dashboardPage(
  dashboardHeader(
    title="My Dashboard",
    dropdownMenuOutput("messageMenu"),
    dropdownMenu(type = "notifications",
      notificationItem(
       text = "5 new users today",
       icon("users")
      ),
      notificationItem(
       text = "12 items delivered",
       icon("truck"),
       status = "success"
      ),
      notificationItem(
       text = "Server load at 86%",
       icon = icon("exclamation-triangle"),
       status = "warning"
      )
    ),
    dropdownMenu(type = "tasks", badgeStatus = "success",
      taskItem(value = 90, color = "green",
              "Documentation"
      ),
      taskItem(value = 17, color = "aqua",
              "Project X"
      ),
      taskItem(value = 75, color = "yellow",
              "Server deployment"
      ),
      taskItem(value = 80, color = "red",
              "Overall project"
      )
    )
  ),
  dashboardSidebar(
    sidebarMenu(id="sidebar",
      menuItem("Dashboard",tabName="dashboard",icon=icon("dashboard")),
      menuItem("Widgets",tabName="widgets",icon=icon("th")),
      menuItem("Connect", icon = icon("fa-brands fa-linkedin"), 
               href = "https://www.linkedin.com/in/pratik-dhungana-452951228/")
    )
  ),
  dashboardBody(
    tabItems(
      tabItem(tabName="dashboard",
        fluidRow(
          box(title="Histogram",background = "navy", solidHeader=TRUE,collapsible=TRUE,plotOutput("plot1",height=250)),
          box(
            title="Inputs",status="danger",background="black", solidHeader=TRUE,collapsible=TRUE,
            sliderInput("slider","Number of observations:", 1,100,50),
            textInput("text","Text Input:")
          )
        ),
        fluidRow(
          div(leafletOutput("mymap"),style='border: 4px solid black'),
          p(),
          actionButton("recalc", "New points"
        )
      )
    ),
      tabItem(tabName="widgets",
        h2("Widgets tab content"),
        fluidRow(
          box(
            title="file input",
            fileInput(
              "file1",
              "Choose a csv file",
              accept = ".csv",
            )
          ),
          box(title="Rendered table",
            tableOutput("contents")    
          )
        )
      )
    )
  )
)

#33333333333

# Download the shapefile. (note that I store it in a folder called DATA. You have to change that if needed.)
download.file("http://thematicmapping.org/downloads/TM_WORLD_BORDERS_SIMPL-0.3.zip" , destfile="world_shape_file.zip")
# You now have it in your current working directory, have a look!

# Unzip this file. You can do it with R (as below), or clicking on the object you downloaded.
system("unzip world_shape_file.zip")
#  -- > You now have 4 files. One of these files is a .shp file! (TM_WORLD_BORDERS_SIMPL-0.3.shp)

# Read this shape file with the rgdal library. 
library(rgdal)
world_spdf <- readOGR( 
  dsn= path.expand(paste0(getwd(),"/world_shape_file")) , 
  layer="TM_WORLD_BORDERS_SIMPL-0.3",
  verbose=FALSE
)

# Clean the data object
library(dplyr)
world_spdf@data$POP2005[ which(world_spdf@data$POP2005 == 0)] = NA
world_spdf@data$POP2005 <- as.numeric(as.character(world_spdf@data$POP2005)) / 1000000 %>% round(2)

# -- > Now you have a Spdf object (spatial polygon data frame). You can start doing maps!

# Library
library(leaflet)

# Create a color palette for the map:
mypalette <- colorNumeric( palette="viridis", domain=world_spdf@data$POP2005, na.color="transparent")
mypalette(c(45,43))

# Create a color palette with handmade bins.
library(RColorBrewer)
mybins <- c(0,10,20,50,100,500,Inf)
mypalette <- colorBin( palette="YlOrBr", domain=world_spdf@data$POP2005, na.color="transparent", bins=mybins)

# Prepare the text for tooltips:
mytext <- paste(
  "Country: ", world_spdf@data$NAME,"<br/>", 
  "Area: ", world_spdf@data$AREA, "<br/>", 
  "Population: ", round(world_spdf@data$POP2005, 2), 
  sep="") %>%
  lapply(htmltools::HTML)

# Final Map
m<-leaflet(world_spdf) %>% 
  addTiles()  %>% 
  setView( lat=10, lng=0 , zoom=2) %>%
  addPolygons( 
    fillColor = ~mypalette(POP2005), 
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
  addLegend( pal=mypalette, values=~POP2005, opacity=0.9, title = "Population (M)", position = "bottomleft" )


#33333333333


server<-function(input,output,session){
  set.seed(122)
  histdata<- rnorm(500)
  messageData<-data.frame(from=c("Sales Dept","New User","Support"),message=c("Sales are steady this month.","How do I register?","The new servers are ready."))
  
  output$plot1<-renderPlot({
      data<-histdata[seq_len(input$slider)]
      hist(data)
    })
  output$messageMenu <- renderMenu({
    # Code to generate each of the messageItems here, in a list. This assumes
    # that messageData is a data frame with two columns, 'from' and 'message'.
    msgs <- apply(messageData, 1, function(row) {
      messageItem(from = row[["from"]], message = row[["message"]])
    })
    
    # This is equivalent to calling:
    #   dropdownMenu(type="messages", msgs[[1]], msgs[[2]], ...)
    dropdownMenu(type = "messages", .list = msgs)
  })
  output$contents <- renderTable({
    file <- input$file1
    ext <- tools::file_ext(file$datapath)
    
    req(file)
    validate(need(ext == "csv", "Please upload a .csv file"))
    
    read.csv(file$datapath, header = input$header)
  })
  points <- eventReactive(input$recalc, {
    cbind(rnorm(40) * 2 + 84, rnorm(40) + 27)
  }, ignoreNULL = FALSE)
  
  #output$mymap <- renderLeaflet({
   # leaflet() %>%
    #  addProviderTiles(providers$Stamen.TonerLite,
     #                  options = providerTileOptions(noWrap = TRUE)
      #) %>%
      #addMarkers(data=points(), label=rep(paste("this point is :",rnorm(1)),40))
  #})
  output$mymap <- renderLeaflet({m})
}

shinyApp(ui,server)
