import pandas as pd
import numpy as np

charades = pd.read_csv('F:/DEC_project/Charades_v1_clean_train_100.csv')


frames_dataset = pd.read_csv('F:/DEC_project/Videos/Videos_1/video_frame_mapping.csv')



print('charades_dataet columns: ')
print(charades.columns)


print('frames_dataset columns: ')
print(frames_dataset.columns)