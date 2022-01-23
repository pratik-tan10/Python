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

dummy <- tribble(
  ~name,        ~amount,
  "Rice",       5100,
  "Corn",       1623,
  "Soya",       1178,
  "Bean",       18453,
  "Wheat",      8181
)
#Changing default stat variable
ggplot(data = dummy) +
  geom_bar(mapping = aes(x = name, y = amount), stat = "identity")

#plotting summary of individual data subclass
ggplot(data = diamonds, mapping = aes(x = cut, y = depth)) + 
  stat_summary(
    fun.min = min,
    fun.max = max,
    fun = median, color = 'red')+
  stat_summary(fun=mean,color='green')

#colorful bar chart
ggplot(data = diamonds) + 
  geom_bar(mapping = aes(x = cut, fill = clarity))
