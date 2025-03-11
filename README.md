# Overview

Welcome to my analysis of the data job market, focusing on data analyst roles. This project was created out of a desire to navigate and understand the job lmarket more effectively,

# The Questions
Below are the questions I want to answer in my project:

    1. What are the skills most in demand for the top 3 most popular data roles?
    2. How are in-demand shills trending for Data Analysts?
    3. How well do jobs and skills pay for Data Analysts?
    4. What are the optimal skills for data analysts to learn?( high Demand and High Paying)

# Tools I Used

for my deep dive into the dta analyst job market, I harnessed the power of several key tools:
    1. Python:  The backbone of my analysis
        Pandas library
        Matplotlib Library
        Seaborn Library



# The Analysis
Need to fill this in
## 1. What are the most demanded skills fro the top 3 most popular data roles?

To find the most demanded skills for the top 3 most populardata roles. I filtered out theose positions by which ones were the most popular, and got the top 5 skills for these top 3 roles. This query highlights the most popular job titles and their top skills, showing which skills I should pay attention to depending on the role I'm targeting.

To find the most demanded skills for the top 3 most popular data roles in the UK. I filtered out the locations in the UK and got the top 5 skills for these top 3 roles. This query highlights the most popular job titles in the UK and their top skills, showing which skills I should pay attention to depending on the role I'm targeting.

View my note book with detailed steps here: [2_Skill_Deand.ipynb](3_Project\2_Skill_Demand.ipynb)

### Visualize Data

```python
fig, ax = plt.subplots(len(job_titles),1)

for i, job_title in enumerate(job_titles):
    df_plot = df_skills_count[df_skills_count['job_title_short'] == job_title].head(5)
    df_plot.plot(kind='barh', x='job_skills', y='skill_count', ax=ax[i], title=job_title)

    ax[i].invert_yaxis()
    ax[i].set_ylabel('')
    ax[i].legend().set_visible(False)

fig.suptitle('Counts of Top Skills in Job Postings', fontsize=15)
fig.tight_layout(h_pad=0.5)
plt.show()
```


### Reaults

![Visualization of Top Skills for Data Nerds](3_Project\images\skill_demand_all_data_roles.png)


### Insights
- Python is a versatile skill, highly demanded across all three roles, but most prominently fro Data Scientists (72%) and jData Engineers (65%).
- SQL is the most Requested skill for kjData Analysts and Data  Scientists, with it in over half the job postings fro both roles. For Data Engineers, Python is the most sought-after skill, appearing in 68% of job postings.
- Data Engineers require more specialized technical skills (AWS, Azure, kSpark) compared to Data Analysts and Data Scientists who are expected to be proficient in more general data management and analysis tools (Excel, Tableau).

### Visulaize Data

``` pyhton

from matplotlib.ticker import PercentFormatter

df_plot = df_DA_US_persent.iloc[:, :5]

sns.lineplot(data=df_plot, dashes =False,palette="tab10", linewidth=2)
sns.set_theme(style="ticks", palette="pastel")
sns.despine()


plt.title('Trending Top Skills for Data Analyst in the US')
plt.ylabel('Likelihood in Job Posting')
plt.xlabel('2024')
plt.legend().remove()


ax = plt.gca()
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))


for i in range(5):
    plt.text(11.2, df_plot.iloc[-1, i], df_plot.columns[i])

plt.show()

```

### Results

![Trending Top Skills for Data Analysts in the US](3_Project\images\Skills_Trend.png)
*Line graph visualizing the Trending to skills for data analysts in the US in 2024.*

### Insights:

- SQL remains the most consistently demanded skill
- Excel experienced a significant increase in demand
- Both Python and Tableau show relatively stable demand
- Power BI is in the increase on demand


# The Analysis

## 3. How well do jobs and skills pay for Data Analysts?

### Salary Analysit for Data Nerds

#### Visualize Data

```python
sns.boxplot(data=df_US_top6, x='salary_year_avg', y='job_title_short', order=job_order, palette='viridis', hue='job_title_short', dodge=False)
sns.set_theme(style='ticks')

plt.title('Salary Distribution in the United States')
plt.xlabel('Yearly Salary ($USD)')
plt.ylabel('')
ax =plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'${int(x/1000)}K'))
plt.xlim(0,600000)
plt.show

```

# Results
![Salary distributions of Data Jobs in the US](3_Project\images\skills_Salary_Analysis.png)
*Box plot visualizing the salary distributions for the top 6data job titles.*

#### Insights

-There's a significant variation in salary ranges across different job titles. Senior Data Scientist positions tend to have the highest salary potential.

- Senior Data Engineer and Senior Data Scientist roles show a considerable number of outliers on teh higher end of the salary spectrum.

- the median salaries increase with the seniiority and specialization of the roles. Senior roles.

# Investigate Median Salary Vs Skill for Data Analysts



### Highest Paid & Most Demanded Skills for Data Analysts
#### Visualize Date


``` pyhton
# Top 10 Highest Paid Skills for Data Analysts
fig, ax = plt.subplots(2,1)

sns.set_theme(style="ticks")
#df_DA_top_pay[::-1].plot(kind='barh', y='median', ax=ax[0], legend=False)
sns.barplot(data=df_DA_Top_Pay, x='median', y=df_DA_Top_Pay.index, ax=ax[0], hue='median', palette='dark:b_r')


ax[0].set_title('Top 10 Hightest Paid Skills for Data Analysts')
ax[0].set_ylabel('')
ax[0].set_xlabel('')
ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${int(x/1000)}K'))
ax[0].legend().remove()

sns.set_theme(style="ticks")
#df_DA_skills[::-1].plot(kind='barh', y='median', ax=ax[1], legend=False)
sns.barplot(data=df_DA_skills, x='median', y=df_DA_skills.index, ax=ax[1],hue='median', palette='light:b')


ax[1].set_title('Top 10 Most In-Demand Skills for Data Analysts')
ax[1].set_ylabel('')
ax[1].set_xlabel('Median Salary (USD)')
ax[1].set_xlim(ax[0].get_xlim())
ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${int(x/1000)}K'))
ax[1].legend().remove()

fig.tight_layout()
plt.show()

``` 


```python
from adjustText import adjust_text

#df_plot.plot(kind='scatter',x='skill_percent', y='median_salary')
sns.scatterplot(data=df_plot, x='skill_percent', y='median_salary', hue='technology')

#sns.despine()
sns.set_theme(style='ticks')


plt.xlabel('Percent of Data Analyst Jobs')
plt.ylabel("Median Yearly Salary ($USD)")
plt.title('Most Optimal Skills for Data Analysts in the US')
plt.tight_layout()


texts = []

for i, txt in enumerate(df_DA_skills_high_demand.index):
   texts.append( plt.text(df_DA_skills_high_demand['skill_percent'].iloc[i], df_DA_skills_high_demand['median_salary'].iloc[i], txt))

adjust_text(texts, arrowprops=dict(arrowstyle="->", color='grey', lw=1))

from matplotlib.ticker import PercentFormatter

ax=plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, pos: f'${int(y/1000)}K' ))    
ax.xaxis.set_major_formatter(PercentFormatter(decimals=0)) 

plt.show()

```
![Most Optimal Skills for Data Analysts in the US ]()
*A scatter plot visualizing the most optimal skills ( high paying & high demand) for data analysts in the US.*


# The Analysis
## 4. What is the most optimal skill to learn fro Data Analysts?

#### Results
![Most Optimal Skills for Data Analysts in the US](3_Project\images\Optima_Skills.png)
* A scatter plot visualizing the most optimal skills ( high paying & high demand) fro data analysts in the US.*


