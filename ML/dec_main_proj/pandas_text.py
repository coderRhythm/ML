import pandas as pd

mapping_dataset= pd.read_csv('Charades_v1_mapping.txt')

class_description_dataset = pd.read_csv('class_description.csv')

objectCode_objects_dataset = pd.read_csv('objectCode_objects.csv')

videos_scene_dataset = pd.read_csv('videos_scene.csv')

print("this is mapping dataset")
print(mapping_dataset.head())
print("this is class_code and description dataset")
print(class_description_dataset.head())
print("this is my object_code and object dataset")
print(objectCode_objects_dataset.head())
print("this is  my videos_scene dataset")
print(videos_scene_dataset.head())