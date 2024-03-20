import pandas as pd

# Load the 'Charades_v1_clean_train_100.csv' dataset
charades = pd.read_csv('F:/DEC_project/Charades_v1_clean_train_100.csv')

# Load the 'Charades_v1_mapping.txt' dataset
charades_mapping = pd.read_csv('F:/DEC_project/Charades_v1_mapping.txt', sep=' ', header=None, names=['code', 'objects', 'video'])

# Load the 'video_frame_mapping.csv' dataset
video_frame_mapping = pd.read_csv('F:/DEC_project/Videos/Videos_1/video_frame_mapping.csv')

# Update 'code' values in charades_mapping
charades_mapping['code'] = 'c' + charades_mapping['code'].str[1:].astype(int).astype(str)

# Remove 'c' from 'id' values in charades
charades['id'] = charades['id'].str[1:]

# Identify codes with no matching 'id' in charades
missing_codes = charades_mapping[~charades_mapping['code'].isin(charades['id'])]['code']
print("Codes with no matching 'id' in charades:")
print(missing_codes)

# Identify videos with no matching 'video_path' in video_frame_mapping
missing_videos = charades_mapping[~charades_mapping['video'].isin(video_frame_mapping['video_path'])]['video']
print("Videos with no matching 'video_path' in video_frame_mapping:")
print(missing_videos)

# Merge datasets using the updated mapping information
merged_df = pd.merge(charades_mapping, charades, left_on='code', right_on='id', how='left')

# Merge with video_frame_mapping
merged_df = pd.merge(merged_df, video_frame_mapping, left_on='video', right_on='video_path', how='left')

# Print rows with NaN values after the second merge
nan_rows_after_second_merge = merged_df[merged_df.isna().any(axis=1)]
print("Rows with NaN values after the second merge:")
print(nan_rows_after_second_merge)

# Create a master dataset
master_df = merged_df[['code', 'video', 'script', 'actions', 'length', 'category']]

# Save the master dataset as a CSV file
master_file_path = 'F:/DEC_project/master_dataset.csv'
master_df.to_csv(master_file_path, index=False)

print(f"Master dataset saved to: {master_file_path}")
