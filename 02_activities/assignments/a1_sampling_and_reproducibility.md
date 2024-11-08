# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times


CARLOS ALBERTO FUENTES MONTES

```
I am going to split my answer in three important parts:

1. EXAMINING THE CODE:
The sampling procedure was made a subset of individuals that were randomly selected to be infected based on a predefined ATTACK_RATE, also among infected individuals, a random sample was chosen to be "traced" based on a tracing success rate defined by TRACE_SUCCESS and finally, secondary contact tracing. This step involves counting traced individuals within events (e.g., weddings or brunches) and then marking additional infections for tracing if a certain threshold (SECONDARY_TRACE_THRESHOLD) is met for an event type. 
The functions used were np.random.choice(), used to randomly select individuals for infection, based on the attack rate and np.random.rand(), used to perform a random sampling for tracing success among infected individuals, based on the TRACE_SUCCESS. The main function were simulate_event(m) that creates a DataFrame representing individuals attending weddings and brunches, infects a subset of them, performs primary and secondary contact tracing and calculates the proportions of infections and traced cases.
The sample size were 1000 individuals participating in the simulation, with 200 attendees for weddings and 800 for brunches. The sampling frame were of 1,000 individuals is split into these two event types. 
The initial infection stage uses a uniform distribution to randomly select a subset of individuals to be infected from the population attending events. Primary contact tracing is modeled by a Bernoulli process, where each infected individual has a TRACE_SUCCESS probability of being traced. This is represented by np.random.rand(), generating random values for each infected individual and comparing them to the tracing success probability.

2. RUN THE PYTHON SCRIPT:
Although it is challenging to make a direct comparison due to the lack of complete labels for the variables, X-axis, and Y-axis, we can observe that both graphs appear to approximate a normal distribution centered around 20%, with some variations around this value. Both distributions suggest that the majority of cases attributed to weddings cluster around this 20% mark, with some deviations on either side. Despite the differences in data presentation, the overall pattern seems consistent, indicating that weddings account for a similar central proportion in both models.

3. MODIFING NUMBER OF REPETITION (1000):
With each execution of the script, the output graph changes, showing variability in both the "Infections from Weddings" and "Traced to Weddings" distributions. These differences are reflected in the frequency and proportion of cases for each variable, indicating that the results are not fully reproducible. This lack of consistency suggests that randomness in the simulation affects the outcomes, leading to fluctuations in the proportions observed with each run.

4. ALTER THE CODE:
This is the change np.random.seed(42). After implementing the fixed seed, the graph produced by the script remains consistent across multiple executions. The distributions of "Infections from Weddings" and "Traced to Weddings" no longer shift with each run, making it possible to compare and analyze the output reliably.
```


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
