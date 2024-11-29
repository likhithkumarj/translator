from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    dest_lang = data.get('dest_lang', 'en')

    try:
        translation = translator.translate(text, dest=dest_lang)
        response = {
            'translated_text': translation.text,
            'detected_language': translation.src
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
