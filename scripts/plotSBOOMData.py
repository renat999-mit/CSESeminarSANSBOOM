
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

noiseError = np.loadtxt("sBOOMNoiseError.txt", delimiter=",")

fig, ax = plt.subplots()

ax.loglog(noiseError[:,0], noiseError[:,1], 'o-', color='b')
ax.axhline(1e-2, ls='dashed', lw=0.6, color='k')
ax.axvline(1e10, ls='dashed', lw=0.6, color = 'k')
ax.set_ylabel(r"Approximate error [dB]")
ax.set_xlabel(r"DOF, (nPoints $\times$ nSteps)")
fig.savefig("errorInNoise.pdf", bbox_inches='tight')

sensiError = np.loadtxt("sBOOMSensitivityError.txt", delimiter=",")

fig, ax = plt.subplots()

ax.loglog(sensiError[:,0], sensiError[:,1], 'o-', color='b')
ax.axhline(1e-2, ls='dashed', lw=0.6, color='k')
ax.axvline(1e10, ls='dashed', lw=0.6, color = 'k')

# Extract the last two points
x1, x2 = sensiError[-2, 0], sensiError[-1, 0]
y1, y2 = sensiError[-2, 1], sensiError[-1, 1]

# Compute slope in log-log space
slope = np.log10(y2 / y1) / np.log10(x2 / x1)

# Start at last point
x_start = x2
y_start = y2

# End at x = 3e10
x_end = 5e10
y_end = y_start * (x_end / x_start) ** slope

# Plot extension line
ax.plot([x_start, x_end], [y_start, y_end], linestyle='--', linewidth=0.7, color='b')

plt.show()
