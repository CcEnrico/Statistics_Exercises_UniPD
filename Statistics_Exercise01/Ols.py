import numpy as np

def least_squares(x,y):
    # calcola m,q usando metodo dei minimi quadrati
    # m = sum(x*y) - n*average(x)*average(y) / sum(x^2) - n*average(x)^2
    # q = average(y) - m*average(x)
    # y = q + mx
    # np.avarage(x) calcola la media campionaria di x
    m = (sum(x*y) - len(x)*np.average(x)*np.average(y))/(sum(x**2)- len(x)*np.average(x)**2)
    q = np.average(y) - m*np.average(x)
    return m,q

    



