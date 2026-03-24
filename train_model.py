import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

X = []
y = []

for _ in range(500):
    exp = np.random.randint(0, 10)
    skills = np.random.randint(0, 100)
    edu = np.random.randint(0, 3)
    projects = np.random.randint(0, 10)
    internship = np.random.randint(0, 2)
    communication = np.random.randint(1, 10)

    score = (skills * 0.4 +
             exp * 5 +
             projects * 3 +
             internship * 10 +
             communication * 2 +
             edu * 5)

    if score > 80:
        label = 2
    elif score > 50:
        label = 1
    else:
        label = 0

    X.append([exp, skills, edu, projects, internship, communication])
    y.append(label)

# ✅ Convert AFTER filling data
X = np.array(X)
y = np.array(y)

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model created successfully")