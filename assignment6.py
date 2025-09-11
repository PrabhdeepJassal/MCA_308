import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
iris = load_iris()
X = iris.data 
y = iris.target 
target_names = iris.target_names

X_std = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_std)
df_pca = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
df_pca['target'] = y

plt.figure(figsize=(8,6))
colors = ['red', 'green', 'blue']
for i, target in enumerate(np.unique(y)):
    plt.scatter(df_pca.loc[df_pca['target'] == target, 'PC1'],
                df_pca.loc[df_pca['target'] == target, 'PC2'],
                color=colors[i],
                label=target_names[i],
                alpha=0.7,
                edgecolors='k')

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA of Iris Dataset (2D Projection)")
plt.legend()
plt.grid(True)
plt.show()
print("Explained variance ratio:", pca.explained_variance_ratio_)
