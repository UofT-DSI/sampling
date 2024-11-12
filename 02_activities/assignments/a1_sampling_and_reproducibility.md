# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Brigitte Yan 

```
Examination of Sampling Procedures in whitby_covid_tracing.py


After diving into Andrew Whitby's blog post on how contact tracing can bias our understanding of COVID-19 case sources, I took a closer look at the whitby_covid_tracing.py script to see how it models this phenomenon.

Sampling Stages in the Model
The simulation involves several stages where sampling occurs:

Infection of Individuals

Function Used: np.random.choice
Sample Size: 10% of the total attendees (100 out of 1000 people).
Sampling Frame: All individuals attending the events (200 at weddings, 800 at brunches).
Process: Randomly selects 100 people to be infected, representing the spread of the virus among event-goers.
Relation to the Blog Post: This mirrors the initial infection spread discussed in the blog, highlighting how infections can occur randomly across different events.
Primary Contact Tracing

Function Used: np.random.rand compared with TRACE_SUCCESS
Sample Size: 20% of the infected individuals (approximately 20 people).
Sampling Frame: The group of infected individuals.
Process: Each infected person has a 20% chance of being traced through primary contact tracing, simulating real-world tracing effectiveness.
Relation to the Blog Post: Shows that not all infections are equally likely to be traced, which can introduce bias.
Secondary Contact Tracing

Process: Counts traced infections per event and identifies events with at least two traced cases.
Function Used: Event count comparison against SECONDARY_TRACE_THRESHOLD
Sampling Frame: Events where traced individuals were present.
Process: If an event has two or more traced cases, all infected attendees of that event are marked as traced.
Relation to the Blog Post: Demonstrates how events with more traced cases are more likely to have additional infections identified, skewing the perceived source of infections.
Calculating Proportions

Process: Computes the proportion of infections and traced cases attributed to weddings versus brunches.
Relation to the Blog Post: Directly relates to the analysis of how contact tracing can distort our understanding of where infections are coming from.
Comparing the Script's Output to the Blog Post
When I ran the script as it was (with 50,000 repetitions), the resulting graphs looked very similar to those in Whitby's blog. The histograms showed that weddings, despite having fewer actual infections, appeared to be the source of a higher proportion of traced cases. This aligns with the blog's point about contact tracing biasing our perception.

Observations with 1000 Repetitions
I then changed the number of repetitions in the simulation from 50,000 to 1,000 to see what would happen. Running the script multiple times, I noticed that the graphs varied with each run. The proportions of infections and traces attributed to weddings fluctuated, indicating that the results weren't reproducible with fewer repetitions due to the randomness in the simulation.

Making the Code Reproducible
To make the script produce the same results every time, I added a line to set the random seed:

python
Copy code
# Set the random seed for reproducibility
np.random.seed(10)
Why This Change Matters:

Random Seed Importance: By setting a seed with np.random.seed(10), we're ensuring that the random number generator produces the same sequence of numbers each time the script runs.
Effect on Reproducibility: With the seed set, all the random choices and probabilities in the simulation become consistent across runs, so the outputted graphs are identical every time.
Impact on the Script:

This change doesn't affect the logic or the outcomes of the simulation in terms of representing contact tracing bias; it simply makes the results consistent.
Now, when I run the script multiple times, I get the same graphs, which is helpful for analysis and presentation.
Conclusion
Through this exercise, I saw firsthand how sampling at different stages of a simulation can introduce biases similar to those in real-world data. By setting a random seed, I ensured that the results are reproducible, making it easier to study and communicate the effects demonstrated in the simulation.

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
