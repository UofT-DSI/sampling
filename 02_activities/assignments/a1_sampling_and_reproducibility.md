# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: YOUR NAME


MD RAZAUL KARIM 


In this link , I have seen  the potential impact of sampling bias in contact tracing on data regarding
sources of infection for COVID-19 in Toronto, Ontario, Canada. Although institutional outbreaks have consistently accounted for a large proportion of all COVID-19 .The blog post highlights how the sampling procedure for contact tracing introduces a systematic bias, resulting in an incomplete and non-representative sample of COVID-19 cases. Here’s a breakdown of the sampling procedure in the model code provided, and how it aligns with the explanation in the blog:

Event Attendance Sampling:

Sample Size: The entire population of 1,000 people.
Sampling Frame: All individuals in the population attend exactly one of two event types:
Weddings: 2 events with 100 attendees each.
Brunches: 80 events with 10 attendees each.
This setup matches the assumption in the blog where some gatherings (like brunches) involve many small groups, while others (like weddings) involve a few large groups.
Underlying Distribution: Each individual is assumed to attend exactly one event, which sets up distinct groups by event type and size. No probabilistic selection occurs here; it’s a fixed assignment of people to events.
Primary Infection Sampling:

Sample Size: 10% of all attendees are marked as infected based on an independent random sampling.
Sampling Frame: All attendees across all events have the same probability of infection.
Underlying Distribution: Each attendee has a 10% chance of being infected, independent of others (i.i.d.), with the binomial distribution describing the infection rate per event.
This sampling mimics the real-world randomness in transmission within an event, where infection is independent but consistent across event types, reflecting the true infection rate without bias.
Primary Contact Tracing Sampling:

Sample Size: Only a subset of infected individuals are contact-traced successfully (20% tracing success).
Sampling Frame: The infected subset of individuals across all events.
Underlying Distribution: Each infected individual has a 20% chance of being traced, which is modeled as a binomial process where each infection independently has a chance to be traced.
This aligns with the blog’s mention of resource constraints and the imperfect recall in contact tracing, making only a fraction of infections traceable. The non-random nature of this tracing success means that some infections are systematically untraceable.
Secondary Contact Tracing:

Procedure: If at least two infected individuals at an event are successfully traced, the model assumes all individuals at that event are then fully traced.
Sampling Frame: Only events with two or more successfully traced cases qualify for secondary tracing.
Underlying Process: Secondary tracing amplifies certain events, allowing more infections at large events (like weddings) to be identified. This effect is deterministic once the tracing threshold is met, which biases the sample toward settings with more traceable cases(example weeding)
This closely follows the blog’s discussion, where events that are easier to trace (e.g., weddings or jails) are systematically overrepresented in tracing results.
Comparison to the Original Blog Post
Running the whitby_covid_tracing.py script with 50,000 repetitions as originally specified would yield output close to the original graphs in Whitby’s blog post if the model assumptions align. The large number of repetitions provides enough data points to accurately estimate the distribution of infection sources and tracing outcomes, generating smooth histograms.

Modifying the Number of Repetitions
Reducing repetitions to 1,000 and running the script several times will likely yield varying results across runs. This is because fewer repetitions reduce sample stability, leading to more variation in output. With 1,000 repetitions, histograms would appear less smooth and vary between runs, which could make them less reliable for inference about the underlying trends.

Making the Code Reproducible
To ensure reproducibility, add a fixed random seed before sampling:

python code 

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Set a random seed for reproducibility
np.random.seed(42)

The rest of the code remains unchanged
Define constants, functions, and perform the simulation
Adding np.random.seed(42) before any sampling will allow the code to produce consistent results in every run. This change ensures that every call to a random function yields the same outcome, enabling reproducible results regardless of system or environment. This does not need to match Whitby’s exact graphs but will produce stable and repeatable histograms with each execution of the script.

True Infection Rates: Reflect the true proportion of infections across different events, unaffected by tracing ability.
Observed Infection Rates: Heavily skewed by secondary contact tracing, making events like weddings appear more prominent in the observed infection data than they are in reality.
This skewed sampling mirrors the real-world limitations and biases highlighted in the blog post, where limited tracing resources result in overrepresentation of certain high-visibility events, creating a misleading view of transmission sources.


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
