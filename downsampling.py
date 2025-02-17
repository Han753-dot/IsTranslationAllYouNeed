import pandas as pd

# Funktion zum Laden der TXT-Dateien (kompletter Datensatz)
def load_txt_dataset(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "####" in line:
                text, label_str = line.strip().split("####")
                label_parts = label_str.strip("[]").split("), (")  # Aufteilen der Annotationen
                annotations = []
                for part in label_parts:
                    # Entfernen der Klammern und Umwandlung in Tuples
                    part = part.strip("()").split(", ")
                    # Hier prüfen wir, ob genau 3 Teile vorhanden sind, bevor wir sie extrahieren
                    if len(part) == 3:
                        target, label_category, sentiment = [x.strip("'") for x in part]
                        annotations.append((target, label_category, sentiment))
                    else:
                        # Falls die Annotation nicht die erwarteten 3 Werte enthält, geben wir sie als solches zurück
                        annotations.append(tuple(part))
                data.append((text, annotations))
    return pd.DataFrame(data, columns=["text", "annotations"])

# Funktion zum Speichern als TXT-Datei
def save_txt_dataset(data, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        for _, row in data.iterrows():
            # Umwandlung der Annotationen in ein Format, das für die Speicherung geeignet ist
            label_str = f"[{', '.join([str(x) for x in row['annotations']])}]"
            file.write(f"{row['text']}####{label_str}\n")

# Funktion zum Splitten des Datensatzes
def split_data(df, train_size=1120, test_size=582):
    # Zufälliges Sampling ohne Verlust von Annotationen
    train_data = df.sample(n=train_size, random_state=42)
    test_data = df.drop(train_data.index).sample(n=test_size, random_state=42)
    return train_data, test_data


# Beispiel-Datensatz laden
rest16_full_google = load_txt_dataset("TASD_GOOGLE_Formate/txt/TASD_REST16_FULL_GOOGLE_TRANSLATED.txt")
rest16_full_ollama = load_txt_dataset("TASD_OLLAMA_Formate/txt/TASD_REST16_FULL_OLLAMA_TRANSLATED.txt")   # Manuell zusammengeführt
gerestaurant_full = load_txt_dataset("data/GERestaurant_data/GERestaurant_FULL.txt")  # Manuell zusammengeführt

# Split in Trainings- und Testset (1120 für Training, 528 für Test)
rest16_train_google, rest16_test_google = split_data(rest16_full_google, train_size=1120, test_size=582)
rest16_train_ollama, rest16_test_ollama = split_data(rest16_full_ollama, train_size=1120, test_size=582)
gerestaurant_train, gerestaurant_test = split_data(gerestaurant_full, train_size=1120, test_size=582)
# Speichern der gesplitteten Datensätze
save_txt_dataset(rest16_train_google, "TASD_GOOGLE_Formate/txt/sampled/rest16_train_google_sampled.txt")
save_txt_dataset(rest16_test_google, "TASD_GOOGLE_Formate/txt/sampled/rest16_test_google_sampled.txt")
save_txt_dataset(rest16_train_ollama, "TASD_OLLAMA_Formate/txt/sampled/rest16_train_ollama_sampled.txt")
save_txt_dataset(rest16_test_ollama, "TASD_OLLAMA_Formate/txt/sampled/rest16_test_ollama_sampled.txt")
save_txt_dataset(gerestaurant_train, "data/GERestaurant_data/sampled/Gerestaurant_train_sampled.txt")
save_txt_dataset(gerestaurant_test, "data/GERestaurant_data/sampled/Gerestaurant_test_sampled.txt")
print("Datensätze wurden gesplittet und gespeichert: 1120 Trainingsbeispiele, 528 Testbeispiele.")


