import json

# Define the phoneme-level vocabulary for all Arabic letters
phoneme_vocabulary = [
    {
        "letter": "ا",
        "phoneme": "/a/",
        "makhraj": "Open mouth",
        "tajweed_rules": [
            {
                "rule": "Madd",
                "description": "Elongation of the sound.",
                "phoneme": "/a:/"
            }
        ]
    },
    {
        "letter": "ب",
        "phoneme": "/b/",
        "makhraj": "Lips",
        "tajweed_rules": []
    },
    {
        "letter": "ت",
        "phoneme": "/t/",
        "makhraj": "Tip of the tongue touching the upper palate",
        "tajweed_rules": []
    },
    {
        "letter": "ث",
        "phoneme": "/θ/",
        "makhraj": "Tip of the tongue touching the upper teeth",
        "tajweed_rules": []
    },
    {
        "letter": "ج",
        "phoneme": "/dʒ/",
        "makhraj": "Middle of the tongue touching the hard palate",
        "tajweed_rules": []
    },
    {
        "letter": "ح",
        "phoneme": "/ħ/",
        "makhraj": "Middle of the throat",
        "tajweed_rules": []
    },
    {
        "letter": "خ",
        "phoneme": "/x/",
        "makhraj": "Deepest part of the throat",
        "tajweed_rules": []
    },
    {
        "letter": "د",
        "phoneme": "/d/",
        "makhraj": "Tip of the tongue touching the upper palate",
        "tajweed_rules": []
    },
    {
        "letter": "ذ",
        "phoneme": "/ð/",
        "makhraj": "Tip of the tongue touching the upper teeth",
        "tajweed_rules": []
    },
    {
        "letter": "ر",
        "phoneme": "/r/",
        "makhraj": "Tip of the tongue touching the alveolar ridge",
        "tajweed_rules": []
    },
    {
        "letter": "ز",
        "phoneme": "/z/",
        "makhraj": "Tip of the tongue touching the upper teeth",
        "tajweed_rules": []
    },
    {
        "letter": "س",
        "phoneme": "/s/",
        "makhraj": "Tip of the tongue touching the upper teeth",
        "tajweed_rules": []
    },
    {
        "letter": "ش",
        "phoneme": "/ʃ/",
        "makhraj": "Middle of the tongue touching the hard palate",
        "tajweed_rules": []
    },
    {
        "letter": "ص",
        "phoneme": "/sˤ/",
        "makhraj": "Tip of the tongue touching the upper teeth with emphasis",
        "tajweed_rules": []
    },
    {
        "letter": "ض",
        "phoneme": "/dˤ/",
        "makhraj": "Side of the tongue touching the upper molars",
        "tajweed_rules": []
    },
    {
        "letter": "ط",
        "phoneme": "/tˤ/",
        "makhraj": "Tip of the tongue touching the upper palate with emphasis",
        "tajweed_rules": []
    },
    {
        "letter": "ظ",
        "phoneme": "/ðˤ/",
        "makhraj": "Tip of the tongue touching the upper teeth with emphasis",
        "tajweed_rules": []
    },
    {
        "letter": "ع",
        "phoneme": "/ʕ/",
        "makhraj": "Middle of the throat",
        "tajweed_rules": []
    },
    {
        "letter": "غ",
        "phoneme": "/ɣ/",
        "makhraj": "Deepest part of the throat",
        "tajweed_rules": []
    },
    {
        "letter": "ف",
        "phoneme": "/f/",
        "makhraj": "Lower lip touching the upper teeth",
        "tajweed_rules": []
    },
    {
        "letter": "ق",
        "phoneme": "/q/",
        "makhraj": "Deepest part of the throat",
        "tajweed_rules": []
    },
    {
        "letter": "ك",
        "phoneme": "/k/",
        "makhraj": "Back of the tongue touching the soft palate",
        "tajweed_rules": []
    },
    {
        "letter": "ل",
        "phoneme": "/l/",
        "makhraj": "Tip of the tongue touching the alveolar ridge",
        "tajweed_rules": []
    },
    {
        "letter": "م",
        "phoneme": "/m/",
        "makhraj": "Lips",
        "tajweed_rules": [
            {
                "rule": "Ghunnah",
                "description": "Nasalization when م has shaddah.",
                "phoneme": "/m̃/"
            }
        ]
    },
    {
        "letter": "ن",
        "phoneme": "/n/",
        "makhraj": "Tip of the tongue touching the upper palate",
        "tajweed_rules": [
            {
                "rule": "Ghunnah",
                "description": "Nasalization when ن has shaddah.",
                "phoneme": "/ñ/"
            },
            {
                "rule": "Ikhfa",
                "description": "Hidden nasal sound when ن is followed by certain letters.",
                "phoneme": "/n̥/"
            }
        ]
    },
    {
        "letter": "ه",
        "phoneme": "/h/",
        "makhraj": "Middle of the throat",
        "tajweed_rules": []
    },
    {
        "letter": "و",
        "phoneme": "/w/",
        "makhraj": "Rounding the lips",
        "tajweed_rules": [
            {
                "rule": "Madd",
                "description": "Elongation of the sound.",
                "phoneme": "/u:/"
            }
        ]
    },
    {
        "letter": "ي",
        "phoneme": "/j/",
        "makhraj": "Middle of the tongue",
        "tajweed_rules": [
            {
                "rule": "Madd",
                "description": "Elongation of the sound.",
                "phoneme": "/i:/"
            }
        ]
    }
]

# Save the vocabulary to a JSON file
output_file = "phoneme_vocabulary.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(phoneme_vocabulary, f, ensure_ascii=False, indent=4)

print(f"Phoneme vocabulary saved to {output_file}")