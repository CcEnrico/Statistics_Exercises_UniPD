import scipy.special as special
from scipy.stats import binom


# calcolo della beta derivata 
def ibeta_derivative(a, b, x, h=1e-5):
    fx = special.betainc(a, b, x)
    fx_plus_h = special.betainc(a, b, x + h)

    derivative = (fx_plus_h - fx) / h

    return derivative

# La funzione di massa di probabilità una funzione che associa a ciascun valore di una variabile aleatoria discreta
# la probabilità che la variabile aleatoria assuma quel valore. 
# fonte: <boost/math/distributions/binomial.hpp> 
# Probability of getting exactly k successes
# if C(n, k) is the binomial coefficient then:
#
# f(k; n,p) = C(n, k) * p^k * (1-p)^(n-k)
#          = (n!/(k!(n-k)!)) * p^k * (1-p)^(n-k)
#          = (tgamma(n+1) / (tgamma(k+1)*tgamma(n-k+1))) * p^k * (1-p)^(n-k)
#          = p^k (1-p)^(n-k) / (beta(k+1, n-k+1) * (n+1))
#          = ibeta_derivative(k+1, n-k+1, p) / (n+1)
def pmf(n, k, p):

    ibeta_deriv = ibeta_derivative(k + 1, n - k + 1, p)
    
    pmf = ibeta_deriv / (n + 1)
    
    return pmf


def scipy_pmf(n, k, p):

    pmf_value = binom.pmf(k, n, p)
    return pmf_value


