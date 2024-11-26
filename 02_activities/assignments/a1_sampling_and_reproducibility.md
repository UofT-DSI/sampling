# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Brandon Boateng

```
The code in whitby_covid_tracing.py simulates the process of contact tracing for COVID-19 and demonstrates how biases can emerge in the tracing data. Sampling occurs at several stages in the model. First, a random subset of individuals is infected with a 10% chance, using uniform random sampling from the population of event attendees. Next, primary contact tracing is applied, where a 20% chance of tracing an infected individual is assigned randomly, again using uniform random sampling. The third stage involves secondary contact tracing, where events with at least two traced individuals are identified, and all infected attendees at those events are traced deterministically, with no randomness involved. Finally, the model calculates the proportions of infections and traces attributed to each event type (wedding vs. brunch) based on the observed data. These sampling stages reflect the biased tracing process discussed in the blog post, where events like weddings, which are easier to trace due to their fixed guest lists, are overrepresented in the traced data, leading to an inflated perception of their role in the spread of infections. This mirrors the real-world bias in contact tracing, where easier-to-trace settings result in biased conclusions about the sources of outbreaks.

The sampling procedure in the code directly reflects the biased sampling described in the blog post, with primary and secondary contact tracing favoring easier-to-trace events (like weddings) over harder-to-trace settings (like brunches). The model simulates the process by overestimating the importance of weddings in the spread of infections due to the biases introduced by the sampling methods at each stage.

In summary, reducing the number of repetitions to 1,000 made the results more variable and less reproducible across multiple runs. While the general trend remained consistent, there is more fluctuation in the output due to the smaller sample size.

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
