import pandas as pd

# Load the dataset
dataset_path = r'F:\DEC_project\Videos\Videos_1\video_frame_mapping.csv'
df = pd.read_csv(dataset_path)

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(df.head())

# Display unique values in key columns
unique_video_paths = df['video_path'].unique()
unique_frame_paths = df['frame_path'].unique()
unique_categories = df['category'].unique()

print("\nUnique Video Paths:")
print(unique_video_paths)

print("\nUnique Frame Paths:")
print(unique_frame_paths)

print("\nUnique Categories:")
print(unique_categories)

# Display statistics about the dataset
print("\nStatistics about the dataset:")
print(df.describe())
