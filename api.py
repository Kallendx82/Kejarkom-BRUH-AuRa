from flask import Flask, jsonify, request
from imgstegno import encrypt_message, decrypt_message, encode_image, decode_image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Konfigurasi upload folder
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Buat folder jika belum ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return jsonify({
        'status': 'success',
        'message': 'API is running'
    })

# API untuk enkripsi teks (kriptografi)
@app.route('/api/encrypt', methods=['POST'])
def api_encrypt_text():
    try:
        data = request.get_json()
        text = data.get('text', '')
        key = int(data.get('key', 0))
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
            
        encrypted_text = encrypt_message(text, key)
        return jsonify({
            'status': 'success',
            'encrypted_text': encrypted_text,
            'key': key
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API untuk dekripsi teks (kriptografi)
@app.route('/api/decrypt', methods=['POST'])
def api_decrypt_text():
    try:
        data = request.get_json()
        text = data.get('text', '')
        key = int(data.get('key', 0))
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
            
        decrypted_text = decrypt_message(text, key)
        return jsonify({
            'status': 'success',
            'decrypted_text': decrypted_text,
            'key': key
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API untuk enkripsi gambar (steganografi)
@app.route('/api/encode', methods=['POST'])
def api_encode_image():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        message = request.form.get('message', '')
        key = int(request.form.get('key', 0))
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)
            
            # Enkripsi pesan
            encrypted_message = encrypt_message(message, key)
            
            # Encode ke dalam gambar
            output_filename = f'encoded_{filename.rsplit(".", 1)[0]}.png'
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
            
            result = encode_image(input_path, encrypted_message, output_path)
            
            # Hapus file input setelah selesai
            if os.path.exists(input_path):
                os.remove(input_path)
                
            return jsonify({
                'status': 'success',
                'message': 'Image encoded successfully',
                'output_file': output_filename
            })
            
        return jsonify({'error': 'File type not allowed'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API untuk dekripsi gambar (steganografi)
@app.route('/api/decode', methods=['POST'])
def api_decode_image():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
            
        file = request.files['file']
        key = int(request.form.get('key', 0))
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)
            
            # Decode pesan dari gambar
            encoded_message = decode_image(input_path)
            
            if encoded_message == "Tidak ada pesan tersembunyi atau format tidak sesuai":
                return jsonify({'error': encoded_message}), 400
                
            # Dekripsi pesan
            decrypted_message = decrypt_message(encoded_message, key)
            
            # Hapus file setelah selesai
            if os.path.exists(input_path):
                os.remove(input_path)
                
            return jsonify({
                'status': 'success',
                'cipher_text': encoded_message,
                'plain_text': decrypted_message
            })
            
        return jsonify({'error': 'File type not allowed'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001) 