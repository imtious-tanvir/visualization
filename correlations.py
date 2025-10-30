import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set up the figure
plt.figure(figsize=(14, 12))

# 1️⃣ Perfect Positive Correlation (r = +1)
x1 = np.arange(1, 11)
y1 = x1
plt.subplot(4, 2, 1)
plt.scatter(x1, y1, color='green')
plt.title("Perfect Positive Correlation (r = +1)")

# 2️⃣ High Positive Correlation (r ≈ +0.9)
x2 = np.arange(1, 11)
y2 = x2 * 2 + np.random.randint(-2, 2, 10)
plt.subplot(4, 2, 2)
plt.scatter(x2, y2, color='limegreen')
plt.title("High Positive Correlation (r ≈ +0.9)")

# 3️⃣ Low Positive Correlation (r ≈ +0.3)
x3 = np.arange(1, 11)
y3 = x3 + np.random.randint(-8, 8, 10)
plt.subplot(4, 2, 3)
plt.scatter(x3, y3, color='yellowgreen')
plt.title("Low Positive Correlation (r ≈ +0.3)")

# 4️⃣ No Correlation (r ≈ 0)
x4 = np.arange(1, 11)
y4 = np.random.randint(1, 20, 10)
plt.subplot(4, 2, 4)
plt.scatter(x4, y4, color='gray')
plt.title("No Correlation (r ≈ 0)")

# 5️⃣ Low Negative Correlation (r ≈ -0.3)
x5 = np.arange(1, 11)
y5 = -x5 + np.random.randint(-8, 8, 10)
plt.subplot(4, 2, 5)
plt.scatter(x5, y5, color='orange')
plt.title("Low Negative Correlation (r ≈ -0.3)")

# 6️⃣ High Negative Correlation (r ≈ -0.9)
x6 = np.arange(1, 11)
y6 = -2*x6 + np.random.randint(-2, 2, 10)
plt.subplot(4, 2, 6)
plt.scatter(x6, y6, color='red')
plt.title("High Negative Correlation (r ≈ -0.9)")

# 7️⃣ Perfect Negative Correlation (r = -1)
x7 = np.arange(1, 11)
y7 = -x7
plt.subplot(4, 2, 7)
plt.scatter(x7, y7, color='darkred')
plt.title("Perfect Negative Correlation (r = -1)")

plt.tight_layout()
plt.show()

# ✅ Calculate and display correlation values
datasets = {
    "Perfect Positive": (x1, y1),
    "High Positive": (x2, y2),
    "Low Positive": (x3, y3),
    "No Correlation": (x4, y4),
    "Low Negative": (x5, y5),
    "High Negative": (x6, y6),
    "Perfect Negative": (x7, y7),
}

print("📊 Correlation Values:\n")
for name, (x, y) in datasets.items():
    r = np.corrcoef(x, y)[0, 1]
    print(f"{name:20s}: r = {r:.2f}")
