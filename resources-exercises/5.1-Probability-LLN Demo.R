# Data Sciences Institute Summer Course
# Module 5: Sampling
# Section 5.1: Probability
# Law of Large Numbers Demo
# Authored by Annie Collins

###########################

library(tidyverse)

# Suppose you are sampling students at a university with a population of 5000
# You want to determine the proportion of international students in the general student population
# Let 0 represent the outcome "domestic student" and 1 represent the outcome "international student"
# The university population consists of 25% statistics students and 75% non-statistics students
students <- sample(c(0, 1), 5000, replace = TRUE, prob = c(0.75, 0.25))

# Suppose we sample a student from the population and determine their domestic vs. international status
sample(students, 1)

# Suppose you sample students various numbers of students and then calculate the proportion of international students in each sample
# Notice how the proportion gets closer to 0.25 as the sample size increases
# n = 5
sample(students, 5) %>% mean()   # mean() returns the proportion of international students
# n = 10
sample(students, 10) %>% mean()
# n = 100
sample(students, 100) %>% mean()

# Suppose we sample 1500 students and calculate the proportion of international students after each new student is sampled and asked about their status
i <-0
n <- 1:1500
sample_students <- rep(NA, 1500)
prop_intl <- rep(NA, 1500)
while (i < 1500) {
  new_sample <- sample(students, 1)   # flip coin
  sample_students[i] <- new_sample          # add outcome of coin flip to vector of all coin sample_students
  prop_calc <- mean(sample_students, na.rm=TRUE)   # Calculate new proportion of heads (remove NA values from vector for calculation)
  prop_intl[i] <- prop_calc
  i <- i + 1
}

# Take a look at the results
student_data <- tibble(n = n, result = sample_students, prop_intl = prop_intl)
View(student_data)

# Plot the results
student_plot <- ggplot(data = student_data) + 
  geom_hline(aes(yintercept = 0.25, color = "r")) +
  geom_line(aes(x = n, y = prop_intl)) + 
  ylab("Cummulative proportion of international students") + 
  xlab("Number of students sampled")
student_plot
