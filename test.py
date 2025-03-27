import json

# Load the alphabet file
with open("alphabet.txt", "r", encoding="utf-8") as f:
    alphabet = [line.strip() for line in f if line.strip()]

# Load the vocabulary file
with open("vocabulary.txt", "r", encoding="utf-8") as f:
    vocabulary = [line.strip() for line in f if line.strip()]

# Define the phoneme-level vocabulary
phoneme_vocabulary = []

# Add all letters from the alphabet file
for letter in alphabet:
    phoneme_vocabulary.append({
        "letter": letter,
        "phoneme": "",  # Placeholder for phoneme
        "makhraj": "",  # Placeholder for makhraj
        "tajweed_rules": []  # Placeholder for tajweed rules
    })

# Add tajweed rules for specific letters
for entry in phoneme_vocabulary:
    letter = entry["letter"]
    if letter == "ن":
        entry["phoneme"] = "/n/"
        entry["makhraj"] = "Tip of the tongue touching the upper palate"
        entry["tajweed_rules"] = [
            {
                "rule": "Ghunnah",
                "description": "Nasalization when ن has shaddah.",
                "phoneme": "/ñ/"
            },
            {
                "rule": "Ikhfa",
                "description": "Hidden nasal sound when ن is followed by certain letters.",
                "phoneme": "/n̥/"
            },
            {
                "rule": "Idgham",
                "description": "Merging of ن with ي, و, م, or ن in specific cases.",
                "phoneme": "/nː/"
            },
            {
                "rule": "Iqlab",
                "description": "Transformation of ن into م when followed by ب.",
                "phoneme": "/m/"
            }
        ]
    elif letter == "م":
        entry["phoneme"] = "/m/"
        entry["makhraj"] = "Lips"
        entry["tajweed_rules"] = [
            {
                "rule": "Ghunnah",
                "description": "Nasalization when م has shaddah.",
                "phoneme": "/m̃/"
            },
            {
                "rule": "Idgham",
                "description": "Merging of م with ب in specific cases.",
                "phoneme": "/mː/"
            }
        ]
    elif letter == "و":
        entry["phoneme"] = "/w/"
        entry["makhraj"] = "Rounding the lips"
        entry["tajweed_rules"] = [
            {
                "rule": "Madd",
                "description": "Elongation of the sound.",
                "phoneme": "/u:/"
            },
            {
                "rule": "Idgham",
                "description": "Merging of و with و in specific cases.",
                "phoneme": "/wː/"
            }
        ]
    elif letter == "ي":
        entry["phoneme"] = "/j/"
        entry["makhraj"] = "Middle of the tongue"
        entry["tajweed_rules"] = [
            {
                "rule": "Madd",
                "description": "Elongation of the sound.",
                "phoneme": "/i:/"
            },
            {
                "rule": "Idgham",
                "description": "Merging of ي with ي in specific cases.",
                "phoneme": "/jː/"
            }
        ]
    elif letter == "ا":
        entry["phoneme"] = "/a/"
        entry["makhraj"] = "Open mouth"
        entry["tajweed_rules"] = [
            {
                "rule": "Madd",
                "description": "Elongation of the sound.",
                "phoneme": "/a:/"
            }
        ]
    # Add more letters and rules as needed

# Save the vocabulary to a JSON file
output_file = "phoneme_vocabulary.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(phoneme_vocabulary, f, ensure_ascii=False, indent=4)

print(f"Phoneme vocabulary saved to {output_file}")