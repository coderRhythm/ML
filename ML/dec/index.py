import cv2
import pandas as pd
import os

# Function to convert video to frames
def convert_video_to_frames(video_path, output_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Get the frames per second (fps) and frame count
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # List to store frame paths
    frame_paths = []

    # Loop through each frame and save it as an image
    for frame_number in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break
        frame_name = f"{output_path}/frame_{frame_number:04d}.jpg"
        cv2.imwrite(frame_name, frame)
        frame_paths.append(frame_name)

    # Release the video capture object
    cap.release()

    return frame_paths

# Function to process videos in a specific folder
def process_videos(input_folder, output_folder, category):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List to store DataFrames
    dfs = []

    # Loop through each video in the input folder
    for video_file in os.listdir(input_folder):
        video_path = os.path.join(input_folder, video_file)
        output_subfolder = os.path.join(output_folder, video_file.split('.')[0])

        # Convert video to frames
        frame_paths = convert_video_to_frames(video_path, output_subfolder)

        # Create DataFrame for the current video
        video_df = pd.DataFrame({'video_path': [video_path]*len(frame_paths), 'frame_path': frame_paths, 'category': [category]*len(frame_paths)})

        # Append the DataFrame to the list
        dfs.append(video_df)

    # Concatenate the list of DataFrames
    result_df = pd.concat(dfs, ignore_index=True)

    return result_df

# Specify input and output folders for egocentric and exocentric videos
egocentric_folder = r"F:\DEC_project\Videos\Videos_1\Egocentric"
exocentric_folder = r"F:\DEC_project\Videos\Videos_1\Exocentric"

egocentric_output_folder = r"F:\DEC_project\Videos\Videos_1\Frames\Egocentric"
exocentric_output_folder = r"F:\DEC_project\Videos\Videos_1\Frames\Exocentric"

# Process egocentric videos
egocentric_df = process_videos(egocentric_folder, egocentric_output_folder, 'egocentric')

# Process exocentric videos
exocentric_df = process_videos(exocentric_folder, exocentric_output_folder, 'exocentric')

# Concatenate the DataFrames
result_df = pd.concat([egocentric_df, exocentric_df], ignore_index=True)

# Save the result DataFrame to a CSV file
result_csv_path = r"F:\DEC_project\Videos\Videos_1\video_frame_mapping.csv"
result_df.to_csv(result_csv_path, index=False)

print("Conversion and CSV creation completed.")
