import pandas as pd

# Load the training dataset
train_data = pd.read_csv('F:\DEC_project\Charades_v1_clean_train_100.csv')

# Display basic information about the dataset
print("Dataset Information:")
print(train_data.info())

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(train_data.head())

# Unique actions in the dataset
unique_actions = train_data['actions'].str.split(';', expand=True).stack().unique()
print("\nUnique Actions:")
print(unique_actions)

# Unique scenes in the dataset
unique_scenes = train_data['scene'].unique()
print("\nUnique Scenes:")
print(unique_scenes)

# Statistics about the dataset
print("\nStatistics about the dataset:")
print(train_data.describe())

# Distribution of video lengths
import matplotlib.pyplot as plt

plt.hist(train_data['length'], bins=30, edgecolor='black')
plt.title('Distribution of Video Lengths')
plt.xlabel('Video Length (seconds)')
plt.ylabel('Frequency')
plt.show()
