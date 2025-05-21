# import needed libraries
import numpy as np
import matplotlib.pyplot as plt

# Set total population(N),infection rate(beta)，recovery rate(gamma),simulation time, 
N=10000
beta=0.3
gamma=0.05
time=1000

# initial infected number
infected=1
recovered=0
suspectible=N-infected

# Set nitialize lists S (for susceptible population)
# I (for infected population)
# R (for recovered population) 
S=[suspectible]
I=[infected]
R=[recovered]


for n in range (time+1):
    # Calculate new infections
    newinfected=suspectible*beta*(infected/N)
    # Calculate new recoveries
    newrecovered=infected*gamma
    # Update susceptible population and infected population 
    suspectible-=newinfected
    infected=infected+newinfected-newrecovered
    recovered+=newrecovered
    
    #Append the updated susceptible, infected, and recovered populations to the lists
    S.append(suspectible)
    I.append(infected)    
    R.append(recovered)

# Set up the plot
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S, label='Susceptible', color='blue')
plt.plot(I, label='Infected', color='red')
plt.plot(R, label='Recovered', color='green')
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.xlim(0, time)
plt.legend()
plt.savefig("SIR.png", format="png")
plt.show()