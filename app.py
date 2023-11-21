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

        audio_files = [
            "static/output_deep.wav",
            "static/output_high.wav",
            "static/output_ghost.wav",
            "static/output_robotic.wav",
            "static/output_echo.wav",
            "static/output_radio.wav",
            "static/output_vader.wav"
        ]

        return render_template("output.html", audio_files = audio_files)

