import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = np.random.rand(1000, 2) * 150
km = KMeans(n_clusters=3, init="random")
km.fit(data)
centers = km.cluster_centers_
labels = km.labels_
print("Cluser centers: ", *centers)
# print("Cluser Labels: ", *labels)
colors = ["r", "g", "b"]
markers = ["+", "x", "*"]
for i in range(len(data)):
  plt.plot(data[i][0], data[i][1], color=colors[labels[i]],
marker=markers[labels[i]])
plt.scatter(centers[:, 0], centers[:, 1], marker="s", s=100,linewidths=5)
plt.show()
