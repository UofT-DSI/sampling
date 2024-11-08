
# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Maral Barkhordari

Please write your explanation here...

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

## 1. Examine the Code in `whitby_covid_tracing.py`

### Sampling Stages in the Model

In the `whitby_covid_tracing.py` code, sampling occurs at the following stages:

- **Infection Sampling**:  
  In `simulate_event`, a subset of people at events is randomly infected based on the `ATTACK_RATE` (10% of the population). This sampling is achieved using `np.random.choice`, which randomly selects infected individuals.

- **Primary Tracing Sampling**:  
  The code uses `np.random.rand` to decide if each infected individual is traced, with a success rate of `TRACE_SUCCESS` (20%).

- **Secondary Tracing Sampling**:  
  Additional tracing occurs if certain events (like weddings) exceed a threshold of traced cases (`SECONDARY_TRACE_THRESHOLD = 2`). This step biases the model by ensuring some events receive more attention.

### Sampling Procedure Description

- **Sampling Procedure**:  
  The code simulates the spread of infection and the tracing of contacts within two distinct groups: those attending weddings and those at brunches. This mimics how the data might be biased toward certain types of gatherings based on how traceable they are.

- **Referenced Functions**:  
  - `simulate_event`: Handles the infection and tracing logic.
  - `np.random.choice`: Randomly selects individuals to be infected, based on the uniform distribution.
  - `np.random.rand`: Determines if an infected person is traced, using a Bernoulli distribution (with a 20% probability).

- **Sample Size**:  
  The sample consists of 1,000 individuals per event simulation (200 at weddings and 800 at brunches).

- **Sampling Frame**:  
  The frame includes all individuals attending the events, split into two groups based on event type.

- **Underlying Distributions**:  
  - **Uniform Distribution**: Used for selecting infected individuals.
  - **Bernoulli Distribution**: Used for deciding whether an infected person gets traced.

- **Relation to the Blog Post**:  
  The code reflects Whitby’s observation that contact tracing biases toward larger, traceable events (like weddings). The uniform and Bernoulli distributions mirror real-world randomness in infection and tracing, and the code biases the results toward events that are easier to trace (e.g., weddings).

## 2. Running the Script and Comparing Results

After running the provided Python script, I generated a histogram comparing the proportion of cases that are actual infections from weddings versus those that are traced to weddings. The results align with the argument Andrew Whitby made in his blog post on contact tracing biases.

### Observations from the Graph

- **Actual Infections vs. Traced Cases**:  
  The first set of bars shows the proportion of cases that actually originated from weddings, based on the attack rate set in the simulation. The second set of bars shows the proportion of cases traced back to weddings through contact tracing.

- **Illustrated Bias**:  
  The graph clearly shows that the proportion of cases traced to weddings is higher than the actual proportion of infections from weddings. This illustrates a key point from Whitby’s blog: contact tracing can introduce a bias that makes certain events, like weddings, appear as more significant sources of infection than they really are.

### Does the Code Reproduce the Graphs from the Original Blog Post?

Yes, this code does appear to reproduce the main findings from Andrew Whitby’s blog post. After running the script, I generated a histogram that reflects the bias in contact tracing discussed in the post. Specifically, the graph shows two key proportions:
1. The actual infections that originated from weddings.
2. The cases traced back to weddings.

The resulting graph demonstrates that the proportion of cases traced to weddings is higher than the actual proportion of infections from weddings. This outcome is consistent with Whitby’s argument that contact tracing can introduce a bias, making certain events—like weddings—appear as more significant sources of infection than they truly are.

## 3. Modifying Repetitions for Reproducibility Observations

After reducing the number of repetitions in the simulation from 50,000 to 1,000 and running the script multiple times, I observed a notable difference in the consistency of the results across runs:

### Observations

- **Higher Variability**:  
  With only 1,000 repetitions, each run displayed more variation in the results, making it evident that random fluctuations have a stronger impact with a smaller sample size. This led to noticeable differences between the graphs generated from different runs, especially in terms of the distribution shapes and peak frequencies.

- **Less Smoothness in Histograms**:  
  The histograms were less smooth and appeared more irregular compared to those generated with 50,000 repetitions. Smaller sample sizes increased the likelihood of gaps or spikes, affecting the overall shape of the distribution.

- **Lower Reproducibility**:  
  Although the general pattern (the bias toward tracing to weddings) was still visible, the exact proportions of cases attributed to weddings versus other events varied between runs. This variability made it challenging to consistently reproduce the exact outcome observed with a larger sample size.

### Conclusion on Reproducibility

With only 1,000 repetitions, the results were less reproducible due to the increased influence of random variation. While the overall trend of tracing bias was still present, the specific values were more variable between runs. For a more consistent and reliable result, a larger sample size (like the original 50,000) is preferable, as it minimizes random fluctuations and provides a stable representation of the underlying bias effect described in Whitby’s blog post.

## 4. Altering Code for Reproducibility

To make the code reproducible, I added a line at the beginning of the script to initialize the random seed. I used `np.random.seed(42)` as an example, but any integer can be used here. This line ensures that any function relying on `np.random` (like `np.random.choice` and `np.random.rand`) will produce the same "random" numbers every time the script runs. As a result, the simulation will produce the same output each time it is executed, regardless of the environment or number of repetitions.

### Set a seed for reproducibility
np.random.seed(42)







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
