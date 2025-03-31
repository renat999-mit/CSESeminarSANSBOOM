import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

plt.rcdefaults()
plt.style.use('seaborn-v0_8-paper')
params = {
    "ytick.color" : "black",
    "xtick.color" : "black",
    "axes.labelcolor" : "black",
    "axes.edgecolor" : "black",
    "text.usetex" : True,
    "font.family" : "serif",
    "font.serif" : ["Computer Modern Serif"],
    "lines.linewidth" : 1,
    "lines.markersize" : 8,
    "font.size" : 12,  # General font size
    "axes.labelsize" : 14,  # Axes label font size
    "xtick.labelsize" : 14,  # X-axis tick label font size
    "ytick.labelsize" : 14,  # Y-axis tick label font size
    "legend.fontsize" : 12
}
plt.rcParams.update(params)

zvec = np.linspace(0,20e3,5000)

Tr = 288.15
L = -0.0065
zr = 11e3

pr = 101325
g = 9.81
R = 287.05

gamma = 1.4

def T(z):
  if z <= zr:
    return Tr + L*(z-zr)
  else:
    return Tr

def p(z):
  if z <= 11e3:
    return pr*(T(z)/Tr)**(-g/(R*L))
  else:
    return pr*np.exp(-g*(z-zr)/(R*Tr))

def rho(z):
  return p(z)/(R*T(z))

def c(z):
  return np.sqrt(gamma*R*T(z))

def ha(z):
  a00 = 1.00271
  a01 = -0.12223
  a02 = 0.04546
  a03 = -0.031545
  a04 = 0.0076472
  a05 = -0.00079906
  a06 = 0.000029429
  a10 = 1.8395e-20
  a11 = 5.44894
  a12 = -0.60683
  a13 = 0.0283643
  a14 = -0.000474746
  z /= 1000
  if z <= 11:
    return a00 * 10**(a01*z + a02*z**2 + a03*z**3 + a04*z**4 + a05*z**5 + a06*z**6)
  else:
    return a10 * 10**(a11*z + a12*z**2 + a13*z**3 + a14*z**4)

fig, ax = plt.subplots(1,3)

ax[0].plot([T(z) for z in zvec], zvec/1000, color = 'r')
ax[0].set_ylabel('$z$ [km]')
ax[0].set_xlabel('$T_0$ [K]')
ax[0].axhline(11, ls = 'dashed', lw = 0.75, color = 'k')

formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-0, 0))

ax[1].plot([p(z)/1000 for z in zvec], zvec/1000, color = 'r')
ax[1].set_xlabel('$p_0$ [kPa]')
ax[1].set_yticklabels([])
ax[1].axhline(11, ls = 'dashed', lw = 0.75, color = 'k')
# ax[1].xaxis.set_major_formatter(formatter)

ax[2].plot([ha(z) for z in zvec], zvec/1000, color = 'r')
ax[2].set_xlabel('$h_{a0}$')
ax[2].set_yticklabels([])
ax[2].axhline(11, ls = 'dashed', lw = 0.75, color = 'k')

plt.show()

fig.savefig("atmosphereStandard.pdf", bbox_inches='tight')