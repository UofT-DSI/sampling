# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: NEDIM IGAL ERS BENVENISTE

```
Sampling Stages:

1) Infecting Individuals: 
Method: Simple random sampling without replacement
Function includes np.random
Sample Frame: 1000
Sample Size:  100
Each person has an equal probability of being infected

2) Primary Contact Tracing:
Method: Simple random sampling 
Function includes np.random
Sample Frame: Infected individuals
Sample Size: 20 percent of the frame

3) Secondary Contract Tracing:
Method: Cluster sampling, events treated as clusters
Function groups the sample into two events
Sample Frame: All event attendees
Sample Size: Depends on the results of the primary tracing step
Conditional probability
```

The graphs produced by the code are not similar to the ones from the blog post. In the blog post, the proportion of cases that result from weddings are overestimated (double the true proportion), whereas the distribution of the graphs produced by the code are closer, both peaking around 0.20 within a similar range.The red distribution does not spread as widely and does not shift as far right as in the original blog post. 

Rerunning the script 5 times after changing the no of reps to 100, I see a huge variation in the graphs - distribution and peak-wise. The results are not reproducible at all. 

Added a seed to the code (np.random.seed(42)) which solved the issue of lack of reproducibility. Ran the script 5 times again and the results are consistent. As suggested in the question, they don't match the results in the blog post. 

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
