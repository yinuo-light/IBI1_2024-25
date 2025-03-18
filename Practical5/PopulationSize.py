#input the population size and regions' name in the UK in two lists
uk_countries=[57.11,3.13,1.91,5.45] 
uk_name=['England','Wales','Northern Ireland','Scotland']

#input the population size and regions' name in China in another two lists
China_countries=[65.77,41.88,45.28,61.27,85.15]
China_name=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu']
#print the sorted population of the countries in ascending order
print("Arrange the population of regions in th UK in ascending order:",sorted(uk_countries))
print("Arrange the population of regions in China in ascending order:",sorted(China_countries))

#draw a pie charts
import matplotlib.pyplot as plt
# The labels in the chart are from the list uk_name
labels=uk_name
# The population sizes in the chart are from the list uk_countries
sizes=uk_countries
# change the distance of each slice from the center of the pie chart
explode=(0,0.1,0,0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=100)
plt.axis('equal')
#give the graph a title
plt.title('UK population sizes')
#print the graph
plt.show()

# The procedures of the second graph are same as above
import matplotlib.pyplot as plt2
labels=China_name
sizes=China_countries
explode=(0,0,0,0,0.1)
plt2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt2.axis('equal')
plt.title('China population sizes')
plt2.show()