# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 100 (from the original 1000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Pavandeep Kaur

# Identification and Explanation of Sampling Stages in the Model: 

1. # initial event attendance sampling (Primary Sampling):
   Procedure: The population is  divided into event types, but this can be seen as a form of stratified sampling where individuals are assigned to specific strata (weddings or brunches).
   Sampling frame: A population of 1000 individuals divided into two event types: Weddings: 2 events, 100 attendees each(200 total)
   Sample Size: The total population is 1000 (200 attending weddings, 800 attending brunches), and 10% of this population (100 individuals) are randomly chosen to be infected.
   Relation to the Blog Post: It reflects the blog post's assumption that every person in the community attends exactly one event during the time period under consideration. The division into weddings and brunches matches the blog post's setup: Weddings: 2 events, 100 attendees each (total 200 people). Brunches: 80 events, 10 attendees each (total 800 people)
   Underlying Distributions: in the initial event attendance sampling step of the code, there are no underlying probability distributions involved. This is because the assignment of individuals to events (weddings or brunches) is fixed and does not rely on any random sampling or probabilistic process.
   Functions used: the functions used in this step are: List Multiplication, Concatenation, Dataframe creation 

Below is code: 
   # Create DataFrame for people at events with initial infection and traced status
events = ['wedding'] * 200 + ['brunch'] * 800
ppl = pd.DataFrame({
    'event': events,
    'infected': False,
    'traced': np.nan  # Initially setting traced status as NaN
})


2. # Infection Sampling:
   Sampling Procedure	Randomly select 10% of the population (100 individuals) without replacement.
   Function: np.random.choice and assignment to infected column.
   Sampling Frame: All individuals in the population (1000 people)
   Sample Size: 10% of the population (100 people) are infected.
   Underlying Distribution: Uniform distribution (each individual has an equal chance of being infected). This is implemented using np.random.choice
   Relation to Blog Post: This reflects the blog post's assumption that 10% of people at each event are infected, but with some randomness introduced (i.e., not exactly 10% per event)

Below is code
# Infect a random subset of people
infected_indices = np.random.choice(ppl.index, size=int(len(ppl) * ATTACK_RATE), replace=False)
ppl.loc[infected_indices, 'infected'] = True


3. # Primary Contact Tracing Sampling:
   Function: np.random.rand and comparison to TRACE_SUCCESS.
   Sampling Frame: All infected individuals (100 people).
   Sample Size: 20% of infected individuals (20 people) are successfully traced.
   Sampling Procedure: For each infected individual, a random number is generated using np.random.rand. If the number is less than TRACE_SUCCESS (0.20), the individual is traced.
   Underlying Distribution: Uniform distribution (each infected individual has a 20% chance of being traced).
   Relation to Blog Post: This models the imperfect nature of contact tracing, where only a fraction of infections are successfully traced.

Below is code:
# Primary contact tracing: randomly decide which infected people get traced
  ppl.loc[ppl['infected'], 'traced'] = np.random.rand(sum(ppl['infected'])) < TRACE_SUCCESS


4. # Secondary Contact Tracing Sampling:
   Function: value_counts and filtering based on SECONDARY_TRACE_THRESHOLD.
   Sampling Frame: Events with at least 2 traced cases
   Sample Size: Varies depending on how many events meet the threshold
   Sampling Procedure: If an event has at least 2 traced cases (SECONDARY_TRACE_THRESHOLD), all infected individuals from that event are traced. This is done by checking the value_counts of traced cases per event and filtering events that meet the threshold
   Underlying Distribution: Determined by the distribution of traced cases across events. Unlike the primary tracing step, this step does not involve randomness. It is based on a fixed rule
   Relation to Blog Post: This reflects the blog post's assumption that if two cases are traced to the same event, a special effort is made to test all attendees of that event

Below is code:
# Secondary contact tracing based on event attendance
  event_trace_counts = ppl[ppl['traced'] == True]['event'].value_counts()
  events_traced = event_trace_counts[event_trace_counts >= SECONDARY_TRACE_THRESHOLD].index
  ppl.loc[ppl['event'].isin(events_traced) & ppl['infected'], 'traced'] = True  


5. # Proportion Calculation Sampling:
   Function: Summing and dividing to calculate proportions.
   Sampling Frame: population: All individuals in the simulation (1000 people).
                   Subsets: Infected Individuals: The subset of individuals marked as infected (100 people).
                   Traced Individuals: The subset of infected individuals who have been successfully traced 
   Sample Size: All infected and traced individuals.
   Sampling Procedure: The proportions of infections and traced cases attributed to weddings are calculated by summing the relevant subsets of the data and dividing by the total number of infections or traced cases.
   Underlying Distribution: Determined by the distribution of infections and traced cases across event types.
   Relation to Blog Post: This aligns with the blog post's goal of comparing the true proportion of infections from weddings to the observed proportion based on contact tracing.

Below is code:
# Calculate proportions of infections and traces attributed to each event type
ppl['event_type'] = ppl['event'].str[0]  # 'w' for wedding, 'b' for brunch
wedding_infections = sum(ppl['infected'] & (ppl['event_type'] == 'w'))
brunch_infections = sum(ppl['infected'] & (ppl['event_type'] == 'b'))
p_wedding_infections = wedding_infections / (wedding_infections + brunch_infections)

wedding_traces = sum(ppl['infected'] & ppl['traced'] & (ppl['event_type'] == 'w'))
brunch_traces = sum(ppl['infected'] & ppl['traced'] & (ppl['event_type'] == 'b'))
p_wedding_traces = wedding_traces / (wedding_traces + brunch_traces)


# Graph Comparison:
The blog post's graph and the script's output both demonstrate that contact tracing overestimates the proportion of infections from weddings. However, the blog post's graph shows a stronger bias with less overlapping between the true and observed proportions, while the script's output shows a weaker bias with more overlapping. This difference could be from  factors such as the number of simulations, parameter values, and graph type. By increasing the number of simulations, adjusting parameter values, and using a density plot, the script's output can be made to more closely match the blog post's graph.
Blog Post's Graph:
  True proportion (blue) and observed proportion (red) distributions have less overlap.
  Observed proportion is clearly shifted to the right, showing a strong bias from contact tracing.
Script's Output:
  True proportion (blue) and observed proportion (red) distributions have more overlap.
  Observed proportion is shifted to the right but shows a weaker bias compared to the blog post



# Repetitions changed to 100:
The results obtained after reducing the number of repetitions to 100 show significant variability between runs. Each graph differs in the distribution of infections and traced cases attributed to weddings. The true proportion (blue) and observed proportion (red) distributions overlap more, and the shapes of the histograms are less consistent. This indicates that with fewer repetitions, the results are less reproducible and more influenced by randomness. The bias introduced by contact tracing is still visible but less pronounced and harder to interpret consistently. 


# Setting a Random Seed: Reproducible code
I added the line np.random.seed(42) right after importing the  libraries.It ensures that every time the code runs, the random selections (such as selecting infected individuals and tracing contacts) will follow the same sequence of random numbers, making the simulation results reproducible.
Unlike the previous version (without a random seed), the results are now fully reproducible.
Running the script multiple times will produce identical graphs and numerical results.
This change does not affect the logic or findings of the simulation but ensures that the script produces the same output every time it is executed.

code:  # Set random seed for reproducibility
np.random.seed(42)


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
