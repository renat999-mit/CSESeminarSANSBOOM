import numpy as np
import matplotlib.pyplot as plt

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

dataSANS = np.loadtxt('nearfieldAdjoint.txt')
dataSANS = np.unique(dataSANS[np.argsort(dataSANS[:, 0])], axis=0)

maxSens = np.max([np.abs(sens) for sens in dataSANS[:,1]])

fig, ax = plt.subplots()

ax.plot(dataSANS[:,0], dataSANS[:,1]/maxSens, color = 'k')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Normalized $d\mathcal{J}_{BSEL}/dP_{nf}$')
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)

fig.savefig("loudnessSensistivity.pdf", bbox_inches='tight')

plt.show()