library(purrr)
library(rvest)
library(xml2)

mountain_wiki_pages<-c("https://en.wikipedia.org/w/index.php?title=Mount_Everest&oldid=958643874", "https://en.wikipedia.org/w/index.php?title=K2&oldid=956671989", "https://en.wikipedia.org/w/index.php?title=Kangchenjunga&oldid=957008408")
# Define a throttled read_html() function with a delay of 0.5s
read_html_delayed <- slowly(read_html, 
                            rate = rate_delay(0.5))
# Construct a loop that goes over all page urls
for(page_url in mountain_wiki_pages){
   # Read in the html of each URL with a delay of 0.5s
  html <- read_html_delayed(page_url)
  # Extract the name of the peak and its coordinates
  peak <- html %>% 
  	html_nodes("#firstHeading") %>% html_text()
  coords <- html %>% 
    html_nodes("#coordinates .geo-dms") %>% html_text()
  print(paste(peak, coords, sep = ": "))
}
