import flask
from flask import Flask, render_template, send_from_directory, request
from pyngrok import ngrok,conf
import os
import sys
import time
import argparse

parser = argparse.ArgumentParser(description="Classification d'images")
parser.add_argument('path', help='chemin du dossier')
parser.add_argument('port', type=int, help='Port')
args = parser.parse_args()

app = Flask(__name__)


@app.route("/getImage/<filename>/<loop_index>")
def get_img(filename, loop_index):
    if loop_index > "4":
        time.sleep(2)
    return send_from_directory(app.config["path"], filename)


@app.route("/", methods=["GET", "POST"])
def home():
    response = flask.Response()
    response.headers["ngrok-skip-browser-warning"]="*"
    if request.method == "POST":
        req = request.form
        app.config["path"] = req["path"]

    images = os.listdir(app.config["path"])

    return render_template("index.html", images=images, path=app.config["path"])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        app.config["path"] = sys.argv[1]

        conf.get_default().auth_token="2CJIoUhtLd70hR9O6HbGmsUKMuS_4yyRyTRX3hKGsCeA2gQ8c"
        url = ngrok.connect(sys.argv[2]).public_url
        print(url)
        app.run( port=sys.argv[2])

    else:
        print("veuillez entrer un chemin pour les images")
