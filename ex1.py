alphabet = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_"
alphabet_len = len(alphabet)

def encrypt_text(text, key):
    """Текстті шифрлау функциясы."""
    encrypted_text = ""
    key_len = len(key)

    for i, char in enumerate(text):
        text_index = alphabet.find(char)
        key_index = alphabet.find(key[i % key_len])
        
        new_index = (text_index + key_index) % alphabet_len
        encrypted_text += alphabet[new_index]
    
    return encrypted_text

def decrypt_text(encrypted_text, key):
    """Текстті дешифрлау функциясы."""
    decrypted_text = ""
    key_len = len(key)

    for i, char in enumerate(encrypted_text):
        text_index = alphabet.find(char)
        key_index = alphabet.find(key[i % key_len])
       
        new_index = (text_index - key_index) % alphabet_len
        decrypted_text += alphabet[new_index]
    
    return decrypted_text

text = input("Шифрланатын немесе дешифрланатын мәтінді енгізіңіз: ").upper()
key = input("Кілтті енгізіңіз: ").upper()

encrypted = encrypt_text(text, key)
decrypted = decrypt_text(encrypted, key)

print("Шифрланған текст:", encrypted)
print("Дешифрланған текст:", decrypted)
