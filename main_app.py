from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def home():
    frames_dir = '/workspaces/video_main/video_frames'
    frames = os.listdir(frames_dir)
    # Sort the frames by their last modified time
    frames.sort(key=lambda frame: os.path.getmtime(os.path.join(frames_dir, frame)))
    return '<br>'.join([f'<div style="width: 200px;"><img src="/frame/{frame}" style="width: 100%;"><p>{frame}</p></div>' for frame in frames])

@app.route('/frame/<frame>')
def serve_frame(frame):
    return send_from_directory('/workspaces/video_main/video_frames', frame)

if __name__ == "__main__":
    app.run(debug=True)