# Write a program that will predict your new mean
# and variance given the mean and variance of your
# prior belief and the mean and variance of your
# motion. 

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

print predict(10., 4., 12., 4.)
