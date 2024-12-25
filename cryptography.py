def encrypt_text(text, key):
    """
    Mengenkripsi teks menggunakan metode Caesar cipher yang dimodifikasi
    """
    encrypted = ""
    for char in text:
        if char.isalpha():
            # Menentukan ascii offset (65 untuk uppercase, 97 untuk lowercase)
            ascii_offset = 65 if char.isupper() else 97
            # Enkripsi karakter
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            encrypted += encrypted_char
        elif char.isdigit():
            # Enkripsi angka
            encrypted_char = str((int(char) + key) % 10)
            encrypted += encrypted_char
        else:
            # Karakter khusus tidak dienkripsi
            encrypted += char
    return encrypted

def decrypt_text(encrypted_text, key):
    """
    Mendekripsi teks yang telah dienkripsi
    """
    # Dekripsi menggunakan key negatif
    return encrypt_text(encrypted_text, -key) 