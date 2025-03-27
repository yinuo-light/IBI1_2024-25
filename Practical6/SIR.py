# import needed libraries
import numpy as np
import matplotlib.pyplot as plt
N=10000
# import needed libraries
beta=0.3
# the probability of an infected person recovering
gamma=0.05
time=1000
infected=1
recovered=0
suspectible=N-infected

S=[suspectible]
I=[infected]
R=[recovered]

for n in range (time+1):
    newinfected=suspectible*beta*(infected/N)
    newrecovered=infected*gamma
    suspectible-=newinfected
    infected=infected+newinfected-newrecovered
    recovered+=newrecovered
    
    S.append(suspectible)
    I.append(infected)    
    R.append(recovered)

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