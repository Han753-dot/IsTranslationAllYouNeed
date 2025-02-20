from lxml import etree
import html
import jsonlines
import re  # Für reguläre Ausdrücke

def xml_to_jsonl(xml_file, output_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()

    sentences = root.findall("sentence")
    with jsonlines.open(output_file, mode='w') as writer:
        for sentence in sentences:
            # Extrahiere den reinen Text aus dem Satz ohne XML-Tags
            full_text = ''.join(sentence.itertext()).strip()

            # Bereinige den Text von unnötigen Leerzeichen und Zeilenumbrüchen
            full_text = re.sub(r'\s+', ' ', full_text)  # Ersetzt mehrere Leerzeichen und Zeilenumbrüche durch ein einzelnes Leerzeichen
            full_text = re.sub(r'^\s+|\s+?$', '', full_text)  # Entfernt führende und nachfolgende Leerzeichen

            # Hole alle <aspect-term>-Tags innerhalb der sentence
            aspects = sentence.findall(".//aspect-term")
            
            # Falls keine Aspekt-Tags vorhanden sind, überspringen wir den Satz
            if not aspects:
                continue

            # Triplets für die jeweiligen Aspekt-Tags extrahieren
            triplets = []
            for aspect in aspects:
                triplets.append({
                    "target": aspect.text,
                    "aspect": aspect.attrib["aspect"],
                    "sentiment": aspect.attrib["polarity"]
                })

            # Wenn Triplets vorhanden sind, den Satz speichern
            if full_text and triplets:
                writer.write({"sentence": full_text, "triplets": triplets})


# Ersetze hier mit den Pfaden zu deinen Dateien
xml_rest15_tasd_test_ollama_translated = "ollama_tasd_translations/tasd_rest15_test.xml"
xml_rest15_tasd_train_ollama_translated = "ollama_tasd_translations/tasd_rest15_train.xml"

xml_rest16_tasd_test_ollama_translated = "ollama_tasd_translations/tasd_rest16_test.xml"
xml_rest16_tasd_train_ollama_translated = "ollama_tasd_translations/tasd_rest16_train.xml"

output_rest15_test_tasd_ollama_translated = "TASD_OLLAMA_Formate/TASD_TEST15_OLLAMA.jsonl"
output_rest15_train_tasd_ollama_translated = "TASD_OLLAMA_Formate/TASD_TRAIN15_OLLAMA.jsonl"

output_rest16_test_tasd_ollama_translated = "TASD_OLLAMA_Formate/TASD_TEST16_OLLAMA.jsonl"
output_rest16_train_tasd_ollama_translated = "TASD_OLLAMA_Formate/TASD_TRAIN16_OLLAMA.jsonl"

xml_to_jsonl(xml_rest15_tasd_test_ollama_translated, output_rest15_test_tasd_ollama_translated)
xml_to_jsonl(xml_rest15_tasd_train_ollama_translated, output_rest15_train_tasd_ollama_translated)

xml_to_jsonl(xml_rest16_tasd_test_ollama_translated, output_rest16_test_tasd_ollama_translated)
xml_to_jsonl(xml_rest16_tasd_train_ollama_translated, output_rest16_train_tasd_ollama_translated)