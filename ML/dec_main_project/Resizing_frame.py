import cv2
import os
import pandas as pd

# Function to resize frames
def resize_frame(frame_path, output_path, target_size=(224, 224)):
    # Read the frame
    frame = cv2.imread(frame_path)
    
    # Resize the frame
    resized_frame = cv2.resize(frame, target_size)
    
    # Save the resized frame
    cv2.imwrite(output_path, resized_frame)

# Function to resize frames for a given folder and update CSV file
def resize_frames_and_update_csv(input_folder, output_folder, original_csv_path, target_size=(224, 224)):
    # Load the original CSV file
    original_df = pd.read_csv(original_csv_path)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through subfolders in the input folder
    for subfolder in os.listdir(input_folder):
        subfolder_path = os.path.join(input_folder, subfolder)
        
        # Create output subfolder for resized frames
        resized_output_folder = os.path.join(output_folder, subfolder)
        os.makedirs(resized_output_folder, exist_ok=True)

        # Iterate through frames in the subfolder and resize them
        for frame_file in os.listdir(subfolder_path):
            frame_path = os.path.join(subfolder_path, frame_file)
            resized_frame_path = os.path.join(resized_output_folder, frame_file)

            # Resize the frame
            resize_frame(frame_path, resized_frame_path, target_size=target_size)

        # Update the DataFrame with information about the resized frames
        resized_frames_info = []
        for index, row in original_df[original_df['category'] == subfolder].iterrows():
            frame_name = f"resized_{row['frame_path'].split('/')[-1]}"
            resized_frame_path = os.path.join(resized_output_folder, frame_name)
            resized_frames_info.append({'video_path': row['video_path'], 'frame_path': resized_frame_path, 'category': subfolder})

        # Create a DataFrame for the resized frames
        resized_df = pd.DataFrame(resized_frames_info)

        # Update the original DataFrame with the resized frame information
        original_df = pd.concat([original_df, resized_df], ignore_index=True)

    # Save the updated DataFrame to a new CSV file
    updated_csv_path = os.path.join(output_folder, "updated_video_frame_mapping.csv")
    original_df.to_csv(updated_csv_path, index=False)

    print("Resizing and CSV update completed.")

# Specify input and output folders for resized frames
egocentric_frames_folder = r"F:\DEC_project\Videos\Videos_1\Frames\Egocentric"
exocentric_frames_folder = r"F:\DEC_project\Videos\Videos_1\Frames\Exocentric"

resized_egocentric_folder = r"F:\DEC_project\Videos\Videos_1\Resized_Frames\Egocentric"
resized_exocentric_folder = r"F:\DEC_project\Videos\Videos_1\Resized_Frames\Exocentric"

# Specify the original CSV file
original_csv_path = r"F:\DEC_project\Videos\Videos_1\video_frame_mapping.csv"

# Resize frames in Egocentric folder and update CSV
resize_frames_and_update_csv(egocentric_frames_folder, resized_egocentric_folder, original_csv_path)

# Resize frames in Exocentric folder and update CSV
resize_frames_and_update_csv(exocentric_frames_folder, resized_exocentric_folder, original_csv_path)
