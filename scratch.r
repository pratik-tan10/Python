Sys.getlocale("LC_TIME")
this_day<-today()
this_day
day(this_day)
wday(this_day,label=TRUE)
now()-> this_moment
this_moment
hour(this_moment)
ymd("1989-05-17")->my_date
my_date
class(my_date)
ymd("1989 May 17")
mdy("March 12, 1975")
dmy(25081985)
ymd("1920/1/2")
ymd_hms(dt1)
hms("03:22:14")
ymd(dt2)
