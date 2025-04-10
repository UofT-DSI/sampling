# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Maziar Farahzad

```
Please write your explanation here...

First sampling occurs when in the code `infected_indices` is defined, where a random subset of size 10 percent of the population is sampled without replacement. 
The population has a fixed distribution of 200 people attending weddings and 800 attending brunch. The 10 percent random sample is selected randomly from the total 1000 population irrespective of the 200|800 partition. 
In this initial step, the sampling frame is everyone in the population as they are all assumed to have a chance of getting infected. 
The associated code is: 
`# Infect a random subset of people
infected_indices = np.random.choice(ppl.index, size=int(len(ppl) * ATTACK_RATE), replace=False)
ppl.loc[infected_indices, 'infected'] = True`

Then, two stages of contact tracing occur.

The primary round then further samples from the infected population (from the sampling explained above, i.e. new sample size =100) in a particular way: first we assign a random number between 0 and 1 chosen uniformly to each infected individual. This is done to simulate the tracibility of each individual. This number can be interpreted as the chance of failure to trace an infected individual's infection to an event. There is a model parameter which is tracing success `TRACE_SUCCESS` and is set to 0.2. That is we are assuming that each infected individual's infection has a 20 percent chance of being traced back to an event. Then, if the random number assigned to each infected indivual is less than 20 percent, their infection can be traced. Otherwise, their infection cannot be traced. 

Therefore, in this step, the sampling frame is infected individuals.

The corresponding code for this step is `pl.loc[ppl['infected'], 'traced'] = np.random.rand(sum(ppl['infected'])) < TRACE_SUCCESS`.

The secondary round then looks at events with 2 or more infected indivduals in attendance, and then automatically everyone in that event is traced. There is really no sampling occoruing in this step of contact tracing, it is a determinsitic step. This happens in these lines of codes:

`# Secondary contact tracing based on event attendance
event_trace_counts = ppl[ppl['traced'] == True]['event'].value_counts()
events_traced = event_trace_counts[event_trace_counts >= SECONDARY_TRACE_THRESHOLD].index
ppl.loc[ppl['event'].isin(events_traced) & ppl['infected'], 'traced'] = True `





The results of running the code on my own does not agree with the one on the blog nor the code's result is reproducable on my computer. 

Changing the sample size from 1000 to 100 also does not help reproducibility. The variation among different resulting histograms is less than the case for sample size 1000 however. This is perhaps due to the fact that with a smaller sample size, there is less room for randomness. 

Overall, the case of 1000 sample size has mean closer to 0.2 (as expected) and a smaller variance compared to the case of 100 sample size. The case with 1000 sample size has the distribution of those infected from weddings and those traced to weddings closer to each other compared to the case of 100 samples, which has a lot of cases from the weddings while very few of them are traced back to the weddings.


By setting a random seed to be fixed, the output graphs are reproducable, since this way the randomness (really pseudo-randomness) is controlled, and in particular the same random samples are chosen in each step. 


```


## Criteria

|Criteria|Complete|Incomplete|
|--------|----|----|
|Altercation of the code|The code changes made, made it reproducible.|The code is still not reproducible.|
|Description of changes|The author explained the reasonings for the changes made well.|The author did not explain the reasonings for the changes made well.|

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 09/04/2025`
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
