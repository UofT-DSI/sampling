# Sampling

## Description

The goal of this module is to introduce the essentials of sampling, probability, and survey methodology. This includes simple probability samples, stratified sampling, cluster sampling, dealing with non-response, estimating and survey quality. Students will consider the theoretical foundations of different sampling approaches, as well as practical applications of this knowledge towards contexts such as market research, political polling, and the Canadian census. Analysis using the Python programming language will also be highlighted, drawing on skills developed in Module 3.

## Learning Outcomes
1. Implement simple probability samples.
2. Evaluate the complicated sampling procedures and the tradeoffs involved.
3. Identify and understand sources of error or inaccuracies in data as a result of sampling strategies.
4. Develop intuition around survey quality.

## Logistics

### Course Contacts
**Questions can be submitted to the #questions channel on Slack**

* Instructor: **{Name}** {Pronouns}. Emails to the instructor can be sent to {first_name.last_name}@mail.utoronto.ca.
* TA: **{Name}** {Pronouns}. Emails to the instructor can be sent to {first_name.last_name}@mail.utoronto.ca.
  
### Delivery of Module
The module will run sychronously three times a week on Zoom. The first three days are used as "lectures" and will last a maximum of 3 hours. During this time, the instructor will introduce the concepts for the week. The last two days are used for as optional, asychronous work periods. The work periods will also last for up to 3 hours. During these two days, an instructor or TA will be present on Zoom to assist learners reach the intended learning outcomes.

### How the Instructor will deliver
The instructors will introduce the concepts through a collaborative live coding session usiing the Python notebooks found under `/01-slides`. All instructors will also upload any live coding files to this repository for any learners to revisit under `/live-code`.
 
### Expectations
Learners are encouraged to be active participants while coding and are encouraged to ask questions throughout the module.

### Policies
* **Accessibility:** We want to provide an accessible learning environment for all. If there is something we can do to make this course more accessible to you, please let us know.
* **Course communications:** Communications take place over email or on Slack. If communicating over email, please include "DSI-Sampling" or similar in the subject line, e.g. "DSI-Sampling: Sampling question"
* **Camera:** Keeping your camera on is optional.
* **Microphone:** Please keep microphones muted unless you need to speak. Please indicate your name before speaking as some Zoom configurations make it hard to tell who is talking!
* **Assessment:** There will be homework which **is not** graded, but highly recommended, and there will be two assignments which **are** graded.
 
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
| 1      | Introduction, Probability                                                                    |                  | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/00-Introduction-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/01-Probability-slides.pptx) |
| 2      | Populations, censuses, surveys, and observational data; Essentials of sampling, asking and observing  |  | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/02-Populations%2C%20censuses%2C%20surveys%2C%20and%20observational%20data-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/03-Essentials%20of%20sampling%2C%20asking%2C%20and%20observing-slides.pptx)|
| 3      | Errors, simple probability samples, Stratified sampling                                      | [Questionnaire Design (Part A)](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Questionnaire%20Design%20(Part%20A).md) <br> [Questionnaire Design (Part B)](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Questionnaire%20Design%20(Part%20B).md) | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/04-Errors-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/05-Simple%20probability%20samples-slides.pptx) <br> [Slides 3](https://github.com/UofT-DSI/sampling/blob/main/lectures/06-Stratified%20sampling-slides.pptx) |
| 4      | Cluster Sampling, Nonresponse | [Data Documentation Comparison Worksheet](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Data%20Documentation%20Comparison%20Worksheet.md) | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/07-Cluster%20sampling-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/08-Nonresponse-slides.pptx) |
| 5      |  Nonresponse (cont.), Estimation and survey quality, and Reproducibility| | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/08-Nonresponse-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/09-Estimation%20and%20survey%20quality-slides.pptx) <br> [Slides 3](https://github.com/UofT-DSI/sampling/blob/main/lectures/11-Respondent-driven%20sampling-slides.pptx)|  
| 6      |  Differential privacy, Ethics, Inequity  | [Sampling and Reproducibility in Python](https://github.com/UofT-DSI/sampling/blob/main/assessment/ASSIGNMENT%20-%20Sampling%20and%20Reproducibility.md) | [Slides 1](https://github.com/UofT-DSI/sampling/blob/main/lectures/14-Differential%20privacy-slides.pptx) <br> [Slides 2](https://github.com/UofT-DSI/sampling/blob/main/lectures/15-Ethics-slides.pptx) <br> [Slides 3](https://github.com/UofT-DSI/sampling/blob/main/lectures/16-Inequity-slides.pptx) | 


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
- [probability-cheatsheet-1](./04-resources/probability-cheatsheet-1.pdf)
- [probability-cheatsheet-2](./04-resources/probability-cheatsheet-2.pdf)
- [probability-cheatsheet-3](./04-resources/probability-cheatsheet-3.png)
- [CLT Demo](./04-resources/5.1-probability-clt-demo.py)
- [LLN Demo](./04-resources/5.1-probability-lln-demo.py)
- [Amazon Exercises](./04-resources/amazon-exercises.pdf)
- [Multiple Imputation Exercises](./04-resources/sampling-multiple-imputation-exerises.py)

### Videos
- [Survey Sampling Methods](https://www.youtube.com/watch?v=tuJnu8RAUuU)
- [Population vs Sample](https://www.youtube.com/watch?v=r-rFO_2NsgI)
- [Survey Margin of Error: What is it? How does it relate to sample size?](https://www.youtube.com/watch?v=nilZF1KmCg4)
- [Reproducibility in Research](https://www.youtube.com/watch?v=EvoVb_QLRK8)
- [Probability Playlist](https://www.youtube.com/playlist?list=PLC58778F28211FA19)



### How to get help
![image](/steps-to-ask-for-help.png)

<hr>

## Folder Structure

```markdown
|-- 01-slides
|-- 02-assignments
|-- 03-instructors
|-- 04-resources
|-- .gitignore
```

* **slides:** Course slides as PDF files
* **live-coding:** Notebooks from class live coding sessions
* **assignments:** Graded assignments
* **resources**: Contains additional resources
* **instructors:** Instructions for the Instructor on what to teach
* README: This file!
* .gitignore: Files to exclude from this folder, specified by the instructor

## Acknowledgements

Radu Craiu, and the Department of Statistical Sciences, suggested this course. Rohan Alexander managed its development. Annie Collins developed the materials intially.



