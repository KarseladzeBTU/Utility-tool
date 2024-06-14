from flask import Flask, render_template, request, send_file
from utils.main_64 import utf8_to_base64, base64_to_utf8
from utils.main_URL import url_encode, url_decode
from utils.main_JSON import json_minify, json_beautify
from utils.main_URL_short import url_shorten
from io import BytesIO
import qrcode


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/base64', methods=['GET', 'POST'])
def base64():
    if request.method == 'POST':
        input_text = request.form['input_text']
        action = request.form['action']

        if action == 'Encode':
            encoded_text = utf8_to_base64(input_text)
            return render_template('base64.html', input_text=input_text, output_text=encoded_text, action=action)
        elif action == 'Decode':
            try:
                decoded_text = base64_to_utf8(input_text)
                return render_template('base64.html', input_text=input_text, output_text=decoded_text, action=action)
            except (UnicodeDecodeError, ValueError):
                error_message = "Unsupported format, please enter valid Base64 code."
                return render_template('base64.html', input_text=input_text, output_text=error_message, action=action)

    return render_template('base64.html')

@app.route('/url', methods=['GET', 'POST'])
def url():
    if request.method == 'POST':
        input_text = request.form['input_text']
        action = request.form['action']

        if action == 'Encode':
            encoded_text = url_encode(input_text)
            return render_template('url.html', input_text=input_text, output_text=encoded_text, action=action)
        elif action == 'Decode':
            decoded_text = url_decode(input_text)
            return render_template('url.html', input_text=input_text, output_text=decoded_text, action=action)

    return render_template('url.html')

@app.route('/json', methods=['GET', 'POST'])
def json():
    if request.method == 'POST':
        input_text = request.form['input_text']
        action = request.form['action']

        if action == 'Minify':
            minified_text = json_minify(input_text)
            return render_template('json.html', input_text=input_text, output_text=minified_text, action=action)
        elif action == 'Beautify':
            beautified_text = json_beautify(input_text)
            return render_template('json.html', input_text=input_text, output_text=beautified_text, action=action)

    return render_template('json.html')

@app.route('/qr', methods=['GET', 'POST'])
def qr_page():
    if request.method == 'POST':
        data = request.args.get('text')
        if not data:
            return {"message": 'Text is required'}, 400

        fill_color = request.args.get('fill', 'black')
        back_color = request.args.get('back_color', 'white')

        qr = qrcode.QRCode(
            version=None,
            box_size=10,
            border=2
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        img_io = BytesIO()
        img.save(img_io, 'JPEG', quality=70)
        img_io.seek(0)

        response = make_response(img_io.getvalue())
        response.headers['Content-Type'] = 'image/jpeg'

        return response
    return render_template('qr.html')

@app.route('/link_shortener', methods=['GET', 'POST'])
def link_shortener():
    if request.method == 'POST':
        inputed_url = request.form.get('input_url')
        shortened_url = url_shorten(inputed_url)
        return render_template('link_shortener.html', input_url=inputed_url, shortened_url=shortened_url)
    return render_template('link_shortener.html')


if __name__ == '__main__':
    app.run(debug=True)
