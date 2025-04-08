# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: HUONG NGUYEN

```
- Stages where sampling occurs:
1. Infecting a random subset of people - this is simple random sampling without replacement because the infected individuals are being chosen randomly and the 'replace' option is set to FALSE; based on the settings of this simulation, the sample size (infected individuals) is 10% of the population and each individual can only be "infected" once. The sampling frame is all individuals at the events (wedding and brunch). This procedure is different from the one described in the blog post where an individual has a 10% chance of getting infected at each event. Here, we're simulating a 10% infection rate for the whole population, which means all the infected people could be from either the wedding or the brunch.

2. Primary contact tracing - this is also random sampling without replacement. Although the number of infected people being traced is capped at 20% (TRACE_SUCCESS =0.2), this is not sampling strategy but rather a way to simulate real-life difficulties of tracing infected individuals. The sample size in this case is 20% of the infected individuals. The sampling frame is all infected individuals. This procedure is also similar to the one mentioned in the blog post in which only 20% of infected individuals can be traced.

This is the output when m = 1000:
![m1000](https://github.com/user-attachments/assets/970314eb-150d-460e-8628-aa3a642da1c4)
This result is different from the one in the blog post! I think the main factor for this difference is that in the blog post, each wedding/brunch is treated as individual incident (2 weddings and 80 brunches), whereas in our code there is one big wedding event and one big brunch event. Although the population number and the number of infected individuals are the same, the source of infection can vary significantly between these two simulations. 

This is the output when m = 100:
1st run:
![m100_1](https://github.com/user-attachments/assets/30269526-b27f-41e8-aea1-b7e0a9e4f284)

2nd run:
![m100_2](https://github.com/user-attachments/assets/39202379-91ce-40e8-8a2c-ea8a700aebda)

3rd run:
![m100_3](https://github.com/user-attachments/assets/0bba244b-a2aa-4bc4-b381-a3ff5a6d8205)

4th run:
![m100_4](https://github.com/user-attachments/assets/077e39e0-0e8c-4842-a4ab-247430f0f6cd)

I'd say that the results are similar (the overall trend of these graphs are similar, with the distributions centering around 20%) but not reproducible.

To ensure that the code is reproducible, I've introduced a seed value (right before defining the simulate_event function). The resulting graph is shown below, and it stays consistent between runs.
![withseed](https://github.com/user-attachments/assets/d8bfdfa3-686e-453e-afa8-68d6e6a8b252)

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
