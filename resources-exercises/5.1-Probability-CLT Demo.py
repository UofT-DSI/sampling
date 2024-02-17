import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Setting the seed for reproducibility
np.random.seed(100)

# Suppose we have a population of 1000 people with uniformly distributed ages between 20 and 30 years old
ages = np.random.uniform(20, 30, 1000)

# Plotting the distribution of ages
sns.histplot(ages, kde=False)
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Distribution of Ages")
plt.show()

# We can calculate the mean age of the population, approximately 25 years old
mean_age_population = np.mean(ages)
print("Mean age of the population:", mean_age_population)

# Suppose we sample one individual from the population. Let random variable X represent the age of the person selected.
# Notice how this result varies between samples 
sample_one = np.random.choice(ages, 1)
print("Age of the sampled individual:", sample_one)

# Now suppose we sample 100 unique individuals from the population without replacement
# Each individual's age can be represented as a random variable X_1 through X_100
# We can calculate the mean of this sample to estimate the mean age of the population
# Notice how this result varies for different samples, but is generally fairly close to 25
sample_100 = np.random.choice(ages, 100, replace=False)
mean_sample_100 = np.mean(sample_100)
print("Mean age of 100 sampled individuals:", mean_sample_100)

def plot_mean_age_distribution(sample_size, num_samples, title):
    mean_ages = []
    # Graphs the mean age of <num_samples> different samples of <sample_size> individuals from our population.
    for _ in range(num_samples):
        sample = np.random.choice(ages, sample_size, replace=False)
        mean_ages.append(np.mean(sample))
    sns.histplot(mean_ages, kde=False)
    plt.xlabel("Mean Age")
    plt.ylabel("Count")
    plt.title(title)
    plt.show()

# And now let's plot the distribution of mean ages
# Notice the shape and the differnces between this histogram and the original age distribution
plot_mean_age_distribution(100, 100, "Distribution of Mean Ages for 100 Samples of Size 100")

# Repeat: 1000 samples of size 100
plot_mean_age_distribution(100, 1000, "Distribution of Mean Ages for 1000 Samples of Size 100")

# Repeat: 1000 samples of size 500
plot_mean_age_distribution(500, 1000, "Distribution of Mean Ages for 1000 Samples of Size 500")
