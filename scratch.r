read.csv(path2csv, stringsAsFactors =  FALSE) -> mydf
dim(mydf)
head(mydf)
library(dplyr)
packageVersion("dplyr")
cran <- tbl_df(mydf)
rm("mydf")
cran
select(cran, ip_id, package,country)
select(cran, r_arch:country)
select(cran, country:r_arch)
select(cran, -time)
-(5:20)
select(cran, -(X:size))
filter(cran, package == "swirl")
filter(cran, r_version=="3.1.1", country=="US")
filter(cran, r_version<="3.0.2", country=="IN")
filter(cran, country == "IN" | country=="US")
filter(cran, size>100500, r_os == "linux-gnu")


filter(cran, !is.na(r_version))
select(cran,size:ip_id) ->cran2
arrange(cran2, ip_id)
arrange(cran2, desc(ip_id))
arrange(cran2, package, ip_id)
arrange(cran2, country, desc(r_version), ip_id)

select(cran, ip_id, package, size) -> cran3
cran3
mutate(cran3, size_mb = size/2^20, size_gb = size_mb/2^10)
mutate(cran3, correct_size= size+1000)
summarize(cran, avg_bytes = mean(size))
