import numpy as np
from scipy.spatial import distance
from sklearn.metrics import jaccard_score

# 1- Customer Preferences
customer_A = np.array([4, 5, 2, 3, 4])
customer_B = np.array([5, 3, 2, 4, 5])

customer_A_binary = np.array([1, 0, 1, 1, 0, 1])
customer_B_binary = np.array([1, 1, 1, 0, 0, 1])

euclidean_dist = distance.euclidean(customer_A, customer_B)
manhattan_dist = distance.cityblock(customer_A, customer_B)
cosine_sim = 1 - distance.cosine(customer_A, customer_B)
hamming_dist = distance.hamming(customer_A_binary, customer_B_binary)
jaccard_sim = jaccard_score(customer_A_binary, customer_B_binary)

print("Customer Preferences")
print("Euclidean Distance :", euclidean_dist)
print("Manhattan Distance :", manhattan_dist)
print("Cosine Similarity  :", cosine_sim)
print("Hamming Distance   :", hamming_dist)
print("Jaccard Similarity :", jaccard_sim)


# 2- Movie Ratings
user1 = np.array([5, 3, 4, 4, 2])
user2 = np.array([4, 2, 5, 4, 3])
chebyshev_dist = distance.chebyshev(user1, user2)
minkowski_dist = distance.minkowski(user1, user2, p=3)

print("\n Movie Ratings")
print("Chebyshev Distance :", chebyshev_dist)
print("Minkowski Distance (p=3):", minkowski_dist)
