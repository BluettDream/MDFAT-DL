from flask import Flask
from controller import image_controller, text_controller

app = Flask(__name__)
app.register_blueprint(image_controller.img)
app.register_blueprint(text_controller.txt)


@app.route("/image/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000, threaded=True)
