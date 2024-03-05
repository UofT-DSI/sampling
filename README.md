# Sampling

## Content

1. [Description](https://github.com/UofT-DSI/sampling#description)
2. [Learning Outcomes](https://github.com/UofT-DSI/sampling#learning-outcomes)
3. [Logistics](https://github.com/UofT-DSI/sampling#logistics)
4. [Marking Scheme](https://github.com/UofT-DSI/sampling#marking-scheme)
5. [Policies](https://github.com/UofT-DSI/sampling#policies)
6. [Folder Structure](https://github.com/UofT-DSI/sampling#folder-structure)
7. [Acknowledgements and Contributions](https://github.com/UofT-DSI/sampling#acknowledgements-and-contributions)

## Description

The goal of this module is to introduce the essentials of sampling, probability, and survey methodology. This includes simple probability samples, stratified sampling, cluster sampling, dealing with non-response, estimating and survey quality. Students will consider the theoretical foundations of different sampling approaches, as well as practical applications of this knowledge towards contexts such as market research, political polling, and the Canadian census. Analysis using the Python programming language will also be highlighted, drawing on skills developed in Module 3.

## Learning Outcomes
1. Ability to implement simple probability samples.
2. Ability to understand more complicated sampling procedures and the tradeoffs involved.
3. Ability to identify and understand sources of error or inaccuracies in data as a result of sampling strategies.
4. Development of intuition around survey quality.

## Logistics

### Course Contacts
* Instructor: [**Morris Greenberg**] [He/Him] [MSc., Statistics]. [morris.greenberg@mail.utoronto.ca](morris.greenberg@mail.utoronto.ca)
* Instructor: [**Mandy Yao**] [She/Her] [MSc, Statistics]. [mandy.yao@mail.utoronto.ca](mandy.yao@mail.utoronto.ca)
  * Email etiquette: Emails are welcomed. Please email both instructors if emailing. We will try to respond within 48-hours.
  


### Delivery instructions
The course will be held over two weeks, four days a week. Each day will be 2.5 hours. Being mindful of online fatigue, there will be one break during each class where students are encouraged to stretch, grab a drink and snacks, or ask any additional questions.

### Technology Requirements
1. Camera is optional although highly encouraged. We understand that not everyone may have the space at home to have the camera on.


### Lesson Schedule
| Lesson | Topic                                                                                        | Assignments      | Resources  |
|--------|----------------------------------------------------------------------------------------------|------------------|------------|
| 1      | Introduction, Probability                                                                    |                  | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/00-Introduction-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/01-Probability-slides.pptx) |
| 2      | Populations, censuses, surveys, and observational data; Essentials of sampling, asking and observing  |  | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/02-Populations%2C%20censuses%2C%20surveys%2C%20and%20observational%20data-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/03-Essentials%20of%20sampling%2C%20asking%2C%20and%20observing-slides.pptx)|
| 3      | Errors, simple probability samples, Stratified sampling                                      | [Questionnaire Design (Part A)](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Questionnaire%20Design%20(Part%20A).md) <br> [Questionnaire Design (Part B)](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Questionnaire%20Design%20(Part%20B).md) | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/04-Errors-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/05-Simple%20probability%20samples-slides.pptx) <br> [Slides 3](https://github.com/UofT-DSI/sampling/blob/main/lectures/06-Stratified%20sampling-slides.pptx) |
| 4      | Cluster Sampling, Nonresponse | [Data Documentation Comparison Worksheet](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Data%20Documentation%20Comparison%20Worksheet.md) | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/07-Cluster%20sampling-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/08-Nonresponse-slides.pptx) |
| 5      |  Nonresponse (cont.), Estimation and survey quality, Respondent-driven sampling| | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/08-Nonresponse-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/09-Estimation%20and%20survey%20quality-slides.pptx) <br> [Slides 3](https://github.com/UofT-DSI/sampling/blob/main/lectures/11-Respondent-driven%20sampling-slides.pptx)|  
| 6      |  Respondent-driven sampling (cont.), Advanced data collection, Reproducibility  | [Sampling and Reproducibility in Python](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Sampling%20and%20Reproducibility.md)| [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/11-Respondent-driven%20sampling-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/12-Advanced%20data%20collection-slides.pptx) <br> [Slides 3](https://github.com/UofT-DSI/sampling/blob/main/lectures/13-Reproducibility-slides.pptx)| 
| 7      |  Differential privacy, Ethics, Inequity  | | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/14-Differential%20privacy-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/15-Ethics-slides.pptx) <br> [Slides 3](https://github.com/UofT-DSI/sampling/blob/main/lectures/16-Inequity-slides.pptx) |  
| 8      |    Case Study                               | [Final Assessment](https://github.com/UofT-DSI/sampling/blob/main/assessment/Final%20Assessment.md) | |


## Marking Scheme and Assignment Submission
Please submit your assignments as pdf files using the google forms linked in the table below.
| Assessment       | Weight |  Due Date | Submission Link |
|------------------|--------|-----------|-----------------|
| Participation |  10%  |        |
| [Questionnaire Design (Part A)](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Questionnaire%20Design%20(Part%20A).md) |  10%  |   March 5, 2024      | [https://forms.gle/pQW2mwzSXPSXcchB9](https://forms.gle/pQW2mwzSXPSXcchB9) |
| [Questionnaire Design (Part B)](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Questionnaire%20Design%20(Part%20B).md) |  10% | March 5, 2024 | [https://forms.gle/xHSfCMq8QAa2PUyQA](https://forms.gle/xHSfCMq8QAa2PUyQA) |
| [Data Documentation Comparison Worksheet](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Data%20Documentation%20Comparison%20Worksheet.md) |  15% |  March 12, 2024  | [https://forms.gle/voo6ndjo7wjY72Zv8](https://forms.gle/voo6ndjo7wjY72Zv8)|
| [Sampling and Reproducibility in Python](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Sampling%20and%20Reproducibility.md) |   15%  |  March 12, 2024        | [https://forms.gle/SwsuDdrxiwNJVWdd6](https://forms.gle/SwsuDdrxiwNJVWdd6)|
| [Final Assessment](https://github.com/UofT-DSI/sampling/blob/main/assessment/Final%20Assessment.md) |   40%  |  March 9, 2024   |[https://forms.gle/QDbissy89WnY3JQP8](https://forms.gle/QDbissy89WnY3JQP8)|

## Policies
Questions are encouraged! Extensions for assessments may be granted but the hard deadline for all assessments is March 16, 2024. Please ask for extensions as soon as possible. 

## Late Policy:
Submissions can be submitted late on an as needed basis. The hard deadline for all assessments, however, is March 16, 2024.

## Academic Integrity:
We will indicate when assignments can be collaborative vs. individual. For individual assignments, please write your own solutions. If you use any outside resources, please cite them. Using large language models is discouraged but allowed. We have found that using answers from these are variable at best. Please use your best judgment.

## Folder Structure
Below are the folders contained in this repo with a description of what they contain and information on how to use them.

### 1. *assessment*:
This folder contains the assessments for the workshop. Students are expected to complete them one week after the content has been delivered.

### 2. *lectures*:
This folder contains the powerpoint files for the slides. 

### 3. *resources-exercises*:
Exercises are just a suggestion but will help students throughout the workshop, as content is cumulative and will only get more difficult. Unfortunately, there is not enough time to review previous content each class so while these exercises are **not** graded, they are highly recommended.

### 4. *lesson plans*:
These were used to plan the course but we are not following them exactly so feel free to ignore.

## Achnowledgements

Radu Craiu, and the Department of Statistical Sciences, suggested this course. Rohan Alexander managed its development. Annie Collins developed the materials intially.



