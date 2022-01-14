print('R for table join')
policies <- data.frame(Policy = c(1:9), State=c(rep("GA",3), rep("FL", 3), rep("AL", 3)), Limit=c(45060:45068))
policies

limits <- data.frame(State=c("FL","GA","AL"), regulatory_limit=c(40000,51000,62000))
limits

#Left Join
scored_policies<-merge(x=policies,y=limits,by="State",all.x=TRUE)
scored_policies

