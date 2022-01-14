print('R for table join')
policies <- data.frame(Policy = c(1:9), State=c(rep("GA",3), rep("FL", 3), rep("AL", 3)), Limit=c(45060:45068))
policies

limits <- data.frame(State=c("FL","GA","AL"), regulatory_limit=c(40000,51000,62000))
limits

#Left Join
scored_policies<-merge(x=policies,y=limits,by="State",all.x=TRUE)
scored_policies

#A query
which(scored_policies$Limit > scored_policies$regulatory_limit)
#Natural Join or natural join
df1 = data.frame(CountryId = c(1:6), Product = c("Netflix","Hulu","HBOMax","DisneyPlus","AppleTV","AmazonPrime"))
df2 = data.frame(CountryId = c(2, 4, 6, 7, 8), State = c("India","Bangladesh","China","Pakistan","Bhutan")) 
df = merge(x=df1,y=df2,by="CountryId")
df
#Inner Join using dplyr
library(dplyr)
df = df1%>%inner_join(df2, by="CountryId")
#Outer Join
df = merge(x=df1,y=df2,by="CountryId",all=TRUE)
#Left outer Join
df = merge(x=df1,y=df2,by="CountryId",all.x=TRUE)
#Right outer join
df = merge(x=df1,y=df2,by="CountryId",all.y=TRUE)



