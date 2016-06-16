import math

def arps_hyp_rate(qi, di, b,t):
    return qi/((1.0+b*di*t)**(1.0/b))

def arps_hyp_cum(qi, q, di, b,t):
    return ((qi**b)/(di*(1.0-b)))**(qi**(1.0-b)-q**(1.0-b))

def arps_exp_rate(qi, di, b):
    return qi*math.e(-di)

def arps_exp_cum(qi, q, di, b,t):
    return qi/di*(1-math.e**(-di*t))