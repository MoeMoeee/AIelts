
index = 27

link = "These days, people work in more than one job, and often change career several times during their life. What are the advantages and disadvantages of this?"

topic = """
These days, people work in more than one job, and often change career several times during their life. What are the advantages and disadvantages of this?
"""

essay = """
People often tended to have a fixed job that could last for their lifetime in the past, but it is changed now. For many individuals, job change has been their purpose in life nowadays. In this essay, I will outline what I consider to be some positive and negative parts of this trend.

Certainly, there are several key benefits stemming from changing jobs frequently. One of them is to gain more experience in a different environment. In one company, for example, the longer an employee works, the more routined tasks are. Thus, moving to a new organisation can allow the worker to learn a different thing. Another key benefit is that people may get higher pay in a new job. It is reported that the pay may rise up to 30% for those who choose to move on with a new entity, while, in contrast, it is only 10% for a regular annual salary increment. Clearly, changing jobs is very attractive. 

However, it does have its limitations. Job-hopping can be difficult because people need to start afresh. They need to go through a probation period many times, learning the basics and gradually involving in an important project if a manager believes in their abilities and values. I myself, for instance, took 2 years to understand and master a new career but finally quit to return to the previous company due to stress. In addition to this difficulty, the person may end up unemployed if they fail to pass the probation or if they cannot get along with their new colleagues. If they cannot find a new job to continue, it ultimately creates a financial issue as well. 

In conclusion, having a job changed is a choice of each person for their future career and better life. If anyone decides to move on with a new career, it is better for them to take some time to consider all potential problems and be well-prepared to overcome them.
"""




with open(f"essay_{index}.txt", "w") as f:
    f.write(f"""Topic:\n{topic}\nEssay:\n{essay}
Revised:\n\nFeedback:\n\nTask Response:\n\nCoherence and Cohesion:\n
Lexical Resource:\n\nGrammatical Range and Accuracy:\n\nScore:""")
    
with open('assets/essay_sample', 'a') as f:
    f.write(f"""\n\n
############################################################################

{index}.
Link: {link}

Topic:\n{topic}
Essay:\n{essay}
""")
