import json
import base64

# El mensaje codificado
encoded_message = "eyJlbW9qaSI6MCwibGF5b3V0TmFtZSI6Ikd1ZXJyYSBJbmZpbml0YSAiLCJjb21iYXQiOjEwMzg0MDAsInRyb29wTGF5b3V0Ijp7IjEiOjE4NjEwLCIzNiI6MTg5MDgsIjQ2IjoxODkwOSwiMjIiOjE4OTA4LCI2MiI6MTg5MDksIjQyIjoxODkwOCwiNTIiOjE4OTA5LCIyNSI6MTg5MDgsIjI2IjoxODkwOCwiMzUiOjE4OTA4LCIyMCI6MTg5MDgsIjMzIjoxODkwOCwiMCI6MTg4MDksIjU0IjoxODkwOCwiNTYiOjE4OTA4LCIyNCI6MTg5MDgsIjYzIjoxODkwOSwiNjAiOjE4OTA5LCI0NCI6MTg5MDgsIjQxIjoxODkwOSwiMzIiOjE4OTA4LCI1NSI6MTg5MDksIjQzIjoxODkwOCwiNTMiOjE4OTA5LCI0NSI6MTg5MDgsIjIiOjE0NjA5LCI2NCI6MTg5MDksIjMiOjE4NjEwLCIxMCI6MTU5MTAsIjEyIjoxNjgxMCwiMjMiOjE4OTA4LCIzNCI6MTg5MDgsIjYxIjoxODkwOSwiNCI6MTQ2MDksIjUiOjE4NjA5LCI2IjoxODgwOSwiNTEiOjE4OTA5LCIxNSI6MTg5MDgsIjMwIjoxODkwOCwiMzEiOjE4OTA4LCI0MCI6MTg5MDksIjIxIjoxODkwOCwiNTAiOjE4OTA4LCI2NiI6MTg5MDksIjY1IjoxODkwOSwiMTMiOjExMTEwLCIxMSI6MTg5MDgsIjE2IjoxNTkxMCwiMTQiOjE2ODEwfSwiaGVyb0xheW91dCI6eyIwIjoxMjcxOX0sIndlYlVybCI6bnVsbCwidXNlcklkIjowLCJuYW1lIjpudWxsfQ=="

# Decodificar el mensaje
decoded_message = json.loads(base64.b64decode(encoded_message.encode('utf-8')).decode('utf-8'))

# Extraer la sección "trooLayer"
troopLayout_data = decoded_message.get("troopLayout", {})
heroLayout_data = decoded_message.get("heroLayout", {})

# Ordenar las claves de "trooLayer" en orden ascendente
sorted_trooLayer = {str(key): value for key, value in sorted(troopLayout_data.items(), key=lambda x: int(x[0]))}

# Imprimir el resultado
print(json.dumps({"troopLayout": sorted_trooLayer, "heroLayout":heroLayout_data}, indent=2))

# Codifica la estructura de datos en formato JSON
json_data = json.dumps({"troopLayout": sorted_trooLayer, "heroLayout":heroLayout_data}, indent=2)

# Convierte la cadena JSON en bytes
json_bytes = json_data.encode('utf-8')

# Codifica los bytes en base64
base64_encoded = base64.b64encode(json_bytes).decode('utf-8')

print(base64_encoded)