# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Danica Leung

```
Please write your explanation here...

### Stages of Sampling:
The first stage of sampling for our simple model is when the population is defined as 1000 people over a single time period. These 1000 people are broken down to 100 people attending wedding 1 and 100 people attending wedding 2 (total 200 people), and a total of 80 brunches each with 10 attendees (total 800 people). The line of code used to define this is `events = ['wedding'] * 200 + ['brunch'] * 800`. This target population becomes the basis in which we simulate 10% of people at every event being infected with Covid defined by the `np.random.choice()` function with the `ATTACK_RATE = 0.10`. Once we run this function, the 10% of people that are labelled as infected becomes are framing population.

The second stage of sampling is during primary contact tracing defined by the function `np.random.rand() < TRACE_SUCCESS = 0.20`. Using our framing (infected) population, we randomly assign a person as being traced or not traced based on a trace success rate of 20%. This is our first sampled population. We use this to calculate the proportion of infections attributed to each event type and ultimately the proportion of wedding infections. This is observed in our graph as the blue bar marked "Infections from Weddings".

The final stage of sampling is during secondary contact tracing. We first filter our results to only those that were traced and then count the number of people traced per event. If the event has more traced individuals than the `SECONDARY_TRACE_THRESHOLD = 2`, every infected person that attended that event gets marked as traced. The idea is that if an event has more than 2 infected people that attended, you will go back and test everyone at that event. Every infected person associated with that event would then be traced. This becomes our second sampled population. We use this to calculate the proportion of traces attributed to each event type and ulimately the proportion of traced infections. This is observed in our graph as the red bar marked "Traced to Weddings".

### Comparing Graphs:
After running the code as is, it does not produce the same graphs as those in the original blog post. In our graph, there is a lot more overlap between the "Infections from Weddings" and the infections "Traced to Weddings". The frequency of these two variables are similar as well as the distribution of the proportion of cases. Cases that were traced to weddings did have a higher frequency of proportion ranging from 0 to 5% but overall, both variables range from approximately 8 to 34%. 

### Reproducibility:
When running the script multiple times, the outputted graphs always changed. This means that the defined function and the subsequent simulation is not reproducibile. Every time you run the code, you will get slightly different results. In order to make it reproducible, a numpy.random.seed function with an integer in its parameters must be included in the code. I inserted a `np.random.seed(42)` function before the simulation is called to make the results reproducible and consistent.

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
