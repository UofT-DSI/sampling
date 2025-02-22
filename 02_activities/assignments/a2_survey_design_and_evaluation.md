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


# Your Changes

## Part A - Survey Design: 

The number of your chosen topic: `#`

Describe the purpose of your survey:
```
The survey aims to understand why there is such a high turnover of employees, especially in entry—and lower-level positions. The insights can help the company implement strategies to improve employee satisfaction and retention.  
```

Describe your target population, sampling frame, sampling units, and observational units:
```
Target population: All employees of the tech company.
Sampling Frame: A database of all registered employees within the company.
Sampling units: Individuals selected to receive the survey among those employees who work for the company.
Samplying strategy: Stratified sampling, where employees are grouped by job level to ensure fair representation of each category.
```

Your 5-10 question survey:
```
1. How long have you been working with us? 
2. What is your current job level?
3. How far do you live from the office?
4. What is your primary work arrangement? Fully remote | Hybrid | Fully in office
5. How satisfied are you with the benefits offered by the company? Very satisfied | Satisfied | Nutral | Dissatisfied| Very Dissatisfied
6. On a scale of 1-5, how challenging do you find your daily tasks? (1 - Not challenge / 5- Extremelly challenge) 
7. Do you feel you have sufficient opportunities for career growth within the company? 
8. write your question here... (optional)
9. write your question here... (optional)
10. write your question here... (optional)
```

## Part B - Survey Evaluation:

Identify and describe survey features:

```
1. Sample type: Two types of sampling: 
    I. Stratification by province/census metropolitan area (CMA) level.
    II. Random selection household member aged 15 or older.

2. Sample size
    The size of the sample was 50,000 units, in which 40,000 invitations letters to the eletronic questionnaire were sent to selected households across Canada.

3. Target population
    Person 15 years and older living in the ten provinces of Canada, excluding full-time (residing for more than six months) residents of institutions.

4. Sampling frame
    The sampling frame combine the landline and cellular telephone numbers from the Census and various administrative sources with Statistics Canada's dwelling frame.

5. Survey mode(s)
    The data are collected directly from survey respondents either through an electronic questionnaire or through CATI (computer assisted telephone interviewing). No proxy reporting is allowed. The respondents has the choice between French and English. The average time to complete the survey is estimated at 44 minutes.

6. Timeline
    The data was collected  between: 2018-09-04 to 2018-12-28

    Reference period: Past 12 months preceding interview date

    Collection period: Every 5 years, from September to December

7. Response rate
    It was expected 24,000 responses out of 50,000

8. Weights
    Three weighting were used:

    I. A weighting factor (WGHT_PER) for analysis at the individual level, to estimate number of people having one or more characteristics.
    II. Bootstrap weights created for design-based variance estimation.
    III. Estimates adjusted using weighting so that they are representative of the target population with regard to certain characteristics.
    A weighting factor is available on the microdata file:


9. Data processing
    The survey followed a structured processing environment (SSPE) to ensure high-quality data outputs. Also, it used a structured environment to monitor the processing of data, and included automated and manual edits at macro and micro levels.

10. Cleaning, imputation, etc

    In order to ensure quality and reliability in the data, all survey records were subjected to computer edits throughout the course of the interview, included built-in questionnaire edits, family relationship checks, consistency checks, and flow edits to ensure correct response paths.

    Also, it was used Imputation of missing values in 9 steps, 

    I. Imputing personal income and family income. 
    II-IV.  Imputing the formal volunteering variables in the master file. 
    V-VI. Imputing the informal volunteering variables in the master file. 
    VII-IX. Imputing variables in the donation file and the solicitation methods in the master file.


    Finally, because in 2018 the personal income were not asked in the survey, tax data (T1FF, T1, T4) was linked for 81.9% of respondents.
    Family income data was available for 81.7% of households, with missing values imputed.


11. Sources of error: 

The survey data can be affected by the following errors:
- Typos in data entry
- Editing errors during the data cleaning can create errors if the assumptions made are incorrect.
- Innacuracies from incorrect or incomplete answers from respondents. It can be caused by misinterpretation of questions, memory issues or omiting responses.


12. Limitations, known biases, etc

The reasons for the survey limitations and bias are: 
- Non-sampling errors resulted from some groups that may have been underrepresented because of non-response or omitted answers
- Selection bias for an unintentional exclusion of non-phone users. Since the survey can only be completed via an electronic questionnaire or a telephone interview (CATI). 
- Income-related analyses can be affected by data linkage limitations because some respondents could opt for no linkage to their tax data.


13. Link to documentation and any additional sources used
```

## Rubric

-	All required components are present and complete **Complete / Incomplete**
-	Choice of sampling strategy for Part A is justified and related to survey purpose **Complete / Incomplete**
-	Information for Part B is complete and correct **Complete / Incomplete**

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 23/02/2025`
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
