BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def utf8_to_base64(utf8_text):
    utf8_bytes = utf8_text.encode('utf-8')
    binary_string = ''.join(f"{byte:08b}" for byte in utf8_bytes)
    padding = (6 - len(binary_string) % 6) % 6
    binary_string += '0' * padding
    six_bit_chunks = [binary_string[i:i+6] for i in range(0, len(binary_string), 6)]
    base64_string = ''.join(BASE64[int(chunk, 2)] for chunk in six_bit_chunks)
    base64_string += '=' * (padding // 2)

    return base64_string

def base64_to_utf8(base64_text):
    base64_text = base64_text.rstrip('=')
    binary_string = ''.join(f"{BASE64.index(char):06b}" for char in base64_text)
    padding = len(binary_string) % 8
    binary_string = binary_string[:len(binary_string) - padding]
    eight_bit_chunks = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    utf8_bytes = bytes(int(chunk, 2) for chunk in eight_bit_chunks)
    utf8_string = utf8_bytes.decode('utf-8')

    return utf8_string
