from flask import Flask, jsonify, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api", methods=["POST"])
def api():
    data = request.get_json()
    count = int(data["count"])
    final = []
    rango = range(0, count+1)
    print(f"RANGO: {rango}")
    for index in range(0, count+10, 10):
        print(index)
        subprocess.run("static/prueba_randomizer2.exe", capture_output=True)
        with open("data.txt", "r") as rand:
            raw = rand.read()
            raw = raw.split(",")
            ints = [int(x.replace("\x00", "")) for x in raw[:-1]]
            chars = [chr(i) for i in ints]
        
        for i in chars:
            final.append(i)
        
    return jsonify(
        {
            "token": ''.join(final[:count])
        }
    )