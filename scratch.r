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

update(this_moment,hours=8,minutes=34,seconds=55)
update(this_moment, hours = 10, minutes = 16, seconds = 0)
this_moment
now(tzone= "America/New_York")->nyc
depart<- nyc+days(2)
depart<- update(depart, hours=17,minutes=34)
arrive<-depart + hours(15) + minutes(50)
with_tz(arrive,"Asia/Hong_Kong") ->arrive
mdy("June 17, 2008",tz="Singapore") -> last_time
interval(last_time,arrive)->how_long
as.period(how_long)
