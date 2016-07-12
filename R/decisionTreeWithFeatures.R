rm(list = ls())
# Decision tree with one feature variable
age <- sample(1:70, 50, replace = TRUE)
label <- c('baby', 'child', 'teenager', 'adults')
age_label <- c()
for (value in age) {
  if (value <= 3) {
    age_label <- c(age_label, 'baby')
  } else if (value <= 13) {
    age_label <- c(age_label, 'child')
  }  else if (value <= 18) {
    age_label <- c(age_label, 'teenager')
  }  else  {
    age_label <- c(age_label, 'adults')
  }
} 

df <- data.frame('age' = age, 'label' = age_label)
print(head(df))
#Classification Tree with rpart
library(rpart)
library(rattle)

dc_model <- rpart(label~., data = df)

summary(dc_model) # detailed summary of splits
fancyRpartPlot(dc_model)

