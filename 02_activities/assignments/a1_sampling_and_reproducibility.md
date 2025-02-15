# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Tatiana Midori Uemura Kawaguti

```
I. Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

        The model executes multiple stages of sampling: Primary Sampling and Secondary Sampling.The sampling procedure is as follows:

        1. Sampling Frame Creation:
        First, a sampling frame is created, represented by a dataframe with 1000 rows, which include all people who attended either a wedding or a brunch. As mentioned in the blog post, the two weddings account for 100 attendees each (200 people), and the remaining 800 individuals represent the 10 attendees at each of the 80 brunches.


        2. Primary Contact Tracing (Random Sampling):
        In this stage, 10% of the total population is randomly selected as 'Infected' (ppl['traced'] == True), with each individual having an equal probability of being infected. This process simulates a 10% infection rate, as described in the blog post.

        The code demonstrating this random selection is:
        infected_indices = np.random.choice(ppl.index, size=int(len(ppl) * ATTACK_RATE), replace=False)

        Since ATTACK_RATE = 0.10, it set a 10% sample size, meaning 100 individuals are randomly selected to be infected.


        3. Secondary Contact Tracing (Random Sampling):
        In the secondary tracing step, the model identifies infected individuals based on contact tracing. Since only 20% of the cases are traced to their source, 20% of the initially infected individuals are randomly selected for tracing (TRACE_RATE = 0.2).

        The corresponding code is:
        traced_indices = np.random.choice(infected_indices, size=int(len(infected_indices) * TRACE_RATE), replace=False)


        4. Proportion Identification:
        Using the previous steps, it is now possible to identify the proportion of individuals who were infected according to the event they attended (wedding or brunch). 

II. Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?


        Upon comparing the graphs, the blue graph (True proportion) labeled "Infections from weddings" shows similar characteristics in both the model and the blog post, centering around 20% with some variation. However, the red graph ("Traced Wedding") differs from the graph in the blog post. Both the model’s and blog post’s graphs show shapes centered around 20%, with some variation. The differences can be attributed to the random nature of the sampling process, which introduces variability.


III. Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

        After modifying the simulation to 100 repetitions (down from the original 1000), and running the script multiple times, the graphs exhibit noticeable changes. This is expected, as a smaller sample size (100 instead of 1000) introduces more variability and makes the results more sensitive to the inherent randomness in the sampling process. The variability in the output suggests that with fewer repetitions, the sampling process becomes more pronounced and less stable.

IV. Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

        To ensure reproducibility and guarantee the same result each time the script is run, we need to add a random seed at the beginning of the script.
        
        Added the following line to the script: np.random.seed(42)

        By setting the random seed, we ensure that the same set of random numbers will be generated each time the script is executed, making the results reproducible, getting the same output every time it is run.



## Criteria

|Criteria|Complete|Incomplete|
|--------|----|----|
|Altercation of the code|The code changes made, made it reproducible.|The code is still not reproducible.|
|Description of changes|The author explained the reasonings for the changes made well.|The author did not explain the reasonings for the changes made well.|

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 16/02/2025`
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
