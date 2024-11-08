# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Anca Kurian

```
Please write your explanation here...

```
Population: the community of 1000 people which, in a given time period, has attended exactly one event (one of the 2 weddings or one of the 80 brunches)
Frame population: the guests attending the events (200 wedding guests + 800 brunch attendees).
Sample population: 10% of attendees.

The sampling model applied is multi-stage model. The analysis starts with the participants being part of a stratum (the strata here are the events attended, where each individual traced can attend only one event). Up to this moment, the stratified sampling model has been applied, as part of the multi-stage sampling model. 
Once the strata are created, the simple random sampling is applied, where 10% of the attendees are selected as part of the sample population. All attendees have an equal chance of being infected, as the data is independent and identically distributed.

The graph from the original post is different than the one generated when running the code. The observed proportion and true proportion overlap greatly in the graph generated, while the graph in the original blog post shows the two observations being very different. The spread of the observed proportion is significantly higher than the spread of data in true proportion. 

When running the same code multiple times, the output is not identical. There is no parameter to ensure reproducibility. The graph maintains the general shape of the data, but the values vary slightly with each reiteration of the code.


A function is used for reproducibility of the script file (random.seed(42)).

# Run the simulation 1000 times
# Randomness function

import random

random.seed(42)
np.random.seed(42)

results = [simulate_event(m) for m in range(1000)]
props_df = pd.DataFrame(results, columns=["Infections", "Traces"])

Running the code multiple times gives the same plot each time. No values change anymore, unlike the code without the random state. 






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
