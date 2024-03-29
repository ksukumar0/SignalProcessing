#!/usr/bin/python
import numpy as np

from scipy.fft import fft, fftfreq, fftshift
# number of signal points
N = 400
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
phaseNoise = np.pi*(np.random.rand(N))
#phaseNoise = 0
y = np.exp(50.0 * 1.j * 2.0*np.pi*x + phaseNoise)
yf = fft(y)
xf = fftfreq(N, T)
xf = fftshift(xf)
yplot = fftshift(yf)
import matplotlib.pyplot as plt
plt.plot(xf, 1.0/N * np.abs(yplot))
plt.grid()
plt.show()
