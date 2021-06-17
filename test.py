import math 
def fun_Lq(tau_, lambda_, K):
    mu_ = 1/tau_
    rho_ = lambda_/(K*mu_)
    P_0 = 0
    for i in range(K):
        P_0 += 1 / (math.factorial(i)) * math.pow(lambda_/mu_, i)
    P_0 += 1/math.factorial(K) * (1/(1-rho_)) * math.pow(lambda_/mu_, i)
    P_0 = 1 / P_0
    L_M = math.pow(K * rho_, K) * rho_ /(math.factorial(K)*math.pow(1 - rho_, 2)) * P_0
    
    return L_M/2

fun_Lq(10, 0.09*2, 2)