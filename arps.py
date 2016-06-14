import math

def arps_hyp(qi, di, b,t):
    return qi*(1.0-b*di*t)**(-1.0/b)

def arps_exp(qi, di, b,t):
    return qi*math.e(di*t)