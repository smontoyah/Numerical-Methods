
# integracion gaussiana
def gauss(npts, a, b):
    eps = 3.E-14                    # Accuracy: ADJUST!
    m = (npts  +  1)//2             # simetria calcula mitad de raices
    print("m vale ",m)
    for i in range(1, m + 1):
        t = math.cos(math.pi*(i - 0.25)/(npts  +  0.5)) 
        t1 = 1 
        while( (abs(t - t1) ) >=  eps):  # halla raices (Newton)
            p1 = 1. ;  p2 = 0.           # primeros polinomios
            for j in range(1, npts + 1):
                p3 = p2;   p2 = p1 
                p1 = ( (2.*j - 1)*t*p2 - (j - 1.)*p3)/j # recurrencia
            pp = npts*(t*p1 - p2)/(t*t - 1.)            # derivada de Pn(x)
            t1 = t
            t = t1  -  p1/pp
        x[i-1] =  - t
        x[npts - i] = t 
        w[i - 1] = 2./( (1. - t*t)*pp*pp) 
        w[npts - i] = w[i - 1]                 # pesos, simetricos
        
    for j in range(0, npts):
            x[j] = x[j]*(b - a)/2.  +  (b  +  a)/2.  # escala a [a,b]
            w[j] = w[j]*(b - a)/2.                   # escala a [a,b]
    return x,w                                       # devuelve pesos
