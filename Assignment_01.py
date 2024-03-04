import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = [2.3, 4.3, 3.3, 4.3, 4.4, 3.2, 2.0, 2.5, 2.0, 2.4,
        3.1, 3.2, 3.3, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 3.1,
        3.2, 2.5, 3.1, 3.0, 2.9, 3.5, 3.3, 3.2, 3.1, 4.0]

# (a) Construct the frequency distribution using 5 classes.
# Calculate class width
class_width = (max(data) - min(data)) / 5

# Creating a list of class intervals
classes = np.arange(min(data), max(data) + class_width, class_width)

# Counting the number of data points in each class interval
frequencies = np.histogram(data, bins=classes)[0]

# Combining class intervals and frequencies into a DataFrame
df = pd.DataFrame({'Class Interval': [f"{round(classes[i], 2)} - {round(classes[i+1], 2)}" for i in range(len(classes)-1)],
                   'Class Width': [round(class_width, 2) for _ in range(len(classes)-1)],
                   'Frequency': frequencies})

# Print the frequency table
print(df.to_string(index=False))

# (b) Construct histogram, frequency polygon, and Ogive graphs.
# Histogram
plt.hist(data, bins=classes, edgecolor='black')
plt.xlabel('Weight (kg)')
plt.ylabel('Frequency')
plt.title('Histogram of Radar Weights')
for i, interval in enumerate(classes[:-1]):
    plt.text(interval + class_width / 2, frequencies[i], f"{round(classes[i], 2)} - {round(classes[i+1], 2)}", ha='center', va='bottom')
plt.grid(True)
plt.show()

# Frequency Polygon
midpoints = classes[:-1] + class_width / 2
plt.plot(midpoints, frequencies, marker='o', linestyle='-', color='b')
plt.xlabel('Weight (kg)')
plt.ylabel('Frequency')
plt.title('Frequency Polygon of Radar Weights')
plt.xticks(midpoints)  # Add midpoints to x-axis
for i, interval in enumerate(classes[:-1]):
    plt.text(midpoints[i], frequencies[i], f"{round(classes[i], 2)} - {round(classes[i+1], 2)}", ha='center', va='bottom')
plt.grid(True)
plt.show()

# Ogive (Less Than)
cumulative_frequencies = np.cumsum(frequencies)
plt.plot(midpoints, cumulative_frequencies, marker='o', linestyle='-', color='g')
plt.xlabel('Weight (kg)')
plt.ylabel('Cumulative Frequency')
plt.title('Ogive (Less Than) of Radar Weights')
plt.xticks(midpoints)  # Add midpoints to x-axis
for i, interval in enumerate(classes[:-1]):
    plt.text(midpoints[i], cumulative_frequencies[i], f"{round(classes[i], 2)} - {round(classes[i+1], 2)}", ha='center', va='bottom')
plt.grid(True)
plt.show()
