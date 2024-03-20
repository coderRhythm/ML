import pandas as pd

# Load datasets
mapping_dataset = pd.read_csv('Charades_v1_mapping.txt', delimiter=' ')
class_description_dataset = pd.read_csv('class_description.csv')
objectCode_objects_dataset = pd.read_csv('objectCode_objects.csv')
videos_scene_dataset = pd.read_csv('videos_scene.csv')

# Merge datasets
merged_dataset = mapping_dataset.merge(class_description_dataset, how='left', left_on='c000', right_on='class_code')
merged_dataset = merged_dataset.merge(objectCode_objects_dataset, how='left', left_on='o009', right_on='object_code')
merged_dataset = merged_dataset.merge(videos_scene_dataset, how='left', left_on='v008', right_on='video_code')

# Drop unnecessary columns
merged_dataset = merged_dataset[['v008', 'description', 'objects', 'scenes']]

# Rename columns
merged_dataset.columns = ['video_code', 'class_description', 'object', 'scene']

# Save the modified merged dataset to a new CSV file
merged_dataset.to_csv('merged_dataset.csv', index=False)

print("Modified Merged Dataset saved to 'merged_dataset.csv'")