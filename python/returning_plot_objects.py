from matplotlib import pyplot as plt

def plot_dummy(ax):
    x, y = [x for x in range(10)], [x**2 for x in range(10)]
    out = ax.plot(x, y)
    return out

fig, axs = plt.subplots(2, 1)
plot_dummy(axs[0])
plot_dummy(axs[1])
plt.show()

# note: weird pylance error
fig, axs = plt.subplots(2, 2)
plot_dummy(axs[0, 0])
plot_dummy(axs[0, 1])
plot_dummy(axs[1, 0])
plot_dummy(axs[1, 1])
plt.show()