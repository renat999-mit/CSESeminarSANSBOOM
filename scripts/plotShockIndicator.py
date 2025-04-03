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

xi_1 = 0.0025
def s_grad(xi_hat, p):
  xi_1 = 0.00125
  k = 1e4 * xi_1
  if p == 1:
    alpha = 0.45
  else:
    alpha = 0.625

  return xi_hat * (np.tanh(p**2 * xi_hat))**(p-1) / (1 + np.exp(-k * (xi_hat - alpha)))

xi_hat = np.linspace(0,1.25,1000)

fig, ax = plt.subplots()

ax.plot(xi_hat, xi_hat, lw = 0.85, ls = 'dashed', label = r'Linear reference', color = 'orange')
ax.plot(xi_hat, s_grad(xi_hat, 1), label = r'$s_{grad}(\hat{\xi})$, $p=1$', color = 'b')
ax.plot(xi_hat, s_grad(xi_hat, 2), label = r'$s_{grad}(\hat{\xi})$, $p=2$', color = 'r')
ax.axvline(1, lw = 0.5, ls = 'dashed', color = 'k')
ax.axhline(1, lw = 0.5, ls = 'dashed', color = 'k')

ax.set_xlim(0,1.25)
ax.set_ylim(-0.05,1.25)

ax.set_xlabel(r'$\hat{\xi}$')
ax.set_ylabel(r'$s_{grad}(\hat{\xi})$')

ax.legend()

fig.savefig('s_grad.pdf', bbox_inches='tight')

plt.show()