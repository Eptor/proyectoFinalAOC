from flask import Flask, jsonify, render_template, request
import subprocess
from string import punctuation, ascii_uppercase, ascii_lowercase, digits

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api", methods=["POST"])
def api():
    data = request.get_json()
    print(f"DATA: {data}")
    count = int(data["count"])
    final = []

    while len(final) < count:
        subprocess.run("static/prueba_randomizer2.exe", capture_output=True)
        with open("data.txt", "r") as rand:
            raw = rand.read()
            raw = raw.split(",")
            ints = [int(x.replace("\x00", "")) for x in raw[:-1]]
            chars = [chr(i) for i in ints]
        
        for i in chars:
            if i in punctuation and data["punctuation"]:
                final.append(i)
            elif i in digits and data["digits"]:
                final.append(i)
            elif i in ascii_lowercase and data["lowercase"]:
                final.append(i)
            elif i in ascii_uppercase and data["uppercase"]:
                final.append(i)
            else:
                break
                


    return jsonify(
        {
            "token": ''.join(final[:count])
        }
    )