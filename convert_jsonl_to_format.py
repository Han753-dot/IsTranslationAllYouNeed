import uuid
import json

def convert_format(data):
    # Extracting the main sentence and triplets
    sentence = data["sentence"]
    triplets = data["triplets"]

    tags = []
    for triplet in triplets:
        target = triplet["target"]
        aspect = triplet["aspect"]
        sentiment = triplet["sentiment"]

        if target:  # Explicit tags
            start = sentence.find(target)
            end = start + len(target)
            tag_type = "label-explicit"
            text = target
        else:  # Implicit tags
            start = -1  # Placeholder for implicit
            end = -1  # Placeholder for implicit
            tag_type = "label-implicit"
            text = None

        tags.append({
            "start": start,
            "end": end,
            "tag_with_polarity": f"{aspect}-{sentiment.upper()}",
            "tag_with_polarity_and_type": f"{aspect}-{sentiment.upper()}-{tag_type.split('-')[1]}",
            "text": text,
            "type": tag_type,
            "label": aspect,
            "polarity": sentiment.upper()
        })

    # Assigning a unique ID
    result = {
        "tags": tags,
        "text": sentence,
        "id": str(uuid.uuid4())
    }
    return result

def process_jsonl_file(input_file, output_file):
    converted_data = []
    
    # Read the JSONL file line by line
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():  # Ignore empty lines
                data = json.loads(line)
                converted_data.append(convert_format(data))

    # Write the converted data to a JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(converted_data, f, ensure_ascii=False, indent=4)
# Usage
input_filename = "TASD_GOOGLE/jsonl/TASD_TEST15_GOOGLE_TRANSLATED.jsonl"  # Replace with your input file
output_filename = "TASD_GOOGLE/TASD_TEST15_GOOGLE_TRANSLATED_FORMATTED.json"  # Replace with your desired output file

input_filename_1 = "TASD_GOOGLE/jsonl/TASD_TRAIN15_GOOGLE_TRANSLATED.jsonl"  # Replace with your input file
output_filename_1 = "TASD_GOOGLE/TASD_TRAIN15_GOOGLE_TRANSLATED_FORMATTED.json" 

input_filename_2 = "TASD_GOOGLE/jsonl/TASD_TEST16_GOOGLE_TRANSLATED.jsonl"  # Replace with your input file
output_filename_2 = "TASD_GOOGLE/TASD_TEST16_GOOGLE_TRANSLATED_FORMATTED.json"  # Replace with your desired output file

input_filename_3 = "TASD_GOOGLE/jsonl/TASD_TRAIN16_GOOGLE_TRANSLATED.jsonl"  # Replace with your input file
output_filename_3 = "TASD_GOOGLE/TASD_TRAIN16_GOOGLE_TRANSLATED_FORMATTED.json" 

process_jsonl_file(input_filename_1, output_filename_1)
process_jsonl_file(input_filename_2, output_filename_2)
process_jsonl_file(input_filename_3, output_filename_3)
print(f"Converted data has been saved to {output_filename}.")