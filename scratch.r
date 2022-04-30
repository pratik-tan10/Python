# Importing your data
dataset <- read.table(text='
    x   y
1   0 123
2   2 116
3   4 113
4  15 100
5  48  87
6  75  84
7 122  77', header=T)


y.hat <- predict(lm(y~x+I(x^2)+I(x^3), data=dataset)) 

qplot(x, y, data=dataset, geom="line") 
last_plot() + geom_line(aes(x=x, y=y.hat), col=2) 
lm(y~I+I(x^2)+I(x^3),data=dataset)

