from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Make 1,000 practice examples. 10% have wrong labels on purpose (noise).
X, y = make_classification(n_samples=1000, n_features=20,
                           n_informative=5, flip_y=0.3, random_state=42)

# Split: 80% for training, 20% locked away for testing.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Try models from very simple (depth 1) to unlimited (None).
for depth in [1, 3, 5, 10, None]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)               # learning happens here
    train_acc = model.score(X_train, y_train) # practice score
    test_acc = model.score(X_test, y_test)    # real exam score
    print(f"depth={depth}: train={train_acc:.2f}  test={test_acc:.2f}")