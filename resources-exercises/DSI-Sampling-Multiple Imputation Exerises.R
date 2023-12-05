install.packages("mice")
library(mice)
library(tidyverse)

# Load data
# Documentation: https://amices.org/mice/reference/mammalsleep.html
data("mammalsleep")
summary(mammalsleep)

# Missing data patterns
md.pattern(mammalsleep)

# Imputation
# Try other arguments for `method`, such as: "sample", "cart", "rf"
mammalsleep_imp <- mice(mammalsleep,
                        m = 5,
                        method = "pmm",
                        seed = 100)

# Summary of imputation process
summary(mammalsleep_imp)

# View imputed values
mammalsleep_imp$imp$ts
mammalsleep_imp$imp$mls
mammalsleep_imp$imp$gt
mammalsleep_imp$imp$ps
mammalsleep_imp$imp$sws

# View method
mammalsleep_imp$method

# Predict slow wave sleep (sws) using body weight (bw) and brain weight (brw)
# Calculates five separate linear regressions based on different imputed values
model1 <- with(mammalsleep_imp, lm(sws ~ bw + brw))
summary(model1)
# Average coefficient estimates from five models
model1_pooled <- pool(model1)
summary(model1_pooled)
# Compare with non-imputed model
model2 <- lm(sws ~ bw + brw, data = mammalsleep)
summary(model2)


