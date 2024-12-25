import requests
import json

class ApiClient:
    def __init__(self, base_url='http://localhost:5001'):
        self.base_url = base_url

    def encrypt_text(self, text, key):
        """
        Mengirim permintaan ke API untuk enkripsi teks
        """
        try:
            response = requests.post(
                f'{self.base_url}/api/encrypt',
                json={'text': text, 'key': key},
                headers={'Content-Type': 'application/json'}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def decrypt_text(self, text, key):
        """
        Mengirim permintaan ke API untuk dekripsi teks
        """
        try:
            response = requests.post(
                f'{self.base_url}/api/decrypt',
                json={'text': text, 'key': key},
                headers={'Content-Type': 'application/json'}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def encode_image(self, image_file, message, key):
        """
        Mengirim permintaan ke API untuk enkripsi gambar
        """
        try:
            files = {'file': image_file}
            data = {'message': message, 'key': key}
            response = requests.post(
                f'{self.base_url}/api/encode',
                files=files,
                data=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}

    def decode_image(self, image_file, key):
        """
        Mengirim permintaan ke API untuk dekripsi gambar
        """
        try:
            files = {'file': image_file}
            data = {'key': key}
            response = requests.post(
                f'{self.base_url}/api/decode',
                files=files,
                data=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {'error': str(e)} 