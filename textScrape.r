# Load VIM
library(VIM)

# Draw a combined aggregation plot of africa
africa %>%
  aggr(combined = TRUE, numbers = TRUE)

# Draw a spine plot of country vs trade
africa %>% 
  select(country, trade) %>%
  spineMiss()
# Load mice
library(mice)

# Impute africa with mice
africa_multiimp <- mice(africa, m = 5, defaultMethod = "cart", seed = 3108)

# Draw a stripplot of gdp_pc versus trade
stripplot(africa_multiimp, gdp_pc ~ trade | .imp, pch = 20, cex = 2)
# Fit linear regression to each imputed data set
lm_multiimp <- with(africa_multiimp, lm(gdp_pc ~ country + year + trade + infl + civlib))

# Pool regression results
lm_pooled <- pool(lm_multiimp)

# Summarize pooled results
summary(lm_pooled, conf.int = TRUE, conf.level = 0.90)
