from flask import Flask
from flask import jsonify
from waitress import serve

app: Flask = Flask(__name__)


@app.route("/pdf-converter/ping", methods=["GET"])
def ping():
    return jsonify({"Hi from PdfConverter API": "ping ok"}), 200


def main(host_ip: str, port: int, *, dev: bool = True):
    if dev:
        app.run(host=host_ip, port=port, debug=True)
    else:
        serve(app, host=host_ip, port=port)


if __name__ == '__main__':
    main("0.0.0.0", 8080)