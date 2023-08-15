import numpy as np
import matplotlib.pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# Random data points between 0 and 1
data = np.random.choice([0, 1], size=(5, 7, 9), p=[0.65, 0.35])

# Create a new figure
fig = plt.figure()

# Axis with 3D projection
ax = fig.add_subplot(projection='3d')   # ax = fig.gca(projection='3d') gca method doesnot have projection argument

# Plot the voxels
ax.voxels(data, edgecolor="k", facecolors='gray')

# Display the plot
plt.show()
