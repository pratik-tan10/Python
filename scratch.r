library(shiny)
library(leaflet)

inputPanel(actionButton
(inputId="resetMap",
	label="Reset view", 
	style="color: #fff; background-color: #990000; border-style: solid; border-color: #999999; margin: 5px")
	 )

leafletOutput("londonMap",
	height=600,
	width="100%")

output$londonMap <- renderLeaflet({
theMap <- leaflet(options = leafletOptions(zoomSnap=0.1)) %>%
addTiles() %>%
setView(lng=-0.128034, lat=51.508047, zoom = 12) %>% 
addMarkers(lng=-0.128034, lat=51.508047,popup="Trafalgar Square, London") 
})

observeEvent(input$resetMap, 
	{leafletProxy("londonMap") %>%
setView(lng=-0.128034, lat=51.508047, zoom = 12)
})
