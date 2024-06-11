def url_encode(inputed_string):
    safe_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~"
    encoded_string1=""
    for char in inputed_string:
        if char in safe_chars:
            encoded_string1+=char
        elif char==" ":
            encoded_string1+="+"
        else:
            encoded_string1+=f'%{ord(char):02X}'
    return encoded_string1

def url_decode(encoded_string1):
    decoded_string1=""
    i=0
    while i<len(encoded_string1):
        if encoded_string1[i]=="%":
            hex_value=encoded_string1[i + 1:i + 3]
            decoded_string1+=chr(int(hex_value, 16))
            i+=3
        elif encoded_string1[i]=="+":
            decoded_string1+=" "
            i+=1
        else:
            decoded_string1+=encoded_string1[i]
            i+=1
    return decoded_string1
