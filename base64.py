import base64


text = "example encryption"


text_bytes = text.encode('utf-8')
base64_bytes = base64.b64encode(teks_bytes)
base64_text = base64_bytes.decode('utf-8')

print(base64_teks)
