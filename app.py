from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        
        inputAudio = request.form.get("inputAudio")
        filter = request.form.get("selectedFilter")

        # 1. sent the data to processs to main.py

        # 2. receive the data back from main.py

        # 3. display the data in output.html

        return render_template("output.html")

