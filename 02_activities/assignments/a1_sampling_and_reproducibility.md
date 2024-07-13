# ASSIGNMENT: Sampling and Reproducibility in Python

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

# Author: Navneet Choudhary

```
There are 4 stages at which sampling occurred: the initial stage of sampling events, the stage of infection, primary contact tracing and secondary contact tracing.

The sampling procedure was either done by predefined rations (2 weddings or 80 brunches) in the initial stage by random sampling. In the infection stage, the sampling procedure was by infection simulation done using independent and identically distributed (IID) random variables. At the primary contact tracing stage, the sampling procedure was to note that each infected individual had a 20% chance of being traced back to the event they attended. This simulates imperfect recall and contact tracing inefficiencies and tracing outcomes (traced or not traced) are determined probabilistically. In the secondary contact tracing state the sampling procedure done by tracing simulation that was taken by ensuring all infections associated with the event are identified and was a more comprehensive tracing effort in comparison to primary tracing. 

The functions used were randomly sampled by numpy.random.choice() for selecting attendees to events. Infection simulation by numpy.random.rand(). Primary contact tracing was done by pandas.Series.value_counts(): and  secondary contact tracing based was done on pandas.DataFrame.loc[]. Sampling size was 1000 people attending the events and the sampling frame were infected individuals which ultimately changed to events where multiple infections were traced. 

The underlying distributions were uniform distributions for stages 1 and 2 and binomial distributions for stages 3 and 4. These distrubtions are chosen to reflect the nature of infection spread and contact tracing discribed in the post. 


Does this code appear to reproduce the graphs from the original blog post?

Yes the code does reproduce the graphs from the original blog post, the result is not exactly 20%, which is also noted in the blog post. But the infection to trace to weddings is 20%.

Comment on the reproducibility of the results.

The results are consistent and even when changing the sample size, it is still consistent.  

Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times.

The changes that were made are adding np.random.seed(42) to ensure random number generation across the rins. I also motified simulate_event() function to use np.random.rand() to be based ont he seeded random number generator (42). 

```


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
