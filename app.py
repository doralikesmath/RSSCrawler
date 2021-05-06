"""
                                ╔═════════════════════════════════════════════╗
                                ║             .-') _                          ║
                                ║            (  OO) )                         ║
                                ║          ,(_)----. .---. .-----.            ║
                                ║          |       |/_   |/  -.   \           ║
                                ║          '--.   /  |   |'-' _'  |           ║
                                ║          (_/   /   |   |   |_  <            ║
                                ║           /   /___ |   |.-.  |  |           ║
                                ║          |        ||   |\ `-'   /           ║
                                ║          `--------'`---' `----''     ©2021  ║
                                ╚═════════════════════════════════════════════╝
"""
from flask import Flask
from flask import send_file, jsonify
app = Flask(__name__)


@app.route("/download")
def download():
    path = "corpus.txt"
    return send_file(path, as_attachment=True)


@app.route("/healthcheck")
def healthcheck():
    return jsonify("Ok")


@app.route("/")
def default():
    return jsonify("There is nothing here")


if __name__ == "__main__":
    app.run(port=5000,debug=True)