
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

# Load data
AVP1 = np.loadtxt("outputErrorAVP1.txt", skiprows=1, delimiter=",")
noAVP1 = np.loadtxt("outputErrorNoAVP1.txt", skiprows=1, delimiter=",")

AVP2 = np.loadtxt("outputErrorAVP2.txt", skiprows=1, delimiter=",")
noAVP2 = np.loadtxt("outputErrorNoAVP2.txt", skiprows=1, delimiter=",")

# Plot
fig, ax = plt.subplots()

ax.loglog(noAVP1[:,0], noAVP1[:,1], 'o-', color='b', label=r'$p=1$, no AV')
ax.loglog(AVP1[:,0], AVP1[:,1], '^-', color='b', label=r'$p=1$, with AV')

ax.loglog(noAVP2[:,0], noAVP2[:,1], 'o-', color='r', label=r'$p=2$, no AV')
ax.loglog(AVP2[:,0], AVP2[:,1], '^-', color='r', label=r'$p=2$, with AV')

ax.legend(loc='center right', bbox_to_anchor=(0.96, 0.52))

# --- Add slope lines ---

def add_slope_segment(ax, x1, x2, y_ref, m, color, text_offset=1.3):
    """
    Draws a slope line from x1 to x2 starting at y_ref * (x/x1)^m.
    Places the m=... label above the center of the line.
    """
    xs = np.array([x1, x2])
    ys = y_ref * (xs / x1)**m
    ax.plot(xs, ys, '--', linewidth=1, color=color)

    # Add label at center of the segment
    x_text = np.sqrt(x1 * x2)
    y_text = y_ref * (x_text / x1)**m * text_offset
    ax.text(x_text, y_text, f"$m = {m}$", ha='center', va='bottom', color=color)

# --- Slope for p=1 ---
x1_p1, x2_p1 = noAVP1[-2:, 0]
y1_p1, y2_p1 = noAVP1[-2:, 1]
ymin_p1 = min(y1_p1, y2_p1)

# Place slightly below
y_ref_p1 = ymin_p1 * 0.4
add_slope_segment(ax, x1_p1, x2_p1, y_ref_p1, m=2, color='b')

# --- Slope for p=2 ---
x1_p2, x2_p2 = AVP2[-2:, 0]
y1_p2, y2_p2 = AVP2[-2:, 1]
ymax_p2 = max(y1_p2, y2_p2)

# Place slightly above
y_ref_p2 = ymax_p2 * 3
add_slope_segment(ax, x1_p2, x2_p2, y_ref_p2, m=4, color='r')

ax.set_xlabel(r"DOF$^{-1/2}$")
ax.set_ylabel(r"Relative error")

fig.savefig("outputError.pdf", bbox_inches='tight')

###################################

figp1, axp1 = plt.subplots()

axp1.loglog(noAVP1[:,0], noAVP1[:,1], 'o-', color='b', label=r'$p=1$, no AV')
axp1.loglog(AVP1[:,0], AVP1[:,1], '^-', color='b', label=r'$p=1$, with AV')

axp1.set_xlim(ax.get_xlim())
axp1.set_ylim(ax.get_ylim())

axp1.legend(loc=(ax.get_legend())._loc)

# --- Slope for p=1 ---
x1_p1, x2_p1 = noAVP1[-2:, 0]
y1_p1, y2_p1 = noAVP1[-2:, 1]
ymin_p1 = min(y1_p1, y2_p1)

# Place slightly below
y_ref_p1 = ymin_p1 * 0.4
add_slope_segment(axp1, x1_p1, x2_p1, y_ref_p1, m=2, color='b')

axp1.set_xlabel(r"DOF$^{-1/2}$")
axp1.set_ylabel(r"Relative error")

figp1.savefig("outputErrorP1only.pdf", bbox_inches='tight')

plt.show()