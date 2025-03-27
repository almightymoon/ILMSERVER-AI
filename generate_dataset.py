import csv
from tqdm import tqdm

# Configuration
OUTPUT_FILE = "quran_audio_dataset.csv"
RECITER = "Alafasy"
BASE_URL = "http://everyayah.com/data/Alafasy_64kbps/"
DEFAULT_SCORE = 95
DEFAULT_NOTES = "Good recitation"
DEFAULT_DURATION = 5.0  # Average duration in seconds

def generate_ayah_url(surah_num, ayah_num):
    """Generate EveryAyah.com URL for an ayah"""
    return f"{BASE_URL}{surah_num:03}{ayah_num:03}.mp3"

def get_ayah_count(surah_num):
    """Return number of ayahs for each surah"""
    # Source: https://en.wikipedia.org/wiki/List_of_surahs_in_the_Quran
    ayah_counts = [
        7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 
        128, 111, 110, 98, 135, 112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 
        34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53, 89, 59, 37, 35, 38, 
        29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 
        12, 12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 
        19, 36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 
        11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6
    ]
    return ayah_counts[surah_num - 1]

def generate_dataset():
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow([
            "surah_num", "ayah_num", "audio_url", "reciter", 
            "is_labeled", "is_correct", "score", "notes", "duration_sec"
        ])
        
        # Generate all ayahs
        for surah in tqdm(range(1, 115), desc="Generating Surahs"):
            ayah_count = get_ayah_count(surah)
            for ayah in range(1, ayah_count + 1):
                writer.writerow([
                    surah, ayah, generate_ayah_url(surah, ayah), RECITER,
                    "True", "True", DEFAULT_SCORE, DEFAULT_NOTES, DEFAULT_DURATION
                ])

if __name__ == "__main__":
    generate_dataset()
    print(f"Dataset generated at {OUTPUT_FILE}")