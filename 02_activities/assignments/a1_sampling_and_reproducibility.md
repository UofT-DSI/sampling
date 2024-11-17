# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Camelia Najafizadeh


# Sampling Stages
# Infection Sampling
 10% of attendees (200 wedding, 800 brunch) are randomly infected using ATTACK_RATE.
# Primary Contact Tracing
20% of infected cases are randomly traced (TRACE_SUCCESS), representing a Binomial distribution.
# Secondary Tracing:
If an event has ≥2 traced cases (SECONDARY_TRACE_THRESHOLD), all infected attendees at that event are traced, introducing bias toward larger gatherings like weddings.

# Sampling Procedure Description
Sampling Procedure:
The code models the spread of an infection and the process of contact tracing within two distinct event groups: wedding attendees and brunch attendees. This approach reflects how the data may be skewed toward specific event types based on the ease of tracing attendees.

# Referenced Functions:
simulate_event: Executes the logic for infection spread and contact tracing.

np.random.choice: Randomly selects individuals to be infected, using a uniform distribution.

np.random.rand: Determines whether an infected individual is traced, based on a Bernoulli distribution with a 20% likelihood.

Sample Size:
The simulation includes 1,000 individuals per event, divided as follows: 200 attending weddings and 800 attending brunches.

Sampling Frame:
The sampling frame consists of all individuals participating in the events, categorized into two groups based on the type of event they attend.

# Relation to blogpost
The code aligns with Whitby’s observation that contact tracing tends to favor larger, more traceable events, such as weddings. The use of uniform and Bernoulli distributions captures the randomness inherent in infection spread and tracing. Additionally, the code introduces a bias toward events that are easier to trace, exemplified by weddings.


# Comparison to Blog Post
Running the code with 50,000 iterations should roughly match the blog's histograms, showing a higher trace proportion for weddings due to secondary tracing. Reducing iterations to 1,000 increases variability and makes results less consistent.

# Reproducibility
To make results reproducible, add np.random.seed(42) at the start of the script. This ensures consistent output across runs by fixing the random sequence.

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
