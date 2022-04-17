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

