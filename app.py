import streamlit as st
import os

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
            with open(os.path.join('/workspaces/video_main/video_files', new_name), 'wb') as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"Saved file as {new_name} to /workspaces/video_main/video_files")

            # To do: process the video file
            st.video(uploaded_file)

if __name__ == "__main__":
    main()