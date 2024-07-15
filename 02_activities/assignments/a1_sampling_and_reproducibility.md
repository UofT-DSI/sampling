# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Yinglin Zhang

```
Please write your explanation here...
The blog post by Andrew Whitby discussess how contact tracing can result in a biased sample of Covid-19 cases. The primary idea is that contact tracing tends to identy clusters of infections, which can mislead certain types of cases and others.

Sampling procedures in the code
1. Initialization of Population:
Fuction: simulate_event()
Sample Size: 50000 individuals (10000 at weddings and 40000 at brunches)
Sample Frame: General population attending these events

2. Infection Process
Function: simulate_event()
Producure: Randomly infects 10% of the population
Sample Size: 500 individuals(10% of 50000)
Distribution: Uniform random selection from the population

3. Primary Contact Tracing:
Function: simulate_event()
Procedure: Randomly traces 20% of the infected individuals
Sample Size: Around 10000 individuals (20% of 50000)
Distribution: Bernoulli distribution with success probability of 0.2

4. Secondary Contact Tracing:
Function: simulate_event()
Procedure: Traces all infected individuals at events with at least two traced cases
Sample Size: Varibale, depending on primary tracing outcomes
Distribution: Conditional on primary tracing results

Relationship to Blog post
The code simulates contact tracing scenarios, illustrating biases where events with structured guest lists, such as weddings, are more traceable than casual gatherings like brunches. This results in data overestimating the impact of easily traceable events due to biased sampling, amplified through secondary tracing steps in the simulation.

The ovservation is similar.

The observation from 50000 to 1000 is and should be the same. However while reducing the number of repetitions to 1000 may provide more variability in the simulation results. 

Here are the changes can be made to the code to have reproducible results:
Using random Model.

Impact: Consistency and verfication






## Criteria

|Criteria|Complete|Incomplete|
|--------|----|----|
|Altercation of the code|The code changes made, made it reproducible.|The code is still not reproducible.|
|Description of changes|The author explained the reasonings for the changes made well.|The author did not explain the reasonings for the changes made well.|

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `HH:MM AM/PM - DD/MM/YYYY`
* The branch name for your repo should be: `sampling-and-reproducibility`
* What to submit for this assignment:
    * This markdown file (sampling_and_reproducibility.md) should be populated.
    * The `whitby_covid_tracing.py` should be changed.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/sampling/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `sampling-and-reproducibility`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack at `#cohort-3-help`. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
