# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Muhammad Ammar Bin Che Mahzan

```
Q1: Examine the code in `whitby_covid_tracing.py`.
Identify all stages at which sampling is occurring in the model.
Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Answer:
'whitby_covid_tracing.py' simulates infection and contact tracing in two types of events (weddings vs. brunches).  Sampling occurs at three stages: 1) who gets infected, 2) primary contact tracing, 3) secondary contact tracing

  python
  # Infect a random subset of people
  infected_indices = np.random.choice(ppl.index, size=int(len(ppl) * ATTACK_RATE), replace=False)
  ppl.loc[infected_indices, 'infected'] = True

Primary contact tracing: randomly decide which infected people get traced: ppl.loc[ppl['infected'], 'traced'] = np.random.rand(sum(ppl['infected'])) < TRACE_SUCCESS

- Sampling frame: the 1,000 rows of the ppl DataFrame (indices 0-999).
- Sample size: exactly floor(1000 × ATTACK_RATE) = 100.
- Procedure: simple random sampling without replacement (uniform).

- Relation to Andrew Whitby blog: in the toy model each person independently has 10% chance of infection—here we force exactly 10% of the population to be infected on each run.

Q2: Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Answer: Yes. the overlaid histograms align with Whitby's original plots, with the blue histogram centered around 0.20 and spanning from 0.10 to 0.30 (True proportion curve), and the red histogram centered higher at 0.40, matching the shape and rightward shift of his "Observed proportion" curve. In short, the code faithfully reproduces the qualitative behavior and relative shift between true and observed wedding-infection proportions that Whitby presented.


Q3: Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Answer: The simulation's output is not reproducible across runs at 100 Monte Carlo trials due to the small number of repetitions. The blue curve (true wedding-infection proportion) and red curve (observed, traced-to-wedding proportion) shift significantly each time the script is run. This variability is due to the central limit effect not stabilizing sample means and variances. To achieve stable visual summaries, more repetitions or fixed random seeding are needed.

Q4: Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times.

Answer: Add line: np.random.seed(20250629). By calling np.random.seed(20250629) before calls to np.random.choice or np.random.rand, NumPy's pseudo-random number generator is set to a known state, ensuring that subsequent random draws in simulate_event follow the same sequence.
```

## Criteria

| Criteria                | Complete                                                       | Incomplete                                                           |
| ----------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------- |
| Altercation of the code | The code changes made, made it reproducible.                   | The code is still not reproducible.                                  |
| Description of changes  | The author explained the reasonings for the changes made well. | The author did not explain the reasonings for the changes made well. |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:

- Submission Due Date: `23:59 - 09/04/2025`
- The branch name for your repo should be: `assignment-1`
- What to submit for this assignment:
  - This markdown file (a1_sampling_and_reproducibility.md) should be populated.
  - The `whitby_covid_tracing.py` should be changed.
- What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/sampling/pull/<pr_id>`
  - Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:

- [ ] Create a branch called `assignment-1`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via the help channel in Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
