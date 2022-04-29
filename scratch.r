a<-"C:/Users/12058/Desktop/dv.txt"
heading <- read.table("dv.txt",skip=36 header = TRUE, sep ="\t", stringsAsFactors = FALSE)
data<- read.table("dv.txt",header = TRUE, sep = "\t", stringsAsFactors = FALSE, skip = 37)
heading<- read.table("dv.txt",header = TRUE, sep = "\t", stringsAsFactors = FALSE, skip = 35, nrows=1)
nam<-c("agency_cd","site_np","dateime",	"gage_max",	"gage_max_cd",	"gage_mean",	"gage_mean_cd",	"tid_max",	"tid_max_cd",	"tid_min",	"tid_min_cd",	"tid_mean",	"tid_mean_cd",	"gage_min",	"gage_min_cd",	"vel_mean",	"vel_mean_cd",	"vel_min",	"vel_min_cd",	"vel_max",	"vel_max_cd")
colnames(data)<-nam
lm(vel_mean~gage_mean, data= data)->lmx
summary(lmx)
plot(lmx,pch=19,col="blue",chx = 2)
plot(tid_mean~gage_mean,pch=19,col="blue",chx = 2)
abline(lmx,col="green")

