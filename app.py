from flask import Flask, render_template, request
from backend.main import process_audio

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":

        if 'inputAudio' not in request.files:
            return 'No file part'

        file = request.files['inputAudio']

        if file.filename == '':
            return 'No selected file'

        file.save('input.wav')

        process_audio()

        audio_names = [
            "Deep",
            "High",
            "Ghost",
            "Robotic",
            "Echo",
            "Radio",
            "Vader"
        ]

        # List of dynamically named audio files
        audio_names = [
            "Deep",
            "High",
            "Ghost",
            "Robotic",
            "Echo",
            "Radio",
            "Vader"
        ]

        # Generating audio file paths with dynamic names
        audio_files = [
            f"static/output_{name.lower()}.wav" for name in audio_names
        ]

        return render_template("output.html", audio_files=audio_files, audio_names=audio_names)

