# install.packages("palmerpenguins")
library(palmerpenguins)

library(tidyverse)

dat <- penguins %>%
  select(species, flipper_length_mm)
summary(dat)
library(ggplot2)

ggplot(dat) +
  aes(x = species, y = flipper_length_mm, color = species) +
  geom_jitter() +
  theme(legend.position = "none")
res_aov <- aov(flipper_length_mm ~ species,
  data = dat
)
par(mfrow = c(1, 2)) # combine plots

# histogram
hist(res_aov$residuals)

# QQ-plot
library(car)
qqPlot(res_aov$residuals,
  id = FALSE # id = FALSE to remove point identification
)
shapiro.test(res_aov$residuals)
# Boxplot
boxplot(flipper_length_mm ~ species,
  data = dat
)
# Dotplot
library("lattice")

dotplot(flipper_length_mm ~ species,
  data = dat
)
# Levene's test
library(car)

leveneTest(flipper_length_mm ~ species,
  data = dat
)

par(mfrow = c(1, 2)) # combine plots

# 1. Homogeneity of variances
plot(res_aov, which = 3)

# 2. Normality
plot(res_aov, which = 2)
boxplot(flipper_length_mm ~ species,
  data = dat
)
boxplot(flipper_length_mm ~ species,
  data = dat
)
library(ggplot2)

ggplot(dat) +
  aes(x = species, y = flipper_length_mm) +
  geom_boxplot()

aggregate(flipper_length_mm ~ species,
  data = dat,
  function(x) round(c(mean = mean(x), sd = sd(x)), 2)
)
