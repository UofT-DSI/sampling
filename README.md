# Sampling

## Content

- [Description](#description)
- [Learning Outcomes](#learning-outcomes)
- [Logistics](#logistics)
   * [Module Contacts](#module-contacts)
   * [Delivery of Module](#delivery-of-module)
   * [How the Technical Facilitator will deliver](#how-the-technical-facilitator-will-deliver)
   * [Expectations](#expectations)
   * [Requirements](#requirements)
   * [Lesson Schedule](#lesson-schedule)
- [Marking Scheme and Assignment Submission](#marking-scheme-and-assignment-submission)
- [Resources](#resources)
   * [Documents](#documents)
   * [Videos](#videos)
   * [How to get help](#how-to-get-help)
- [Folder Structure](#folder-structure)
- [Acknowledgements](#acknowledgements)

## Description

The goal of this module is to introduce the essentials of sampling, probability, and survey methodology. This includes simple probability samples, stratified sampling, cluster sampling, dealing with non-response, estimating and survey quality. Students will consider the theoretical foundations of different sampling approaches, as well as practical applications of this knowledge towards contexts such as market research, political polling, and the Canadian census. Analysis using the Python programming language will also be highlighted, drawing on skills developed in Module 3.

## Learning Outcomes
1. Implement simple probability samples.
2. Evaluate the complicated sampling procedures and the tradeoffs involved.
3. Identify and understand sources of error or inaccuracies in data as a result of sampling strategies.
4. Develop intuition around survey quality.

## Logistics

### Module Contacts
**Questions can be submitted to the #questions channel on Slack**

* Technical Facilitator: **{Name}** {Pronouns}. Emails to the Technical Facilitator can be sent to {first_name.last_name}@mail.utoronto.ca.
* Learning Support Staff: **{Name}** {Pronouns}. Emails to the Technical Facilitator can be sent to {first_name.last_name}@mail.utoronto.ca.
  
### Delivery of Module
The module will run sychronously three times a week on Zoom. The first three days are used as "lectures" and will last a maximum of 3 hours. During this time, the Technical Facilitator will introduce the concepts for the week. The last two days are used for as optional, asychronous work periods. The work periods will also last for up to 3 hours. During these two days, an Technical Facilitator or TA will be present on Zoom to assist learners reach the intended learning outcomes.

### How the Technical Facilitator will deliver
The Technical Facilitators will introduce the concepts through a collaborative live coding session usiing the Python notebooks found under `/01_slides`. All Technical Facilitators will also upload any live coding files to this repository for any learners to revisit under `/live_code`.
 
### Expectations
Learners are encouraged to be active participants while coding and are encouraged to ask questions throughout the module.
 
### Requirements
* Learners are not expected to have any coding experience, we designed the learning contents for beginners.
* Learners are encouraged to ask questions, and collaborate with others to enhance learning.
* Learners must have a computer and an internet connection to participate in online activities.
* Learners must have VSCode installed with the following extensions: 
    * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
* Learners must not use generative AI such as ChatGPT to generate code in order to complete assignments. It should be use as a supportive tool to seek out answers to questions you may have.
* We expect learners to have completed the [onboarding repo](https://github.com/UofT-DSI/Onboarding/tree/tech-onboarding-docs).
* Camera is optional although highly encouraged. We understand that not everyone may have the space at home to have the camera on.

### Lesson Schedule
| Lesson | Topic                                                                                        | Assignments      | Resources  |
|--------|----------------------------------------------------------------------------------------------|------------------|------------|
| 1      | Introduction, Probability                                                                    |                  | [Slides 1](./01_slides/00_introduction_slides.pdf) <br> [Slides 2](./01_slides/01_probability_slides.pdf) |
| 2      | Populations, censuses, surveys, and observational data; Essentials of sampling, asking and observing  |  | [Slides 1](/01_slides/02_populations_censuses_surveys_and_observational_data_slides.pdf) <br> [Slides 2](./01_slides/03_essentials_of_sampling_asking_and_observing_slides.pdf)|
| 3      | Errors, simple probability samples, Stratified sampling, Differential privacy         | [Questionnaire Design (Part A)](./02_assignments/questionnaire_design_part_a.md) <br> [Questionnaire Design (Part B)](./02_assignments/questionnaire_design_part_b.md) | [Slides 1](./01_slides/04_errors_slides.pdf) <br> [Slides 2](./01_slides/05_simple_probability_samples_slides.pdf) <br> [Slides 3](./01_slides/06_stratified_sampling_slides.pdf) <br> [Slides 4](./01_slides/07_differential_privacy_slides.pdf) |
| 4      | Cluster Sampling, Nonresponse, Ethics | [Data Documentation Comparison Worksheet](./02_assignments/data_documentation_comparison_worksheet.md) | [Slides 1](./01_slides/08_cluster_sampling_slides.pdf) <br> [Slides 2](./01_slides/09_nonresponse_slides.pdf) <br> [Slide 3](./01_slides/10_ethics_slides.pdf) |
| 5      |  Estimation and survey quality, and Reproducibility, Inequity| [Sampling and Reproducibility in Python](./02_assignments/sampling_and_reproducibility.md) | [Slides 1](./01_slides/11_estimation_and_survey_quality_slides.pdf) <br> [Slides 2](./01_slides/12_reproducibility_slides.pdf) <br> [Slides 3](./01_slides/13_inequity_slides.pdf)|  
| 6      | Case Study  | | | 

## Marking Scheme and Assignment Submission
Please submit your assignments as pdf files using the google forms linked in the table below.

All assignments are pass or fail.

| Assessment       |  Due Date | Submission Link |
|------------------|-----------|-----------------|
| [Questionnaire Design (Part A)](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Questionnaire%20Design%20(Part%20A).md) |   TBD      | [https://forms.gle/pQW2mwzSXPSXcchB9](https://forms.gle/pQW2mwzSXPSXcchB9) |
| [Questionnaire Design (Part B)](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Questionnaire%20Design%20(Part%20B).md) |TBD | [https://forms.gle/xHSfCMq8QAa2PUyQA](https://forms.gle/xHSfCMq8QAa2PUyQA) |
| [Data Documentation Comparison Worksheet](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Data%20Documentation%20Comparison%20Worksheet.md) |  TBD  | [https://forms.gle/voo6ndjo7wjY72Zv8](https://forms.gle/voo6ndjo7wjY72Zv8)|
| [Sampling and Reproducibility in Python](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Sampling%20and%20Reproducibility.md) |  TBD       | [https://forms.gle/SwsuDdrxiwNJVWdd6](https://forms.gle/SwsuDdrxiwNJVWdd6)|

## Resources
Feel free to use the following as resources:

### Documents
- [Probability Cheatsheet 1](./04_resources/probability_cheatsheet_1.pdf)
- [Probability Cheatsheet 2](./04_resources/probability_cheatsheet_2.pdf)
- [Probability Cheatsheet 3](./04_resources/probability_cheatsheet_3.png)
- [CLT Demo](./04_resources/5.1_probability_clt_demo.py)
- [LLN Demo](./04_resources/5.1_probability_lln_demo.py)
- [Amazon Exercises](./04_resources/amazon_exercises.pdf)
- [Multiple Imputation Exercises](./04_resources/sampling_multiple_imputation_exerises.py)

### Videos
- [Survey Sampling Methods](https://www.youtube.com/watch?v=tuJnu8RAUuU)
- [Population vs Sample](https://www.youtube.com/watch?v=r-rFO_2NsgI)
- [Survey Margin of Error: What is it? How does it relate to sample size?](https://www.youtube.com/watch?v=nilZF1KmCg4)
- [Reproducibility in Research](https://www.youtube.com/watch?v=EvoVb_QLRK8)
- [Probability Playlist](https://www.youtube.com/playlist?list=PLC58778F28211FA19)



### How to get help
![image](/steps_to_ask_for_help.png)

<hr>

## Folder Structure

```markdown
.
├── 01_slides
├── 02_assignments
├── 03_instructors
├── 04_resources
├── LICENSE
├── README.md
└── steps_to_ask_for_help.png
```

* **slides:** Module slides as PDF files
* **live_coding:** Notebooks from class live coding sessions
* **assignments:** Graded assignments
* **resources**: Contains additional resources
* **instructors:** Instructions for the Technical Facilitator on what to teach
* README: This file!
* .gitignore: Files to exclude from this folder, specified by the Technical Facilitator

## Acknowledgements

Radu Craiu, and the Department of Statistical Sciences, suggested this Module. Rohan Alexander managed its development. Annie Collins developed the materials intially.



