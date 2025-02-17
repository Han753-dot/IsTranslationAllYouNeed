import json
import uuid

def convert_txt_to_json(input_file, output_file):
    data = []
    
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            # Wenn die Zeile das Separator-Tag "####" enthält, teilen wir die Text- und Annotationsteile
            if "####" in line:
                text, label_str = line.strip().split("####")
                
                # Extrahiere die Annotationen (Tag, Polarity, Label)
                label_parts = label_str.strip("[]").split("), (")
                tags = []
                
                # Verarbeite jede Annotation
                for part in label_parts:
                    part = part.strip("()").split(", ")
                    if len(part) == 3:
                        target, label_category, sentiment = [x.strip("'") for x in part]
                        
                        # Setze die Polarity
                        polarity = sentiment.upper()
                        
                        # Erstelle den Tag mit Polarity
                        tag_with_polarity = f"{label_category}-{polarity}"
                        tag_with_polarity_and_type = f"{label_category}-{polarity}-no-phrase-implicit"
                        
                        # Erstelle den Tag-Eintrag
                        tag_entry = {
                            "end": len(text),  # Ende des Texts, hier als Platzhalter, kann später angepasst werden
                            "start": 0,  # Start des Texts, hier als Platzhalter
                            "tag_with_polarity": tag_with_polarity,
                            "tag_with_polarity_and_type": tag_with_polarity_and_type,
                            "text": "NULL",  # Text wird hier später als NULL gespeichert
                            "type": "label-implicit",
                            "label": label_category,
                            "polarity": polarity
                        }
                        tags.append(tag_entry)
                
                # Erstelle ein Entry für das JSON
                entry = {
                    "tags": tags,
                    "text": text,
                    "id": str(uuid.uuid4())  # Generiere eine eindeutige ID
                }
                
                data.append(entry)
    
    # Speichern der konvertierten Daten als JSON-Datei
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    
    print(f"Konvertierung abgeschlossen. Die Datei wurde als {output_file} gespeichert.")

# Beispielaufruf des Skripts
convert_txt_to_json("data/GERestaurant_data/sampled/Gerestaurant_test_sampled.txt", "data/GERestaurant_data/sampled/Gerestaurant_test_sampled.json")
convert_txt_to_json("data/GERestaurant_data/sampled/Gerestaurant_train_sampled.txt", "data/GERestaurant_data/sampled/Gerestaurant_train_sampled.json")
