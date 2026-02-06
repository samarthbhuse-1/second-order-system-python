import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

wn = 5
zeta = 0.5

num = [wn**2]
den = [1, 2*zeta*wn, wn**2]

system = signal.TransferFunction(num, den)
t, y = signal.step(system)

plt.plot(t, y)
plt.title("Second Order System Step Response")
plt.xlabel("Time")
plt.ylabel("Output")
plt.grid()
plt.show()

