# import needed libraries
import numpy as np
import matplotlib.pyplot as plt

# Create a 100*100 array, every number is 0
# 0:suspectible 
population=np.zeros((100,100))
#randomly select the x and y of the outbreak of the infectious disease
outbreak=np.random.choice(range(100),2)
# 1:infected 
population[outbreak[0],outbreak[1]]=1

# Set the time for the disease spread
time=100
# Set the possibility of infection and recovery
# the probability of a susbectible person being infected
beta=0.3
# the probability of an infected person recovering
gamma=0.05

# Show the initial image of the first infected person
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Initial State')
plt.show()

# Set a list to insure we finally get images from the specific times 
Display=[10,50,100] 

#Set all infected individuals in the array to have a value of 1
for T in range(time):
  infected=np.argwhere(population == 1)
    
  for idx in infected:
      i,j=idx
      for x,y in [(i+1,j),(i-1,j),(i+1,j+1),(i+1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1)]:
# Evaluate if the spots around infected people are in the array
# Evaluate if the people around the infected one are suspectible  
        if 100>x>0 and 100>y>0 and population[x,y] == 0:
# Decide if the person will be infected.        
# If a random number between 0 and 1 is less than gamma, the person will recovered           
          if np.random.rand()<beta:
            population[x, y] = 1

# Decide if infected people will recover. 
  for m,n in infected:
# If a random number between 0 and 1 is less than gamma, the person will recovered       
         if np.random.rand()<gamma:
            population[m,n]=2

# Display the images in specific time roles. 
  if T + 1 in Display:
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time Step {T + 1}')
        plt.show()

    
                
    




