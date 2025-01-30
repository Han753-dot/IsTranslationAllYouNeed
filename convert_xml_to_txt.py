import xml.etree.ElementTree as ET

def process_text(text):
    """Entferne unnötige Leerzeichen und Zeilenumbrüche."""
    return ' '.join(text.split())

def parse_aspect_terms(sentence):
    """Extrahiere die Aspect-Terms aus einem Satz."""
    aspects = []
    for aspect in sentence.findall('aspect-term'):
        term = aspect.text.strip() if aspect.text else "None"
        aspect_type = aspect.attrib.get('aspect', 'Unknown')
        polarity = aspect.attrib.get('polarity', 'neutral')
        aspects.append((term, aspect_type, polarity))
    return aspects

def convert_xml_to_txt(input_xml, output_txt):
    tree = ET.parse(input_xml)
    root = tree.getroot()
    
    with open(output_txt, 'w', encoding='utf-8') as f:
        for sentence in root.findall('sentence'):
            # Verarbeite den Satzinhalt
            raw_text = ''.join(sentence.itertext()).strip()
            clean_text = process_text(raw_text)
            
            # Extrahiere Aspect-Terms
            aspects = parse_aspect_terms(sentence)
            
            # Schreibe das Ergebnis
            aspect_str = str(aspects)
            f.write(f"{clean_text}####{aspect_str}\n")


# Input and output files
xml_rest15_tasd_test_google_translated = "preprocessing/TASD_TEST15_GOOGLE_TRANSLATED.xml"
xml_rest15_tasd_train_google_translated = "preprocessing/TASD_TRAIN15_GOOGLE_TRANSLATED.xml"

xml_rest16_tasd_test_google_translated = "preprocessing/TASD_TEST16_GOOGLE_TRANSLATED.xml"
xml_rest16_tasd_train_google_translated = "preprocessing/TASD_TRAIN16_GOOGLE_TRANSLATED.xml"

output_rest15_test_tasd_google_translated = "TASD_GOOGLE/txt/TASD_TEST15_GOOGLE_TRANSLATED.txt"
output_rest15_train_tasd_google_translated = "TASD_GOOGLE/txt/TASD_TRAIN15_GOOGLE_TRANSLATED.txt"

output_rest16_test_tasd_google_translated = "TASD_GOOGLE/txt/TASD_TEST16_GOOGLE_TRANSLATED.txt"
output_rest16_train_tasd_google_translated = "TASD_GOOGLE/txt/TASD_TRAIN16_GOOGLE_TRANSLATED.txt"

convert_xml_to_txt(xml_rest15_tasd_test_google_translated, output_rest15_test_tasd_google_translated)
convert_xml_to_txt(xml_rest15_tasd_train_google_translated, output_rest15_train_tasd_google_translated)

convert_xml_to_txt(xml_rest16_tasd_test_google_translated, output_rest16_test_tasd_google_translated)
convert_xml_to_txt(xml_rest16_tasd_train_google_translated, output_rest16_train_tasd_google_translated)
# Convert XML to TXT

print(f"Conversion complete. Output saved to.")
