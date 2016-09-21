from StringIO import StringIO

from flask import Flask, render_template, request, send_file
from PIL import Image

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/get_image", methods=['GET', 'POST'])
def get_image():
    print request
    if request.method == 'POST':
        print request.files['picFile']
        pic_file = Image.open(request.files['picFile'])

        img_io = StringIO()
        pic_file.save(img_io, 'JPEG', quality=10, optimize=True)
        img_io.seek(0)

        return send_file(img_io, mimetype='image/jpeg')


if __name__ == "__main__":
    app.run()