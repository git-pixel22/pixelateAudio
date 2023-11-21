from flask import Flask, render_template, request
from main import process_audio

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

        isDone = process_audio()

        list = []

        if isDone:
            list.append("output_deep.wav")
            list.append("output_high.wav")
            list.append("output_ghost.wav")
            list.append("output_robotic.wav")
            list.append("output_echo.wav")
            list.append("output_radio.wav")
            list.append("output_vader.wav")

        return render_template("output.html", audio_files = list)

