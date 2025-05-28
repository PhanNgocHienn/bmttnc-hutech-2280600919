from flask import Flask, request, jsonify, render_template
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/transposition")
def transposition():
    return render_template('transposition.html')


# CAESAR
@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form['InputPlainText']
    key = int(request.form['InputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt(text, key)
    return f"text:{text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form['InputCipherText']
    key = int(request.form['InputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# VIGENERE
@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form['plain_text']
    key = request.form['key']
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    return f"text:{text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form['cipher_text']
    key = request.form['key']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# RAILFENCE
@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form['plain_text']
    key = int(request.form['key'])
    railfence = RailFenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    return f"text:{text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form['cipher_text']
    key = int(request.form['key'])
    railfence = RailFenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# PLAYFAIR
@app.route("/playfair/creatematrix", methods=["POST"])
def playfair_create_matrix():
    key = request.form['key']
    playfair = PlayFairCipher()
    matrix = playfair.playfair_creatematrix(key)
    return f"Matrix for key '{key}':<br/>{matrix}"

# TRANSPOSITION
@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form['plain_text']
    key = int(request.form['key'])
    transposition = TranspositionCipher()
    encrypted_text = transposition.encrypt(text, key)
    return f"text:{text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form['cipher_text']
    key = int(request.form['key'])
    transposition = TranspositionCipher()
    decrypted_text = transposition.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)