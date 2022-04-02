import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([20, 21, 22, 23, 24, 25])
features = ["Danceability", "Energy", "Acousticness", "Speechiness", "Liveness", "Valence"]
plt.xticks(x, features)
plt.plot(x, y)
plt.show()