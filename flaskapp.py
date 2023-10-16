import time
import os
from flask import Flask, Response

app = Flask(__name__)
frame_directory = "frames"  # Change this to the directory where your frame files are located

def generate_frames():
    frame_files = sorted(os.listdir(frame_directory))
    while True:
        for frame_file in frame_files:
            with open(os.path.join(frame_directory, frame_file), "r") as f:
                frame = f.read()
                yield "\033[2J\033[H"  # ANSI escape code to clear the screen
                yield frame
            time.sleep(0.1)  # Adjust the delay as needed for your desired speed

@app.route('/animation')
def animation():
    return Response(generate_frames(), content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
