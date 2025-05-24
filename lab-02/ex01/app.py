from flask import Flask, render_template, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

# API xử lý Encrypt
@app.route("/api/encrypt", methods=["POST"])
def api_encrypt():
    data = request.get_json()
    text = data.get("text", "")
    key = int(data.get("key", 0))
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return jsonify({"result": encrypted_text})

# API xử lý Decrypt
@app.route("/api/decrypt", methods=["POST"])
def api_decrypt():
    data = request.get_json()
    text = data.get("text", "")
    key = int(data.get("key", 0))
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return jsonify({"result": decrypted_text})

if __name__ == "__main__":
    app.run(debug=True)
