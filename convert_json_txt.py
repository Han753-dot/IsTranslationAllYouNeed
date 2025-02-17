import json

# Datei laden
input_file = 'data/GERestaurant_data/train_dataset.json'
output_file = 'data/GERestaurant_data/train_dataset.txt'

# JSON-Datei öffnen und laden
with open(input_file, 'r', encoding='utf-8') as infile:
    data = json.load(infile)

# Textdatei öffnen zum Schreiben
with open(output_file, 'w', encoding='utf-8') as outfile:
    for entry in data:
        sentence = entry['text']  # Extrahiere den Text
        tags = entry['tags']  # Extrahiere die Tags
        
        triplets = []
        for tag in tags:
            target = tag['text'] if tag['text'] != 'NULL' else 'None'
            aspect = tag['label']
            sentiment = tag['polarity'].lower()
            triplets.append(f"('{target}', '{aspect}', '{sentiment}')")
        
        triplet_string = f"[{', '.join(triplets)}]" if triplets else "[('None', 'GENERAL-IMPRESSION', 'neutral')]"
        
        outfile.write(f"{sentence}####{triplet_string}\n")

print(f"Die Umwandlung wurde abgeschlossen. Die Daten wurden in {output_file} gespeichert.")
