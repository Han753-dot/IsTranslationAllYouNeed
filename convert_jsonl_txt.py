import json

# Datei laden
input_file = 'TASD_GOOGLE/json/TASD_TRAIN16_GOOGLE_TRANSLATED.jsonl'
output_file = 'TASD_GOOGLE/txt/TASD_TRAIN16_GOOGLE_TRANSLATED.txt'


# Öffnen der JSONL-Datei und der Textdatei zum Schreiben
with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
    for line in infile:
        data = json.loads(line.strip())
        sentence = data['sentence']  # Extrahiere den Satz
        triplets = data['triplets']  # Extrahiere die Triplets
        
        # Wenn es keine Triplets gibt, setze 'NULL' als target
        if not triplets:
            triplet_string = "[('NULL', 'food quality', 'positive')]"
        else:
            # Erstelle Triplet-String im gewünschten Format
            triplet_string = "[" + ', '.join([f"('{t['target']}', '{t['aspect']}', '{t['sentiment']}')" for t in triplets]) + "]"
        
        # Schreibe den Satz und die Triplets im gewünschten Format
        outfile.write(f"{sentence}####{triplet_string}\n")

print(f"Die Umwandlung wurde abgeschlossen. Die Daten wurden in {output_file} gespeichert.")
