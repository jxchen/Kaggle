library("randomForest")

training <- read.csv("cs-training.csv")
RF <- randomForest(training[,-c(1,2,7,12)], training$SeriousDlqin2yrs,do.trace=TRUE,importance=TRUE,ntree=500,forest=TRUE)

test <- read.csv("cs-test.csv")

pred <- data.frame(predict(RF,test[,-c(1,2,7,12)]))
names(pred) <- "SeriousDlqin2yrs"

write.csv(pred,file="output2.csv")
