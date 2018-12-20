import numpy as np
import math

def f(mu, sigma2, x):
    return 1/np.sqrt(2 * np.pi * sigma2) * np.exp(-0.5 * np.square(x-mu) / sigma2)

print(f(10., 4., 8.))
print(f(10., 4., 10.)) # f(x) is max when mu and x are same, maximizing the gaussian
