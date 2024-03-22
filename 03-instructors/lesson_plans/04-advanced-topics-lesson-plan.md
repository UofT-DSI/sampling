# Module 5: Sampling

## Lesson 4: Advanced Topics

### Estimated Time: 5 hours

### Concepts:
- Snowball sampling
- Hidden populations
- Sample size estimation
- Multi-phase sampling
- Multiple imputation
- Random number generators
- Reproducibility

### Lesson Description:
This lesson explores more advanced topics in sampling and data analysis. We explore different variations of multi-stage sampling ways to make our sampling more effective and discussions on reproducibility in research.

### Instructor Preparation:
- Read over slides and Salganik and Heckathorn (2004)

## Course Preparation

### Materials and Resources
- Slides
  - 11-Respondent-driven sampling-slides
  - 12-Advanced data collection-slides
  - 13-reproducibility-slides
- Key texts
  - [Salganik M. J. & Heckathorn D. D. (2004). 5. Sampling and Estimation in Hidden Populations Using Respondent-Driven Sampling. Sociological Methodology 34(1) 193–240.](https://journals.sagepub.com/doi/10.1111/j.0081-1750.2004.00152.x)
  - Stef van Buuren & Karin Groothuis-Oudshoorn (2011). mice: Multivariate Imputation by Chained Equations in R. Journal of Statistical Software 45(3) 1-67. DOI 10.18637/jss.v045.i03.

### Learning Goals
- Calculate asymptotically unbiased estimates of populations proportions through respondent-driven sampling
- Write reproducible sampling simulations in Python

## Lesson Content & Instructor Notes

### 11-Respondent-driven sampling

- **Introduction (20 minutes)**
  - Review previous day’s concepts
  - Make sure students have access to Salganik and Heckathorn (2004). Give them 10 minutes to skim over the article.
- **Lesson (60 minutes)**
  - 11-Respondent-driven sampling-slide
> **Instructor Notes**: 
> - These slides involve walking through long calculations which could be improved by following along on a whiteboard or iPad.

---

### 12-Advanced data collection

- **Lesson (60 minutes)**
  - 12-Advanced data collection-slides
  - DSI-Sampling-Multiple Imputation Exercises
- **Exercises (30 minutes)**
  - Have students work through their own multiple imputation workflow with another data set. Additional data can be found [here under “Datasets”](https://amices.org/mice/reference/index.html). For Python, many exist in sklearn.datasets, seaborn, statsmodels.api, etc.
> **Instructor Notes**: 
> - Prompt students to pull up Python documentation for functions and follow along with slides identifying any additional arguments of interest. 
> - Go through slides and then demo Python or have students follow along.

---

### 13-Reproducibility

- **Assessment (60 minutes)**
  - assignment-sampling-and-reproducibility
    - [Blogpost](https://andrewwhitby.com/2020/11/24/contact-tracing-biased/)
- **Lesson**
    - 13-reproducibility-slides
- **Discussion (30 minutes)**
  - Reflect upon the data documentation assignment from Lesson 2. Where do you think the articles considered are lacking in terms of their documentation and reproducibility? What would need to change or improve for the data collection process to be reproducible?
> **Instructor Notes**: 
> - Instructions are in the md file. Have students read blogpost and work through whitby_covid_tracing. Assignment may take more or less time depending on familiarity with Python. 
> - Might be good to demo set.seed in Python in addition to static output provided on slides.
