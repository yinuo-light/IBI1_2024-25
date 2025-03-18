#Let the users input the language they want to know the usage proportion of
language=input("Language name:")
#use the dictionary to record the information
popularity={'JavaScript':62.3, 'HTML':52.9, 'Python':51, 'SQL':51, 'TypeScript':38.5}
#returns the usage proportion of the language by checking the dictionary
print("The percentage of people using",language,"is",popularity[language],"%")

#To draw a bar graph
import matplotlib.pyplot as plt
import numpy as np
#draw a 5 columns bar graph
N=5
scores=(62.3, 52.9, 51, 51, 38.5)
ind=np.arange(N)
width=0.35
p1=plt.bar(ind, scores, width)
#provide other information of the graph
plt.ylabel('percentage')
plt.title('Programming language popularity')
plt.xticks(ind, ('JavaScript', 'HTML', 'Python', 'SQL', 'TypeScript'))
plt.yticks(np.arange(0,100,10))
#show the graph 
plt.show()
