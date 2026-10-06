import numpy as np
import matplotlib.pyplot as plt
import random 
import scipy

def logLikeli(mu,sigma,x):
    if sigma <= 0:
        return -np.inf
    return -0.5*np.log(2*np.pi*sigma**2) - (x-mu)**2/(2*sigma**2)

x=np.random.normal(0,0.5,10000)

#mu_vals=np.arange(-1,1,0.1)
mu_vals=np.mean(x)
#sigma_vals=np.std(x)
sigma_vals=np.arange(0,2,0.1)

#Logli_vals=np.array([np.sum(logLikeli(i,sigma_vals,x)) for i in mu_vals])

Logli_vals=np.array([np.sum(logLikeli(mu_vals,i,x)) for i in sigma_vals])


a=np.argmax(Logli_vals)

#print(mu_vals[a],Logli_vals[a])
#print(mu_vals)
#print(mu_vals[a])



plt.figure(figsize=(10,7))
'''plt.title("Loglikelihood calculated for a Gaussian data with scanned over its mean")
plt.xlabel("mean values")'''
plt.title("Loglikelihood calculated for a Gaussian data with scanned over its standard deviation")
plt.xlabel("Standard Deviation values")
plt.ylabel("Loglikelihood values")
plt.plot(sigma_vals,Logli_vals)
plt.plot(sigma_vals[a],Logli_vals[a],'ro',label='maximum value of Loglikelihood')
plt.savefig("MaximalLikelihoodforstd.jpg")
plt.show()


# Attempt to calculate log-likelihood values for each combination of mu and sigma
'''
Logli_vals=np.zeros((len(mu_vals),len(sigma_vals)))

for i in range(len(mu_vals)):
    for j in range(len(sigma_vals)):
        Logli_vals[i,j]=np.sum(logLikeli(mu_vals[i],sigma_vals[j],a))

#print(Logli_vals)'''
        
       

