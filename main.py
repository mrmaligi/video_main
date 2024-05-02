#provides a quick example of how to prompt Gemini 1.5 Pro using a video file. In this case, you'll use a short clip of Sherlock Jr.
#from google.cloud import vision
#import google.generativeai as genai
#Authentication Overview
#Important: The File API uses API keys for authentication and access. Uploaded files are associated with the API key's cloud project. Unlike other Gemini APIs that use API keys, your API key also grants access data you've uploaded to the File API, so take extra care in keeping your API key secure. For best practices on securing API keys, refer to Google's documentation.
#Setup your API key
#To run the following cell, your API key must be stored it in a Colab Secret named GOOGLE_API_KEY. If you don't already have an API key, or you're not sure how to create a Colab Secret, see Authentication for an example.

import os

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Make sure to replace 'genai' with the correct module name
# import genai
# genai.configure(api_key=GOOGLE_API_KEY)
#from google.colab import userdata
#GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
#genai.configure(api_key=GOOGLE_API_KEY)

#Extract frames
#The Gemini API currently does not support video files directly. Instead, you can provide a series of timestamps and image files.
#We will extract 1 frame a second from a 10 minute clip of the film Sherlock Jr..
#Note: You can also upload your own files to use.

video_file_name = "/workspaces/video_main/video_files/PXL_20230824_025354799[1].mp4"
#Use OpenCV to extract image frames from the video at 1 frame per second.

import cv2
import os
import shutil

# Create or cleanup existing extracted image frames directory.
FRAME_EXTRACTION_DIRECTORY = "/workspaces/video_main/video_frames"
FRAME_PREFIX = "_frame"
def create_frame_output_dir(output_dir):
  if not os.path.exists(output_dir):
    os.makedirs(output_dir)
  else:
    shutil.rmtree(output_dir)
    os.makedirs(output_dir)

def extract_frame_from_video(video_file_path):
  print(f"Extracting {video_file_path} at 1 frame per second. This might take a bit...")
  create_frame_output_dir(FRAME_EXTRACTION_DIRECTORY)
  vidcap = cv2.VideoCapture(video_file_path)
  fps = vidcap.get(cv2.CAP_PROP_FPS)
  frame_duration = 1 / fps  # Time interval between frames (in seconds)
  output_file_prefix = os.path.basename(video_file_path).replace('.', '_')
  frame_count = 0
  count = 0
  while vidcap.isOpened():
      success, frame = vidcap.read()
      if not success: # End of video
          break
      if int(count / fps) == frame_count: # Extract a frame every second
          min = frame_count // 60
          sec = frame_count % 60
          time_string = f"{min:02d}:{sec:02d}"
          image_name = f"{output_file_prefix}{FRAME_PREFIX}{time_string}.jpg"
          output_filename = os.path.join(FRAME_EXTRACTION_DIRECTORY, image_name)
          cv2.imwrite(output_filename, frame)
          frame_count += 1
      count += 1
  vidcap.release() # Release the capture object\n",
  print(f"Completed video frame extraction!\n\nExtracted: {frame_count} frames")

extract_frame_from_video(video_file_name)