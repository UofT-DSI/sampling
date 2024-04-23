---
marp: true
theme: dsi-certificates-theme
_class: invert
paginate: true
---

# Sampling: Inequity

```code
$ echo "Data Science Institute"
```
---

# Key Texts

- James, A. (2008). Making Sense of Race and Racial Classification. In T. Zuberi & E. Bonilla-Silva (Eds.), *White logic, white methods : Racism and methodology * (pp. 31-45). Rowman & Littlefield Publishers.
- Harnois, C. (2018). Analyzing race and ethnicity with the GSS. In *Analyzing inequalities: An introduction to race, class, gender, and sexuality using the general social survey* (pp. 65-96). SAGE Publications, Inc., *[https://dx.doi.org/](https://dx.doi.org/)*
- Ashok, S. (2016, August 27). The rise of the American ‘Others’. The Atlantic. *[https://www.theatlantic.com/politics/archive/2016/08/the-rise-of-the-others/497690/](https://www.theatlantic.com/politics/archive/2016/08/the-rise-of-the-others/497690/)*
...

---

# Key Texts (continued...)

- Krause, H. (2021, August 27). We need to fill in the blanks in our social identity data. *We All Count* . *[https://weallcount.com/2021/08/27/we-need-to-fill-in-the-blanks-in-our-social-identity-data/](https://weallcount.com/2021/08/27/we-need-to-fill-in-the-blanks-in-our-social-identity-data/)*
- Krause, H. (2020, December 4). No one is an asterisk . *We All Count* . *[https://weallcount.com/2020/12/04/no-one-is-an-asterisk/](https://weallcount.com/2020/12/04/no-one-is-an-asterisk/)*
- Krause, H. (2020, June 26). Proxy variables part 2: race. *We All Count* . https://weallcount.com/2020/06/26/proxy-variables-part-2-race/

---

# Race in Surveys

---

# Discussion Questions

1. What is race?
2. What may be contributing factors to how we perceive racial identity in others and ourselves?
3. How many races are there? What are they?
4. What are the differences between race, ethnicity, and nationality?
5. How might our definitions of racial categories change across time and space?

---

# Race

- What is **race** ?
  - Race broadly refers to a group of humans that share common characteristics
    - Skin colour
    - Hair type
    - Facial features
    - Language
    - Religion
    - Cultural practice
    - Geographic origin
  - In the modern day, generally accepted to be a social construct with no biological validity

<!--
https://www.britannica.com/topic/race-human/The-history-of-the-idea-of-race
-->

---

# Ethnicity

- What is **ethnicity**?
  - Generally encompasses more than race
  - More often associated with cultural expression, cultural identity, and national/regional origin
  - Ethnicity can often specify subgroups within certain broader racial classifications
    - People who identify racially as “white” may identify ethnically as Turkish, Mexican, French Canadian, Ashkenazi Jew, etc. or a combination of multiple distinct ethnic groups

<!-- 
https://www.livescience.com/difference-between-race-ethnicity.html: Ethnicity has been used to oppress different groups, as occurred during the Holocaust, or within interethnic conflict of the Rwandan genocide, where ethnicity was used to justify mass killings. Yet, ethnicity can also be a boon for people who feel like they're siloed into one racial group or another, because it offers a degree of agency, Ifekwunigwe said. 
-->

---

# Race in Surveys

- Data on race and ethnicity are needed to track demographic shifts in populations and inequalities between members of different groups
- Desire to identify and quantify the influence of race without oversimplifying or essentializing
- However, data on race can also be used to perpetuate inequalities in the wrong hands

**How do we ask about and measure race?**

---

# Racial Classifications

> “Because race is a socially constructed concept with no fixed reality, all classification efforts are fraught with imprecision. Classification schemas are always a set of imperfect choices made in response to a given set of political agendas and imperatives. The institutionalization of these choices over the long run always has the effect of ‘naturalizing’ particular understandings of race. That is why there generally has been a great deal of struggle associated with changes in census classification, and why it is necessary to interrogate change and continuities in categorization”

> – Angela James, “Making Sense of Race and Racial Classification” in *White Logic, White Methods: Racism and Methodology*

---

# Racial Classifications

- Identification
  - Most surveys allow respondents to self-identify in response to questions about race
  - In the past, race has been indicated by researchers based on appearance or observed lifestyle
    - On the US census, race was recorded by surveyors until 1960
    - On the US General Social Survey, race was recorded through interviewer observation until 2000. Interviewers were instructed to ask respondents of their race only if they were in doubt.
- Race versus ethnicity
  - Depending on the context of the study, one measure may be more informative than the other
  - Both can provide useful insight

---

# Racial Classifications

- Asking the question
- What type of question should be used?
  - Open ended, “pick one”, “pick many”
- How many options should be given? What are the options?
- How can this data be analyzed?
  - Open ended: How can information be extracted from responses and meaningfully categorized and quantified?
  - “Pick one”: How can we properly account for mixed race individuals?
  - “Pick many”: How can we analyze many unique combinations of races, particularly those that pertain to small numbers of respondents? If we are looking for information about one race, to what extent do mixed race individuals enter into our analyses?

---

# Case Study: France

- In France, it is **prohibited to collect data relating to the race or ethnic origin of a person** through official government statistical programs, namely those conducted by the *Institut national de la statistique et des études économiques* and the Ministerial Statistical Departments
- Article 1 of the Constitution states: “France shall be an indivisible, secular, democratic and social Republic. It shall ensure the equality of all citizens before the law, without distinction of origin, race or religion. It shall respect all beliefs.”

<!-- 
- https://www.insee.fr/en/information/2388586
- https://www.conseil-constitutionnel.fr/en/decision/2007/2007557DC.htm
- https://www.constituteproject.org/constitution/France_2008.pdf?lang=en 
-->

---

# Case Study: US Census

![](./images/16_case_study_us_census.png)

<!-- 
https://www.census.gov/programs-surveys/decennial-census/decade.2020.html 
-->

---

# Case Study: Canadian Census

![](./images/16_case_study_canadian_census.png)

<!--
2021
- https://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvInstrumentList&Id=1283315
- https://www12.statcan.gc.ca/census-recensement/2021/ref/questionnaire/index-eng.cfm

- Note that the Canadian census never explicitly asks about an individual’s race. Data points from question 25 appear as “visible minority status”. Ethnicity and indigenous identity are similarly asked on the Canadian GSS.

- How many options are there?
- What are the options?
- How do these compare to the US census? What might be the reason for the differences? 
-->

---

# Equity Considerations in Collecting and Using Data about Race

---

# Collecting and Using Data about Race

- Use racial and ethnic categories that are meaningful for your target population
  - Different target populations may benefit from different categorizations for racial or ethnic identities in survey questions
    - For example, if you know your sample is predominantly Indigenous peoples, one “Indigenous” ethnic category will not provide much additional data
  - Use clusters or strata that are relevant to your target population
  - Test surveys in advance
  - Consult target population or available resources for best practices

<!-- 
Often clusters or strata are geographic in nature. Show and discuss https://native-land.ca/ as an example of strata relevant to specific ethnic groups. 
-->

---

# Collecting and Using Data about Race

- Think critically about the “Other: Please specify” option
  - Allowing respondents to select “Other” as a racial/ethnic identity is useful for those who fall outside of set racial categories
  - High number of “Other” responses may indicate that options provided are too limited and may render analysis less useful
  - Responses to “Please specify” can indicate more categories or further clarification that should be provided

<!--
https://www.theatlantic.com/politics/archive/2016/08/the-rise-of-the-others/497690/
-->

---

# Collecting and Using Data about Race

- Allow respondents to self-identify
  - Race is complex and unlikely to be perceived fully accurately by an interviewer
  - Self-identification allows respondents agency over how their identity is reported in data sets

---

# Collecting and Using Data about Race

- Provide background on how questions about racial or ethnic identity were asked
  - All choices and considerations that have gone into creating questions concerning race should be communicated to data users
  - Consider the following examples from Krause (2020):
    - 25% of students are Black
    - 25% of students self-identified as Black from a list of “Black, Hispanic, White, Mixed Race, Asian, Indigenous, Other, Prefer Not To Say”, created by the University admissions department in consultation with a student advisory panel.
    - 25% of students were counted by their teachers as Black from a provided choice of “White, Black, or Other”, suggested in a staff meeting.

<!-- 
https://weallcount.com/2021/08/27/we-need-to-fill-in-the-blanks-in-our-social-identity-data/
-->

---

# Collecting and Using Data about Race

- Where possible, report data for all racial and ethnic categories even when sample size is small
  - Often estimates for small sub-populations are supressed due to small sample size
  - Suppressing data for small sub-populations can perpetuate marginalization
  - Instead consider reporting sample size and reliability levels (standard deviation, coefficient of variation, confidence interval, etc.) so that results for all groups can be disseminated

<!-- 
https://weallcount.com/2020/12/04/no-one-is-an-asterisk/
-->

---

# Collecting and Using Data about Race

- Investigate the social circumstances for the differences between racial or ethnic groups in data sets
  - Race often serves as a proxy variable for a variety of social, cultural, historical, political, etc. circumstances that create inequalities
  - Providing broader context shifts responsibility from racialized groups to systems of oppression
  - Avoid simply controlling for race as a demographic variable

<!--
https://weallcount.com/2020/06/26/proxy-variables-part-2-race/
-->

---

# References

- Takezawa, Y. I. , Smedley, . Audrey and Wade, . Peter (2020, November 23). race. Encyclopedia Britannica. *[https://www.britannica.com/topic/race-human](https://www.britannica.com/topic/race-human)*
- Bryce, E. (2020, February 8). What’s the difference between race and ethnicity?. Live Science. *[https://www.livescience.com/difference-between-race-ethnicity.html](https://www.livescience.com/difference-between-race-ethnicity.html)*
- Institut national de la statistique et des études économiques (2016, September 9). Ethnic-based statistics. *[https://www.insee.fr/en/information/2388586](https://www.insee.fr/en/information/2388586)*
- Conseil constitutionnel (2007, November 15). Decision no. 2007-557 DC of 15 November 2007. *[https://www.conseil-constitutionnel.fr/en/decision/2007/2007557DC.ht](https://www.conseil-constitutionnel.fr/en/decision/2007/2007557DC.htm)*

...

---

# References (continued...)

- U.S. Census Bureau (2020). *2020 Decennial Census Questionnaire.* https://www.census.gov/programs-surveys/decennial-census/technical-documentation/questionnaires.2020_Census.html
- U.S. Census Bureau (2010). *2010 Decennial Census Questionnaire.* https://www.census.gov/programs-surveys/decennial-census/technical-documentation/questionnaires.2010_Census.html
- Statistics Canada (2021). *2021 Census of Population, Form 2A-L* . https://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvInstrumentList&Id=1283315

