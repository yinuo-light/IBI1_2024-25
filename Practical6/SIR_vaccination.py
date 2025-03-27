# import needed libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def cal(V):
    N=10000
    beta=0.3
    gamma=0.05
    time=1000
    infected=1
    vaccinated=N*V
    recovered=vaccinated
    suspectible=N-infected-vaccinated
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
     P=str(int(V*100))
    return I, P


V=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
for a in V:
  I,P=cal(a)
  plt.plot(I, label=f'Vaccination rate: {P}%')
  
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('SIR Model')
plt.xlim(0, 1000)
plt.legend()
plt.show()