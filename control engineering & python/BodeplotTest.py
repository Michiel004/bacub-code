from pylab import *
def H(w):
   ...:     wc = 4000*pi
   ...:     return 1.0 / (1.0 + 1j * w / wc)
   ...: 
    f = logspace(1,5) # frequencies from 10**1 to 10**5
    plot(f, 20*log10(abs(H(2*pi*f)))); xscale('log')