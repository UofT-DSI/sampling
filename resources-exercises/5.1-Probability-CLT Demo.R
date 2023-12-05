# Data Sciences Institute Summer Course
# Module 5: Sampling
# Section 5.1: Probability
# Central Limit Theorem Demo
# Authored by Annie Collins

###########################

library(tidyverse)

# Suppose we have a population of 1000 people with uniformly distributed ages between 20 and 30 years old
set.seed(100)
ages <- runif(1000, min = 20, max = 30)
ages
ggplot() + geom_histogram(aes(x = ages)) + xlab("Age") + ylab("Count") + theme_minimal()

# We can calculate the mean age of the population, approximately 25 years old
mean(ages)

# Suppose we sample one individual from the population. Let random variable X represent the age of the person selected.
# Notice how this result varies between samples
sample(ages, 1)

# Now suppose we sample 100 unique individuals from the population without replacement
# Each individual's age can be represented as a random variable X_1 through X_100
# We can calculate the mean of this sample to estimate the mean age of the population
# Notice how this result varies for different samples, but is generally fairly close to 25
sample(ages, 100) %>% mean()

# Now let's graph the mean age of 100 different samples of 100 individuals from out population.
i <- 0
mean_ages_100 <- rep(NA, 100)
while (i < 100) {
  sample <- sample(ages, 100)
  mean_ages_100[i] <- mean(sample)
  i <- i + 1
}

# And now let's plot the distribution of mean ages
# Notice the shape and the differnces between this histogram and the original age distribution
plot_mean_age_100 <- ggplot() + geom_histogram(aes(x = mean_ages_100)) + xlab("Mean age for sample size of 100, with 100 samples") + ylab("Count") + theme_minimal()
plot_mean_age_100

# Repeat: 1000 samples of size 100
i <- 0
mean_ages_1000 <- rep(NA, 1000)
while (i < 1000) {
  sample <- sample(ages, 100)
  mean_ages_1000[i] <- mean(sample)
  i <- i + 1
}
plot_mean_age_1000 <- ggplot() + geom_histogram(aes(x = mean_ages_1000)) + xlab("Mean age for sample size of 100, with 1000 samples") + ylab("Count") + theme_minimal()
plot_mean_age_1000

# Repeat: 1000 samples of size 500
i <- 0
mean_ages_500 <- rep(NA, 1000)
while (i < 1000) {
  sample <- sample(ages, 500)
  mean_ages_500[i] <- mean(sample)
  i <- i + 1
}
plot_mean_age_500 <- ggplot() + geom_histogram(aes(x = mean_ages_500)) + xlab("Mean age for sample size of 500, with 1000 samples") + ylab("Count") + theme_minimal()
plot_mean_age_500