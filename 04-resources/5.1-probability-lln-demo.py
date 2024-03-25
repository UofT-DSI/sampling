# Data Sciences Institute
# Module 5: Sampling
# Section 5.1: Probability
# Law of Large Numbers Demo
# Authored by Annie Collins
# Converted to Python by Daniel Razavi

###########################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Suppose you are sampling students at a university with a population of 5000
# You want to determine the proportion of international students in the general student population
# Let 0 represent the outcome "domestic student" and 1 represent the outcome "international student"
# The university population consists of 25% statistics students and 75% non-statistics students
students = np.random.choice([0, 1], 5000, replace=True, p=[0.75, 0.25])

# Suppose we sample a student from the population and determine their domestic vs. international status
print(np.random.choice(students, 1))

# Suppose you sample students various numbers of students and then calculate the proportion of international students in each sample
# Notice how the proportion gets closer to 0.25 as the sample size increases
for n in [5, 10, 100]:
    print(np.mean(np.random.choice(students, n)))

# Suppose we sample 1500 students and calculate the proportion of international students after each new student is sampled and asked about their status
n = np.arange(1, 1501)
sample_students = np.empty(1500)
prop_intl = np.empty(1500)

for i in range(1500):
    new_sample = np.random.choice(students, 1)
    sample_students[i] = new_sample[0]  # Extract scalar value from the array
    prop_intl[i] = np.nanmean(sample_students[:i+1])  # Calculate new proportion of international students

# Take a look at the results
student_data = pd.DataFrame({'n': n, 'result': sample_students, 'prop_intl': prop_intl})
student_data.to_csv('student_data.csv', index=False)
print("student_data.csv file saved.")

# Plot the results
plt.axhline(y=0.25, color='r', linestyle='-')
plt.plot(student_data['n'], student_data['prop_intl'], label='Cumulative proportion of international students')
plt.ylabel('Cumulative proportion of international students')
plt.xlabel('Number of students sampled')
plt.legend()
plt.show()
