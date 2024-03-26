# ASSIGNMENT: Sampling and Reproducibility in Python

## Requirements

Read the blog post [Contact tracing can give a biased sample of COVID-19 cases](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/) by Andrew Whitby to understand the context and motivation behind the simulation model we will be examining.

Examine the code in `whitby_covid_tracing.py`. Identify all stages at which sampling is occurring in the model. Describe in words the sampling procedure, referencing the functions used, sample size, sampling frame, any underlying distributions involved, and how these relate to the procedure outlined in the blog post.

Run the Python script file called whitby_covid_tracing.py as is and compare the results to the graphs in the original blog post. Does this code appear to reproduce the graphs from the original blog post?

Modify the number of repetitions in the simulation to 1000 (from the original 50000). Run the script multiple times and observe the outputted graphs. Comment on the reproducibility of the results.

Alter the code so that it is reproducible. Describe the changes you made to the code and how they affected the reproducibility of the script file. The output does not need to match Whitby’s original blogpost/graphs, it just needs to produce the same output when run multiple times

## Why am I doing this assignment?

This assignment supports learning outcomes 1 and 3:
	1.	Develop ability to implement simple probability samples.
	3.	Identify and understand sources of error or inaccuracies in data as a result of sampling strategies.

## Rubric

-	All required components are present and complete **Pass / Fail**
-	Script file can produce the same output when run multiple times **Pass / Fail**
-	Sampling terminology from class is used correctly **Pass / Fail**