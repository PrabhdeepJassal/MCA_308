#1.
# from sklearn.datasets import load_iris
# from sklearn.tree import DecisionTreeClassifier, plot_tree
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt

# iris = load_iris()
# X, y = iris.data, iris.target

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# model = DecisionTreeClassifier(criterion="gini", max_depth=4, random_state=42)
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)

# print(f"CART Decision Tree Accuracy: {accuracy * 100:.2f}%")


# plt.figure(figsize=(10,6))
# plot_tree(model, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
# print("Train accuracy:", model.score(X_train, y_train))
# print("Test accuracy:", model.score(X_test, y_test))

# plt.show()

#2.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

for col in iris.feature_names:
    df[col] = pd.cut(df[col], bins=3, labels=['low', 'medium', 'high'])

train, test = train_test_split(df, test_size=0.3, random_state=42)

def oneR(train_df, target_col):
    min_error = float('inf')
    best_rule = None
    best_col = None
    
    for col in train_df.columns:
        if col == target_col:
            continue
        rules = {}
        for val, subset in train_df.groupby(col):
            most_common_class = subset[target_col].mode()[0]
            rules[val] = most_common_class
        predictions = train_df[col].map(rules)
        error = sum(predictions != train_df[target_col])
        if error < min_error:
            min_error = error
            best_rule = rules
            best_col = col
    return best_col, best_rule

best_attr, best_rule = oneR(train, 'target')
print(f"Best Attribute: {best_attr}")
print(f"Rules: {best_rule}")

test_predictions = test[best_attr].map(best_rule)
accuracy = np.mean(test_predictions == test['target'])
print(f"OneR Accuracy: {accuracy * 100:.2f}%")

