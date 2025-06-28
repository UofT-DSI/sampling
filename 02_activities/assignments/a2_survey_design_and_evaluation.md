# Assignment: Questionnaire Design and Sample Evaluation

## Requirements

The goal of this assignment is to practice developing and evaluating sampling materials.

### Part A - Survey Design:

Select one of the scenarios below and design a survey to meet the need(s) outlined in the prompt.

1.	In two to three sentences, describe the purpose of your survey
2.	Describe your target population, sampling frame, sampling units, and overall sampling strategy.
3.	Write a 5-10 question survey to address your chosen scenario below.

##### Scenarios
1.	You work in the Human Resources Department at a large tech company. Over the past few months, the company has been experiencing a high turnover rate across many of its departments, specifically within the entry- and lower-level positions. The company wishes to understand why this turnover is happening, and what changes need to occur to improve employee satisfaction.
2.	You work for a Canadian national political party during a federal election. Throughout the campaign period, your party has seen relatively high approval ratings, but an opposing party is also polling favorably and may still have a chance to win the election. You are one month away from the election and you want to understand what voters want from your party and its leader in order to maintain your lead and eventually win the election.
3.	You are a student researcher in the sociology department at the University of Toronto. You are working on a research project that concerns the relationship between music taste and age. This involves both comparisons between different people of different ages and comparisons of the same individual at different ages during their lifetime. You wish to understand to what extent age influences music taste, specifically as it relates to perceptions of popular music. Your results will be written into an academic paper that you hope to publish.

### Part B - Survey Evaluation:

For the **Canadian General Social Survey on Giving, Volunteering, and Participating, 2018 (cycle 33)**, conducted by Statistics Canada find any and all available documentation for the data gathered and identify and describe the survey features indicated below.

1. Sample type
2. Sample size
3. Target population
4. Sampling frame
5. Survey mode(s) 
6. Timeline
7. Response rate
8. Weights
9. Data processing
10. Cleaning, imputation, etc
11. Sources of error
12. Limitations, known biases, etc
13. Link to documentation and any additional sources used


# Your Changes

## Part A - Survey Design: 

The number of your chosen topic: `#`

Describe the purpose of your survey:
```
The purpose of the survey is to assess what factors are contributing to high turnover in entry and low-employees and what can be done to improve employee satisfaction. By focusing on recently departed employees and their reasons for leaving, the survey will determine the what changes the company will need to make to retain their employees.
```

Describe your target population, sampling frame, sampling units, and observational units:
```
Our target population is former entry-level and lower level employees who have left our company. Our sampling frame is the list of entry-level and lower-level employees who have resigned from the company within the last year. Our observational units are the former employees. For this survey, I would use stratified sampling, with the strata being the departments to which these employees belonged. 
```

Your 5-10 question survey:
```
1. What department did you work in?
    a. HR
    b. IT
    c. Finance
    d. Sales
2. When you left this position, had you accepted another position at a different company?
    a. yes
    b. no
3. How much time did you work in this position?
    a. less than 3 months
    b. 3 months to a year
    c. one year to 3 years
    d. more than 3 years
4. Did you consider your salary and benefits at this job adequate?
    a. yes
    b. no
5. How much did salary and benefits contribute to your decision to leave?
    a. not at all
    b. a little
    c. a lot
    d. it was the mosts important factor
6. Did you consider your manager to be a good manager?
    a. yes
    b. no
7. How much did management contribute to your decision to leave?
    a. not at all
    b. a little
    c. a lot
    d. it was the most important factor
8. Please describe any other reason for departing from this role.
```

## Part B - Survey Evaluation:

Identify and describe survey features:

```
1. Sample type: statified probability sampling. The strata are provices/census metropolitan areas.
2. Sample size: approx. 50,000 sample units (groups of phones associated with an address, or single phone number)
3. Target population : all persons 15 years of age and older living in the ten province of Canada, excluding full-time (residing for more than six months) residents of institutions
4. Sampling frame: landline and cell phone numbers for the Census and various administrative sources within Statistics Canada's dwelling frame, grouped by address they are associated with if available. From the groups, only one individual would be interviewed.
5. Survey mode(s) : electronic questionnaire or CATI (computer assisted telephone interviewing) in english or french.
6. Timeline: Data was collected between 2018-09-04 and 2018-12-28.
7. Response rate: 41.9%
8. Weights: Estimation weights adjusting for the proportion of the population that would be 'rejected' for not being volunteers, for weighted income distribution matching the 2017 CIS distribution by province, and to ensure representation of independent estimatrs for various age-sex groups by province. Bootstrap weights were also created for design-based variance estimation.
9. Data processing: Data was linked to personal tax records for respondents, and tax records of all household members. Address, household and respondent personal information was also linked to provide data on location, demographics, income information, and demographics of the rest of the household. This was all done with the consent of respondents, with the option for respondents to object to the linkage of their data.
10. Cleaning, imputation, etc: Cleaning involved automatic and manual edits at various stages and levels. Family relationships were checked to ensure the integrity of matrix data. An example of another check that was done to ensure consistency of data was to compare the respondent age and respondent birth date. Imputation was done using donor records that would be scored based on similarity to respondent, in which the highest scored donor record was deemed the 'nearest' and the missing information was filled using this donor record. Imputation was done in nine steps, with info such as personal and family income first, and variables in the donation file and solicitation file coming last.
11. Sources of error: Common sources came from imperfect coverage and non response. The chosen frame excluded households without telephones or without numbers listed in the chosen sources for the frame. Non-response could also occurr at both the stage of selecting a household and at the stage of having an individual from the answer respond. 
12. Limitations, known biases, etc: Known biases are non-reponse bias, particularly to questions around income and household composition. In the 2018 stody, this was mitigated by the linkages to census and tax records. This study also excludes people in the territories altogether. 
13. Link to documentation and any additional sources used: https://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvey&Id=796234#a4
```

## Rubric

-	All required components are present and complete **Complete / Incomplete**
-	Choice of sampling strategy for Part A is justified and related to survey purpose **Complete / Incomplete**
-	Information for Part B is complete and correct **Complete / Incomplete**

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 29/06/2025`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (a2_survey_design_and_evaluation.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/sampling/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via the help channel in Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
