#plotting with ggplot2
library(tidyverse)
summary(mpg)
head(mpg)
ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, color = class))
ggplot(data = mpg) + 
  geom_smooth(mapping = aes(x = displ, y = hwy, linetype = class, color = class))
