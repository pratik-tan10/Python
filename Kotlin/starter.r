#plotting with ggplot2
library(tidyverse)
summary(mpg)
head(mpg)
ggplot(data = mpg, mapping = aes(x=displ, y=hwy, color = drv))+
  geom_point(mapping = aes(shape = drv, alpha = (1-displ) ))+
  geom_smooth(mapping = aes(linetype=drv),se=FALSE)
ggplot(data = mpg, mapping = aes(x = displ, y = hwy)) + 
  geom_point(color = 'white', size=5)+
  geom_point(mapping=aes(color=drv))
