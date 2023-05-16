
index = 45

link = "https://writing9.com/text/5ec80ab475f0910018dec589"

topic = """\
It is thought by some that it is better to live in a city while others believe that life is better in the countryside. Discuss both side and give your opinion.\
"""

essay = """\
Many people have many perspectives about where to live. Although some might say that living in urban is more convenient, others think that there are too many chaotic and pollution. This essay will explore advantages and disadvantages of both places and give an opinion at the end.

Nowadays, lots of major cities are facing with congested traffic because most of residents are dependent on their private car and commute to work where is their workplace located. Therefore, there are a lot of air pollution in the heart of the town and not only this but also too much noisy, especially during rush hour. However, somebody choose to rent or buy a condominium which is located in the right center of cities as this place is nearby their company and there are plenty of the convenient shopping malls and entertainment places, such as a cinema, a restaurant, a fitness center and so on.

In contrast, some families decide to live on the outskirts as it is more quiet and more fresh air, so they can have a better quality of living than stay inside the city which is fully of crowds. On the other hand, these groups may have to battle through the traffic problems as they need to travel to work.

To sum up, there are pros and cons between living in an urban and countryside. People have many options to decide whether which place is suite them. In my view, I think living in the city is the best option as we can go to work easily.\
"""




with open(f"essay_{index}.txt", "w") as f:
    f.write(f"""Topic:\n\n"{topic}"\n\nEssay:\n\n"{essay}"\n
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

