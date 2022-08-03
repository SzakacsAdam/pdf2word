from flask import Flask
from waitress import serve

app: Flask = Flask(__name__)


@app.route("/api/pdf", methods=["POST"])
def post_pdf():
    pass


@app.route("/api/pdf/<pdf_hash>", methods=["GET"])
def get_pdf(pdf_hash: str):
    print(f"\n\t{pdf_hash=}\n")


def main(host_ip: str, port: int, *, dev: bool = True):
    if dev:
        app.run(host=host_ip, port=port, debug=True)
    else:
        serve(app, host=host_ip, port=port)


if __name__ == '__main__':
    main()
