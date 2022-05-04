library(ggplot2)
set.seed(2021)
coffee <- data.frame(grams = c(rnorm(12500, 12.5, 2), runif(7500, 10, 15)))
coffee$grams <- ifelse(coffee$grams < 8, 8, coffee$grams)
ggplot(coffee, aes(x = grams)) +
  geom_histogram(fill = 'cadetblue', bins = 50) +
  geom_vline(xintercept = mean(coffee$grams), color = 'gold') +
  labs(title = 'Distribution of Grams of Coffee Used Across All 20,000 Forum Members',
       y = 'Number of People', x = 'Grams of Coffee')
# Manually calculate population SD, as sd() function divides by n - 1 instead of n
pop_sd <- sqrt(sum((coffee$grams - mean(coffee$grams))^2) / nrow(coffee))
# Note that 12.52 and 0.18 are the rounded mean and SE
se <- pop_sd / sqrt(100)
lo <- mean(coffee$grams) - (1.96 * se)
hi <- mean(coffee$grams) + (1.96 * se)
interval <- c(lo, hi)
interval
## [1] 12.16489 12.87077

# Or, shortcut the steps above with:
# interval <- qnorm(c(.025, .975), mean = mean(coffee$grams), sd = (pop_sd / sqrt(100)))
