import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats

#generating a random Data set
ini_size=100
x=np.zeros(ini_size)
for i in range(ini_size):
    x[i]=random.uniform(0,1)

dof=10
y=np.zeros(dof)
for i in range(dof):
    y[i]=x[random.randrange(0,ini_size,1)]
    

#Sampling points using some Monte-Carlo method
'''y=[]
for i in x:
    j=random.uniform(0,1)
    if j<0.3:
        y.append(i)'''

#print(len(y))
#sample size and degrees of freedom
num_samp=100
dof=len(y)
stds=0.01

#Defining the random variate
X=np.zeros((num_samp,dof))
for i in range(dof):
    #for expo
    #X[:,i] = stats.expon.rvs(scale=y[i], size=num_samp)
    #for lognorm
    X[:,i] = stats.lognorm.rvs(stds, loc=0, scale=np.exp(y[i]), size=num_samp) 

#Standardization

'''Z = (X - y) / y''' #For exponential
Z=(np.log(X) - y) / stds #For lognormal

#Converting the distribution to a chi-squared distribution

chi=np.sum(Z**2, axis=1)
#plotting
p=plt.hist(chi, bins=50, density=True, alpha=0.5, color='w', edgecolor='black', label='Chi-squared Distribution')
freq,bins=p[0],p[1]
bin_mid=0.5*(bins[:-1]+bins[1:])
freq_theory=stats.chi2.pdf(bin_mid, dof)

plt.plot(bin_mid, freq_theory, 'black', lw=2, label='Theoretical Chi-squared Distribution')

plt.title('Chi-squared Distribution with {} degrees of freedom'.format(dof))
plt.xlabel('Chi-squared Value')
plt.ylabel('Probability Density')
plt.legend()    
plt.savefig("Lognorm_Chi_Dof{}.jpg".format(dof))
plt.show()

        
