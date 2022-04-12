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
