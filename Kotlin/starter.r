boxplot(sample(3:14, sample(1:9,1), replace=TRUE),sample(1:8, sample(1:9,1), replace=TRUE), sample(3:100, sample(1:24,1), replace=TRUE), sample(3:100, sample(1:24,1), replace=TRUE),
main = "Multiple boxplots for comparision",
at = c(1,2,4,5),
names = c("L with c", "L without c", "S with c", "S without c"),
las =1 ,
col = c("red","yellow","green","lightblue"),
border = "brown",
horizontal = FALSE,
notch = FALSE,
xlab = 'Group',
ylab = 'Count'
)
