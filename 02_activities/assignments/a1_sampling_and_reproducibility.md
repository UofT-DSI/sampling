# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model (complete). Describe in words the sampling procedure, referencing the functions used(complete), sample size(complete), sampling frame(complete), any underlying distributions involved (complete), and how these relate to the procedure outlined in the blog post (done).

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post? (complete)

Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results. (complete)

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times (complete)

# Author: Lauren Mulders

```
Please write your explanation here...
**Sampling Procedure**
    Each stage has a different frame (the group of people being considered), and the sample sizes and distributions change accordingly.

    1. Infection Sampling: Randomly selects 10% of the people at the events to be infected. The sample size is fixed at around 100 people.
    2.  Primary Contact Tracing: Traces 20% of the infected people (using a random process for each infected individual).
    3. Secondary Contact Tracing: If 2 or more traced individuals are at the same event, everyone infected at that event is traced, expanding the sample size dynamically based on event rules.

**Sampling Stages**
 1. Infection Sampling
    Frame: The frame are the people that attended the events -> 1000 people, broken up into 200 that attended weddings and 800 that attended brunch
    
    Sample size: 10% of attendees (200 wedding, 800 brunch) are randomly infected using ATTACK_RATE. Expected sample size = 100
    
    Distribution: The infection assignment follows a binomial-like distribution, where each individual has a fixed probability 10% of being infected.

    Function Used: numpy.random.choice()

    Sampling Procedure Relatve to the blogpost: Both Whitby's and DSI's infection sampling process is random, but could introduce some biases depending on how people are infected and how infectious they are. For example, individuals at weddings might be more closely connected (more potential contacts) than those at brunch, leading to potentially different infection rates. This introduces a social bias where the event type could affect infection rates and bias the results.


2.  Primary Contact Tracing
    Frame: the expected 100 infected people
    
    Sample size: The expected sample size is around 20 individuals, based on the TRACE_SUCCESS of 20%
    
    Distribution: The tracing process follows a binomial-like distribution, where each infected individual has a 20% chance of being traced. 

    Fucntion Used: Function Used: numpy.random.rand()

    Sampling Procedure Relatve to the blogpost: The random tracing mechanism could introduce bias toward people who are more likely to seek testing (those with more visible symptoms) or who attend certain events. In Whitby's work, and in DSI's testing, bias is a concern, it might prioritize individuals who are more symptomatic or otherwise more likely to be traced. 


3.  Secondary Tracing
    Frame: The traced people from primary tracing ~20 people

    Sample Size: The sample size expands based on the event-level rules: If there are ≥2 traced individuals at an event, all infected individuals at that event will also be traced. The sample size here varies based on event clustering and the threshold rule.
    
    Distribution: secondary tracing process is conditional on event-level aggregation and thus introduces dependencies, leading to a grouped/binomial-like distribution for traced cases.

    function Used: Pandas filtering + event-based logic
    
    Sampling Procedure Relatve to the blogpost: Secondary tracing could introduce event-based bias. If an event has multiple traced individuals (e.g., a wedding), the secondary tracing rule triggers, and all infected people at that event are traced. However, if an event has fewer traced individuals, secondary tracing may miss them, leaving a potential event-type bias. This clustering effect can over-represent cases from larger events, like weddings, and under-represent cases from smaller events, creating a skew in the sample. Both DSI's and Whitby contain these event-based biases.



#  Does this code appear to reproduce the graphs from the original blog post?

    No, it doesnt.  In the blog post, there is a wider spread. In the blog "observed proportions" tend to center around 50%, rather than in the DSI's graph where it centers at 20%.


# Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.
    
    Given that randomness plays a significant role in each of the sampling stages, there is variance in the results when the code is run and graphed. Without setting a fixed random seed, the script will produce different outputs each time it is executed, impacting reproducibility.
    

# Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

    Reducing the repetitions from 1000 to 100 results in fewer data points, increasing variability in the distributions. The graphs will be more affected by noise, with larger fluctuations due to the smaller sample size. The histograms will appear less stable, with patterns changing significantly between outputs.


# Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

    Setting a Fixed Random Seed: I added the line np.random.seed(42) at the beginning of the script. This sets the seed for NumPy's random number generator, ensuring that the random choices and random numbers generated by the simulation will be the same each time the script is executed.

```


## Criteria

|Criteria|Complete|Incomplete|
|--------|----|----|
|Altercation of the code|The code changes made, made it reproducible.|The code is still not reproducible.|
|Description of changes|The author explained the reasonings for the changes made well.|The author did not explain the reasonings for the changes made well.|

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 16/02/2025`
* The branch name for your repo should be: `assignment-1`
* What to submit for this assignment:
    * This markdown file (a1_sampling_and_reproducibility.md) should be populated.
    * The `whitby_covid_tracing.py` should be changed.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/sampling/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-1`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via the help channel in Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
