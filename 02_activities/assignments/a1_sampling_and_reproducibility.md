# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Ferial Vahmiyan

```
In Whitby’s COVID-19 model code (whitby_covid_tracing.py), sampling occurs at several stages, representing the process of infections happening at events and the success of tracing those infections. Here’s a detailed breakdown of each sampling stage:

1. Sampling for Infections
Procedure: In the simulate_event() function, individuals attending events (weddings and brunches) are assigned infection statuses.
Function: np.random.choice is used to select infected individuals from a pool of attendees.
Sample Size: The sample size of infected people is determined by multiplying the total number of attendees (1,000 people across all events) by the attack rate (ATTACK_RATE = 0.10), meaning 10% (100 people) are randomly chosen to be infected.
Sampling Frame: All event attendees, with wedding and brunch attendees represented in the ppl DataFrame.
Distribution: A simple random sampling without replacement from the total attendee list, which aligns with the assumption in the blog post that infection rates are constant across events (10%).
2. Primary Contact Tracing Sampling
Procedure: After individuals are infected, primary contact tracing occurs. Here, infected individuals are sampled for successful tracing with a certain probability.
Function: np.random.rand creates random values for each infected individual, and those values are compared to the tracing success rate (TRACE_SUCCESS = 0.20), meaning each infected person has a 20% chance of being traced.
Sample Size: The sample size depends on the number of infected individuals, but on average 20% of the infected people (around 20 of the initial 100) will be successfully traced.
Sampling Frame: Only infected people, focusing tracing efforts on these individuals rather than the entire attendee pool.
Distribution: The primary contact tracing uses an independent Bernoulli process for each infected individual (each person has a 20% chance of being traced).
Relation to Blog Post: This is Whitby’s “primary contact tracing” stage, where only a fraction of cases are traced. This reflects real-world limitations in tracing resources and accuracy.
3. Secondary Contact Tracing Sampling
Procedure: If two or more individuals from the same event are traced in primary tracing, the entire event group is then traced. This is meant to represent intensified tracing efforts for events identified as having multiple infected cases.
Function: The function event_trace_counts[event_trace_counts >= SECONDARY_TRACE_THRESHOLD].index checks the count of cases traced to each event type (wedding or brunch). If an event reaches or exceeds a set threshold (defined as 2 people here), the model assumes all attendees of that event can be traced.
Sample Size: All infected individuals from “traced” events where the threshold was met. If, for example, a wedding has 2 or more traced cases, all attendees from that wedding are fully traced.
Sampling Frame: All infected attendees of events flagged by primary tracing as having 2 or more traced infections.
Distribution: This stage is deterministic for identified events, as all individuals at flagged events are fully traced. This mirrors the blog’s mention of “secondary contact tracing,” where some events (like weddings) become fully traceable based on an initial tracing success.
Summary
In Whitby’s model, the initial infection sampling represents random chance of infection across event types (weddings and brunches), primary contact tracing attempts to trace infections with a set success probability, and secondary contact tracing biases the sample by fully tracing events meeting a certain threshold of initial traced cases. This setup introduces sampling bias similar to that in real-world contact tracing, where certain event types become overrepresented in traced data due to differences in traceability, aligning with Whitby's main argument that observed case distributions may misrepresent true infection sources.

![image](https://github.com/user-attachments/assets/8068cf22-da6c-4867-8d0b-2a47c9c8b038)

The simulation with 50,000 iterations produced a histogram displaying the distribution of infection proportions traced to weddings versus brunches. The red distribution (traced cases) shows a higher average proportion of cases traced back to weddings compared to the actual proportion of infections originating there (blue distribution). This outcome aligns with the blog post’s conclusion: contact tracing can bias the sample by overestimating infections from easily traceable events like weddings. The shape and distribution closely resemble the blog post’s original graphs, confirming that this code effectively reproduces the intended bias effect. ​

![image](https://github.com/user-attachments/assets/e763af75-d226-4338-a0d8-54d26d60b2ba)
![image](https://github.com/user-attachments/assets/46e4f7eb-4072-45c7-830b-89b761297ce6)
![image](https://github.com/user-attachments/assets/e2b31d96-137c-4b9d-b550-d1f698dfd980)

Running the simulation multiple times with 1,000 iterations shows some variability in the output, indicating that the results are less stable with fewer repetitions. While each run still demonstrates the overall bias effect (i.e., higher proportions of cases traced to weddings than the actual infection rates), the shapes and peak positions of the histograms differ slightly between runs.

This variability suggests that reducing the iteration count to 1,000 diminishes the reproducibility of the results, as random fluctuations have a greater impact on the observed proportions. To achieve more consistent results, a higher number of iterations would be preferable, as seen in the more stable distributions from the original 50,000-iteration setup.

To make the simulation reproducible, the key change is to set a fixed random seed. Here’s how it would be done:

np.random.seed(seed + m)  # Using a different seed for each loop iteration

This adjustment ensures that each run produces the same results by controlling the random number generator, making output graphs consistent across executions. This does not necessarily match the original blog’s graph exactly but gives a stable reproduction of the model’s behavior. 




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
