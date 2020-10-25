from flask import Flask, send_file

app = Flask(__name__)


@app.route('/media/<path:path>')
def get_image(path):
    image_path = f'media/{path}'
    return send_file(image_path)
