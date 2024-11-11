# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: ANSHU DWIVEDI

```
1. Examining the Code in whitby_covid_tracing.py

Sampling Stages in the Model

The sampling stages in the `whitby_covid_tracing.py` script occur as follows:

- Infection Sampling: Within the `simulate_event` function, a subset of attendees at events is randomly infected based on an `ATTACK_RATE` (10% of the population). This is done through `np.random.choice`, which randomly selects individuals to infect.

- Primary Tracing Sampling: Using `np.random.rand`, the code determines whether each infected individual is traced, with a 20% probability of success (`TRACE_SUCCESS`).

- Secondary Tracing Sampling: Further tracing occurs when events, like weddings, exceed a threshold of traced cases (defined by `SECONDARY_TRACE_THRESHOLD = 2`), introducing a bias by prioritizing certain events for tracing.

Sampling Procedure Description

The sampling procedure simulates infection spread and contact tracing within two groups—those attending weddings and brunches—to illustrate how traceability biases toward specific types of gatherings.

Referenced Functions:

- `simulate_event`: Manages infection and tracing logic.
- `np.random.choice`: Randomly selects infected individuals using a uniform distribution.
- `np.random.rand`: Uses a Bernoulli distribution (20% probability) to decide if an infected person is traced.

Sample Size: Each simulation involves 1,000 individuals, with 200 attending weddings and 800 attending brunches.

Sampling Frame: Consists of all event attendees, categorized by event type.

Underlying Distributions:

- Uniform Distribution: For selecting infected individuals.
- Bernoulli Distribution: For deciding tracing outcomes.

Relation to the Blog Post: The code models Whitby’s observations on contact tracing bias, favoring large, easily traceable events like weddings. The use of uniform and Bernoulli distributions mimics real-world randomness, introducing a bias in tracing for larger events.

2. Running the Script and Comparing Results

After running the Python script, a histogram was generated to compare actual infections at weddings to cases traced to weddings. These results support Andrew Whitby’s insights on contact tracing biases.

Observations from the Graph:

- Actual Infections vs. Traced Cases: One bar set reflects actual infections from weddings, while another shows cases traced to weddings.
- Illustrated Bias: The graph indicates a higher tracing rate for weddings than actual infections, aligning with Whitby’s point that tracing can skew data to make certain events, like weddings, appear more significant sources of infection.

Does the Code Reproduce the Graphs from the Original Blog Post?

Yes, the code replicates Whitby’s blog findings. The generated histogram demonstrates the tracing bias by showing two main aspects:
   - The actual infections originating from weddings.
   - The traced cases associated with weddings.

The resulting graph confirms Whitby’s argument about the inherent bias in contact tracing, which makes certain events seem more infection-prone than they are.

3. Modifying Repetitions for Reproducibility Observations

Reducing the simulation’s repetitions from 50,000 to 1,000 revealed notable changes in result consistency across runs:

Observations:

- Higher Variability: With only 1,000 repetitions, each run exhibited more variability, highlighting how random fluctuations impact results more at a smaller scale. This caused differences in distribution shapes and frequencies between runs.
- Less Smooth Histograms: The histograms appeared more irregular, with gaps and spikes, unlike the smoother distribution from 50,000 repetitions.
- Lower Reproducibility: The tracing bias trend remained visible, but case proportions fluctuated between runs, making exact results harder to replicate compared to a larger sample size.

Conclusion on Reproducibility: With fewer repetitions, results were less reproducible due to greater random variation. While the general tracing bias trend was present, specific values varied between runs. Larger sample sizes, like 50,000, are more reliable for stable results, reducing the influence of random variation.

4. Altering Code for Reproducibility

To ensure consistent results, I added `np.random.seed(42)` at the beginning of the script. Setting this seed makes `np.random` functions like `np.random.choice` and `np.random.rand` generate the same "random" values each time the script runs, ensuring reproducibility across different environments and repetition levels.

```


## Criteria

|Criteria|Complete|Incomplete|
|--------|----|----|
|Altercation of the code|The code changes made, made it reproducible.|The code is still not reproducible.|
|Description of changes|The author explained the reasonings for the changes made well.|The author did not explain the reasonings for the changes made well.|

## Submission Information

🚨 Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md) 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

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
