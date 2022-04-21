library(tidyverse)
library(caret)
library(nnet)
# Load the data
data("iris")
# Inspect the data
sample_n(iris, 3)
# Split the data into training and test set
set.seed(123)
training.samples <- iris$Species %>% 
  createDataPartition(p = 0.8, list = FALSE)
train.data  <- iris[training.samples, ]
test.data <- iris[-training.samples, ]

#################### without variable selection
modelx <- nnet::multinom(Species ~., data = train.data)
summary(modelx)

predicted.classes <- modelx %>% predict(test.data)
head(predicted.classes)
# Model accuracy
mean(predicted.classes == test.data$Species)

################## with variable selection
model <- nnet::multinom(Species ~., data = train.data)%>%
  stepAIC(trace = FALSE)
summary(model)

predicted.classes <- model %>% predict(test.data)
head(predicted.classes)
# Model accuracy
mean(predicted.classes == test.data$Species)
