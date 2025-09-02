import numpy as np
from scipy.stats import norm
from math import exp, sqrt

def CallPayOff(S, X):
    return np.maximum(S - X, 0.0)
    
def PutPayOff(S, X):
    return np.maximum(X - S, 0.0)

def MCAsianCall(S0, X, r, v, T, N, M): 
    dt = T / N
    Ct = np.zeros(M) 
    St = np.zeros(N+1)
    nudt = (r - 0.5 * v * v) * dt
    sidt = v * sqrt(dt)
    
    for i in range(M):
        z = norm.rvs(size=N)
        St[0] = S0
        for j in range(1, N+1):
            St[j] = St[j-1] * exp(nudt + sidt*z[j-1])
        
        Ct[i] = CallPayOff(St[N], St.mean())
        
    callPrc = Ct.mean() * exp(-r * T)
        
    return callPrc
        
def main():
    S0 = 40.0
    X = 40.0
    r = 0.08
    v = 0.30
    T = 1.0
    N = 3
    M = 25000       
    
    prc = MCAsianCall(S0, X, r, v, T, N, M)  
    print("The Price of the Asian Call Option is : %s" % prc)
    
if __name__ == "__main__":
    main()
