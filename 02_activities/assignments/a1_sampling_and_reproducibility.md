# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: HUONG NGUYEN

```
- Stages where sampling occurs:
1. Infecting a random subset of people - this is simple random sampling without replacement because the infected individuals are being chosen randomly and the 'replace' option is set to FALSE; based on the settings of this simulation, the sample size (infected individuals) is 10% of the population and each individual can only be "infected" once. The sampling frame is all individuals at the events (wedding and brunch). This procedure is similar to the one described in the blog post where an individual has a 10% chance of getting infected regardless of the event that they are at. 
2. Primary contact tracing - this is also random sampling without replacement. Although the number of infected people being traced is capped at 20% (TRACE_SUCCESS =0.2), this is not sampling strategy but rather a way to simulate real-life difficulties of tracing infected individuals. The sample size in this case is 20% of the infected individuals. The sampling frame is all infected individuals. This procedure is also similar to the one mentioned in the blog post in which only 20% of infected individuals can be traced.

This is the output when m = 1000:
![download1](https://github.com/user-attachments/assets/6ae3984c-0554-4af5-a54f-e0375e450bd0)

This is the output when m = 100:
1st run:
![download2](https://github.com/user-attachments/assets/812e5eb0-2f9b-4816-b609-367d669d53c0)

2nd run:
![download3](https://github.com/user-attachments/assets/24905c03-4e94-43ad-9906-8aad1e696a04)

3rd run:
![download4](https://github.com/user-attachments/assets/2f6a7270-aa56-47aa-b06a-07fb54254086)

4th run:
![download5](https://github.com/user-attachments/assets/9eebf756-4529-46cf-8fa0-1ca81bc8ead1)


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
