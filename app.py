import streamlit as st
import os
import requests
from moviepy.editor import VideoFileClip

def main():
    st.title('Upload Video Files')

    uploaded_file = st.file_uploader("Choose a video file", type=['mp4', 'mov', 'avi'])

    if uploaded_file is not None:
        # Get the new name from the user
        new_name = st.text_input("Enter the new name for the video file")

        if new_name:
            # Add the original file extension to the new name
            _, extension = os.path.splitext(uploaded_file.name)
            new_name += extension

            # Save the file with the new name to a specific location
            file_path = os.path.join('/workspaces/video_main/video_files', new_name)
            with open(file_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"Saved file as {new_name} to /workspaces/video_main/video_files")

            # Resize the video to 720p
            clip = VideoFileClip(file_path)
            clip_resized = clip.resize(height=720)  # Set the height as 720p
            clip_resized.write_videofile(file_path)

            # Display the video file
            st.video(file_path)

            # Trigger video processing on backend
            response = requests.post("http://localhost:3000/process-video", json={"videoPath": file_path})

            if response.status_code == 200:
                st.success("Video processing initiated successfully!")
            else:
                st.error("Failed to trigger video processing.")

if __name__ == "__main__":
    main()