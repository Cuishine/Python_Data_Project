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