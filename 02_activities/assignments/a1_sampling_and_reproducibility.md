# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Kristina Talalaievska
## Sampling Stages in the Model based on function, sample size and proecedure involved:

 1. Infection Sampling
 • Function: simulate_event
 • Sample Size: 10% of event attendees.
 • Procedure : Randomly pick 10% of all attendees to be infected using np.random.choice.
 2. Primary Contact Tracing Sampling
 • Function: simulate_event
 • Sample Size: Depends on the number of individuals.
 • Procedure: For each infected individual, there’s a 20% chance they will be traced. This is determined by comparing random numbers with the trace success rate (TRACE_SUCCESS).
 3. Secondary Contact Tracing Sampling
 • Function: simulate_event
 • Sample Size: Depends on the number of events with at least two traced infections.
 • How It’s Done: If an event has two or more traced infections, all infected people at that event are marked as traced.

## All 3 types of sampling reflected in the blog: 
 1. Initial Infection (Infection Sampling): Randomly infect 10% of attendees to simulate the start of an outbreak.
 2. Primary Contact Tracing: Randomly trace 20% of the infected individuals to simulate initial tracing efforts.
 3. Secondary Contact Tracing: If two or more traces occur at an event, all infected individuals at that event are traced to simulate cluster tracing.

## Sampling parameters in the blog:
 1. ATTACK_RATE indicates people initially infected.
 2. TRACE_SUCCESS indicates success rate of tracing infected individuals.
 3. SECONDARY_TRACE_THRESHOLD indicates  minimum number of traces needed at an event to trigger further tracing.

## Visual Representation
The final plot shows how often infections and traces are attributed to weddings versus brunches across 1000 simulations. The blue bars represent the proportion of infections from weddings, and the red bars represent the proportion of traces linked to weddings.

The two codes you provided appear to be identical. Each code runs a simulation to model infections and contact tracing, then creates and saves histograms of the infection and tracing proportions. They should produce the same output when run with the same parameters. To make the code reproducible, the follow steps are required:
1. Setting Random Seed: The line np.random.seed(10) ensures that the random number generator starts from the same point (seed=10) every time the code runs. This means the random sampling for infection and tracing will produce identical results each time.
 2. Explicit Data Type Conversion: By explicitly setting the traced column in the ppl DataFrame to a boolean (ppl['traced'].astype('boolean')), the code ensures that the data type is uniform and interpretable. It prevent unexpected errors or discrepancies. 
 3. Documentation and Function Clarity: The addition of a docstring for the simulate_event function clarifies its purpose, parameters, and expected outputs. It facilitates code maintenance and collaboration by providing clear instructions.
 4. Plotting and Visualization Standards: Using sns.histplot from Seaborn for plotting ensures consistent and visually appealing histograms. Parameters such as color, alpha, binwidth are set consistently, enhancing the clarity and reproducibility of the visual output.
 6. Plot Labels and Title: Clear labeling (plt.xlabel, plt.ylabel, plt.title) of the plot components (Proportion of cases, Frequency, Impact of Contact Tracing on Perceived Infection Sources) improves interpretability. Including a legend (plt.legend()) and adjusting layout (plt.tight_layout()) further enhances the plot’s readability and professional presentation.

  

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
