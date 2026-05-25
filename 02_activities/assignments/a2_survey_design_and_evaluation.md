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

The number of your chosen topic: `1`

Describe the purpose of your survey:
The purpose of this survey is to investigate the underlying reasons for high turnover among entry- and lower-level employees across all departments of the company. 
The survey aims to identify key pain points in the employee experience and gather 
actionable insights that can inform organizational changes to improve job satisfaction and retention.

Describe your target population, sampling frame, sampling units, and observational units:
Target population: All current entry- and lower-level employees across all 
departments, as well as former employees who left the company within the past 
12 months.

Sampling frame: (1) For current employees — the HR database listing all active 
entry- and lower-level employees by department. (2) For departed employees — 
exit interview records and available contact information for staff who left within 
the past 12 months.

Sampling units: Individual employees (current or recently departed).

Observational units: Individual employees.

Sampling strategy: Stratified random sampling, with departments as strata. 
This ensures that every department is proportionally represented, which is 
important because the turnover problem spans multiple departments and root 
causes may differ by team. For departed employees, a census approach (contacting 
all available former employees) is used, since this group is small and their 
perspective is especially critical for understanding turnover.

Your 5-10 question survey:
1. How long have you worked (or did you work) at this company?
   [ ] Less than 6 months  [ ] 6–12 months  [ ] 1–2 years  [ ] More than 2 years

2. On a scale of 1 to 5, how satisfied are you (or were you) with your overall 
   work experience at this company?
   (1 = Very dissatisfied, 5 = Very satisfied)

3. What is (or was) the primary reason you are considering leaving (or did leave) 
   the company? (Select all that apply)
   [ ] Compensation  [ ] Limited career growth  [ ] Poor management  
   [ ] Work-life balance  [ ] Company culture  [ ] Better opportunity elsewhere  
   [ ] Other: ______

4. How would you rate your relationship with your direct manager?
   (1 = Very poor, 5 = Excellent)

5. Do you feel (or did you feel) that your compensation and benefits are 
   fair for your role and responsibilities?
   [ ] Yes  [ ] No  [ ] Unsure

6. Do you feel (or did you feel) there are clear opportunities for career 
   advancement within the company?
   [ ] Yes  [ ] Somewhat  [ ] No

7. How would you rate your work-life balance at this company?
   (1 = Very poor, 5 = Excellent)

8. How would you describe the overall workplace culture? (Open-ended)

9. What single change would most improve employee satisfaction and retention 
   at this company? (Open-ended)

10. Would you recommend this company to a friend as a place to work?
    [ ] Yes  [ ] No  [ ] Maybe

## Part B - Survey Evaluation:

Identify and describe survey features:
1. Sample type:
   Stratified random (probability) sample, stratified by province and 
   Census Metropolitan Area (CMA). A cross-sectional design was used.

2. Sample size:
   Approximately 20,000 respondents completed the survey 
   (with a larger number initially selected/contacted).

3. Target population:
   All non-institutionalized persons aged 15 years and older living in 
   private households in Canada's 10 provinces. Excludes residents of 
   Yukon, Northwest Territories, and Nunavut, and full-time residents 
   of institutions (e.g., prisons, care homes).

4. Sampling frame:
   Statistics Canada's common telephone frame, which combines landline 
   and cellular telephone numbers, integrated with the dwelling/Address 
   Register frame. This replaced older random digit dialing (RDD) methods 
   and improved coverage.

5. Survey mode(s):
   Two modes were offered:
   - CATI (Computer-Assisted Telephone Interviewing) — interviewer-assisted
   - rEQ (Respondent-completed Electronic Questionnaire, i.e., online) — 
     offered for the FIRST TIME in the 2018 cycle
   Questionnaire available in both English and French.

6. Timeline:
   Data collection: September to December 2018
   Public Use Microdata File (PUMF) released: January 26, 2021

7. Response rate:
   Overall response rate: 40.9%
   - Regular sample: 42.2%
   - Oversample: 37.1%

8. Weights:
   - WGHT_PER: person-level survey weight, adjusted for non-response 
     and population benchmarks (age, sex, province)
   - Bootstrap weights: provided for design-based variance estimation 
     (accounting for the complex stratified design)
   - Record linkage to personal tax files used to supplement income data 
     (since 2014)

9. Data processing:
   Statistics Canada's standard SSPE (Survey Support Processing Environment) 
   generalized processing steps were applied. Automated and manual edits 
   were performed, including consistency, flow, and family edits. The CATI 
   system included built-in validation and questionnaire flow controls.

10. Cleaning, imputation, etc.:
    - Donor imputation used to address item non-response (e.g., hours 
      volunteered, donation amounts, income)
    - Score functions matched donors and recipients on relevant characteristics
    - Income data linked from personal tax records (administrative linkage) 
      to reduce non-response on income questions
    - Approximately 88 variables were subject to imputation in prior cycles; 
      similar approach applied in 2018

11. Sources of error:
    - Sampling error: inherent variability due to surveying a sample rather 
      than the full population; estimated using bootstrap resampling methods
    - Non-response error: overall response rate of ~41% means non-response 
      bias is a significant concern; weights partially correct for this
    - Coverage error: exclusion of territories and institutionalized persons 
      means results are not fully representative of all Canadians
    - Measurement error: self-reported data on volunteering hours and 
      donation amounts may involve recall bias or social desirability bias

12. Limitations / known biases:
    - Excludes Yukon, NWT, Nunavut → results not generalizable to all Canada
    - Excludes institutionalized persons (who may have different 
      volunteering/donating patterns)
    - Low response rate (~41%) increases risk of non-response bias
    - Introduction of online mode (rEQ) in 2018 affects comparability 
      with previous cycles (2004, 2007, 2010, 2013)
    - Questionnaire was significantly reworked in 2018 (new international 
      standards, new online tech questions) → results CANNOT be directly 
      compared to earlier GVP cycles
    - Income questions historically have high non-response rates even 
      after imputation

## Rubric

-	All required components are present and complete **Complete / Incomplete**
-	Choice of sampling strategy for Part A is justified and related to survey purpose **Complete / Incomplete**
-	Information for Part B is complete and correct **Complete / Incomplete**

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 09 February 2026`
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
