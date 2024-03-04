import pandas as pd

# Data
data = {
    "TypeA": [3.1, 3.2, 3.6, 4.2, 4.5],
    "TypeB": [5.3, 6.5, 5.5, 4.2, 3.1],
    "TypeC": [3.2, 4.6, 5.3, 5.4, 5.2]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Function to calculate descriptive statistics
def get_statistics(data):
    mean = data.mean()
    median = data.median()
    mode = data.mode().iloc[0]  # Get the first mode if there are multiple
    variance = data.var()
    std_dev = data.std()
    coeff_var = (std_dev / mean) * 100  # Coefficient of variation in %
    skewness = data.skew()
    return pd.Series({
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Variance": variance,
        "Standard Deviation": std_dev,
        "Coefficient of Variation (%)": coeff_var,
        "Coefficient of Skewness": skewness
    })

# Calculate statistics for each type of radar
statistics = {}
for col in df.columns:
    statistics[col] = get_statistics(df[col])

# Print statistics as DataFrame
print(pd.DataFrame(statistics))

# Identify consistent radar type (assuming consistency means low standard deviation)
consistent_type = df.std().idxmin()
print(f"Consistent radar type (based on low standard deviation): {consistent_type}")

# Identify data distribution based on coefficient of skewness
distribution_info = {}
for col, stats in statistics.items():
    skewness = stats["Coefficient of Skewness"]
    distribution = "Normal" if abs(skewness) < 0.5 else "Skewed"
    distribution_info[col] = distribution

print(f"Data distribution for each type:")
for col, dist in distribution_info.items():
    print(f"- {col}: {dist}")
