d1 <- Sys.Date()
class(d1)
unclass(d1)
d1
d2 <- as.Date("1969-01-01")
unclass(d2)
t1 <- Sys.time()
t1
class(t1)
unclass(t1)
t2 <-as.POSIXlt(Sys.time())
class(t2)
unclass(t2)
t2
str(unclass(t2))
t2$min
weekdays(d1)
months(t1)
quarters(t2)
t3 <- "October 17, 1986 08:24"
strptime(t3, "%B %d, %Y %H:%M") ->t4
t4
class(t4)
Sys.time() > t1
Sys.time()-t1
difftime(Sys.time(), t1, units = 'days')
