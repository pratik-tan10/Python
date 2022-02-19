if (!file.exists("Downloads")){
  dir.create("Downloads")
}
dUrl <- "https://www2.census.gov/geo/tiger/TIGER2017/EDGES/tl_2017_01125_edges.zip"
download.file(dUrl, dfile = "tiger17.zip",method="curl")
dateDownloaded <- date()
tTable <- read.table("./data/census.csv", sep =",", header =TRUE)
head(tTable)
