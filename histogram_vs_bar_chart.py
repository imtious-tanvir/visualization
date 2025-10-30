import matplotlib.pyplot as plt

# Data
data = [55, 60, 65, 70, 72, 75, 80, 85, 90, 95, 100]
categories = ['CSE', 'EEE', 'ME']
values = [30, 25, 15]

# Create horizontally arranged subplots (1 row, 2 columns)
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Histogram (left)
axs[0].hist(data, bins=5, color='skyblue', edgecolor='black')
axs[0].set_title("Histogram Example")
axs[0].set_xlabel("Score Range")
axs[0].set_ylabel("Frequency")

# Bar Chart (right)
axs[1].bar(categories, values, color='orange')
axs[1].set_title("Bar Chart Example")
axs[1].set_xlabel("Department")
axs[1].set_ylabel("Number of Students")

# Adjust spacing between plots
plt.tight_layout()

# Show both side by side
plt.show()
