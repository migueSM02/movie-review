from flask import Flask, render_template, request, jsonify
import numpy as np
import json
import joblib
from googletrans import Translator

app = Flask(__name__)
translator = Translator()


#cargar el diccionario y el modelo entrenado
with open('data/imbd_dic.json', 'r') as f:
    word_index = json.load(f)

trained_model = joblib.load('data/trained_model.pkl')


@app.route('/static/<path:path>')
def static_file(path):
    return app.send_static_file(path)


def vectorize_sequences_with_dtype(sequences, dimension=10000, dtype=np.float32):
    results = np.zeros((len(sequences), dimension), dtype=dtype)
    for i, sequence in enumerate(sequences):
        valid_indices = [index for index in sequence if index < dimension]
        results[i, valid_indices] = 1.
    return results


def encode_review(text, word_index, max_words=10000):
    tokens = text.split()
    sequence = [word_index.get(word, 0) for word in tokens if word_index.get(word, 0) < max_words]
    return sequence


# Ruta principal para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')


# Ruta para la predicción basada en la entrada del usuario
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        feature = request.json['feature']

        review_text = str(feature).lower()
        idioma = translator.translate(review_text)

        if idioma != 'en':
            texto_traducido = translator.translate(review_text, dest='en').text
            encoded_review = encode_review(texto_traducido, word_index)
        else:
            encoded_review = encode_review(review_text, word_index)

        vectorized_review = vectorize_sequences_with_dtype([encoded_review])
        predicted_label = trained_model.predict(vectorized_review)[0]

        if int(predicted_label) == 0:
            predicted_text = "Negative"
        else:
            predicted_text = "Positive"
        return jsonify({'prediction': predicted_text})


if __name__ == '__main__':
    app.run(debug=True)
