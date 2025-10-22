import csv
import json
import re
from pathlib import Path

DATA_DIR = Path('data')
OUTPUT_CSV = Path('data/yoruba_speech_registry.csv')

# Load Common Voice metadata
cv_path = DATA_DIR / 'cv23.json'
with cv_path.open() as f:
    cv_data = json.load(f)

yo = cv_data['locales']['yo']

# Extract release date from changelog
changelog_text = Path('CHANGELOG.md')
if changelog_text.exists():
    changelog = changelog_text.read_text(encoding='utf-8')
else:
    changelog = ''
release_date = ''
match = re.search(r"### \[Corpus 23.0\].*?- \*\*Date released\*\*: ([^\n]+)", changelog, re.S)
if match:
    release_date = match.group(1).strip()

cv_entry = {
    'dataset': 'Common Voice Yoruba',
    'source': 'Mozilla Common Voice',
    'release_or_listing': 'cv-corpus-23.0-2025-09-05',
    'release_date': release_date,
    'hours_total': yo.get('totalHrs'),
    'hours_valid': yo.get('validHrs'),
    'clip_count': yo.get('clips'),
    'license': 'Not listed in JSON (historically CC0 1.0)',
    'speaker_mix': 'Female {:.0%}, Male {:.0%}, Unspecified {:.0%}'.format(
        yo['splits']['gender'].get('female_feminine', 0.0),
        yo['splits']['gender'].get('male_masculine', 0.0),
        yo['splits']['gender'].get('', 0.0)
    ),
    'notes': 'Age data skewed toward twenties; sentence_domain metadata unused.',
    'source_link': 'https://raw.githubusercontent.com/common-voice/cv-dataset/main/datasets/cv-corpus-23.0-2025-09-05.json'
}

# Load OpenSLR SLR86 metadata
female_lines = (DATA_DIR / 'openslr86_line_index_female.tsv').read_text(encoding='utf-8').strip().splitlines()
male_lines = (DATA_DIR / 'openslr86_line_index_male.tsv').read_text(encoding='utf-8').strip().splitlines()
open_slr_entry = {
    'dataset': 'Google Yoruba Speech (SLR86)',
    'source': 'OpenSLR',
    'release_or_listing': 'SLR86',
    'release_date': '2020',
    'hours_total': '',
    'hours_valid': '',
    'clip_count': len(female_lines) + len(male_lines),
    'license': 'Creative Commons Attribution-ShareAlike 4.0 International',
    'speaker_mix': f"Female clips: {len(female_lines)}, Male clips: {len(male_lines)}",
    'notes': 'High-quality studio recordings; annotation_info.txt documents noise/disfluency tags.',
    'source_link': 'https://www.openslr.org/86/'
}

# Coqui index gap entry
coqui_entry = {
    'dataset': 'Coqui STT dataset index',
    'source': 'Coqui',
    'release_or_listing': 'dataset_links.md',
    'release_date': '',
    'hours_total': '',
    'hours_valid': '',
    'clip_count': '',
    'license': '',
    'speaker_mix': '',
    'notes': 'No Yoruba resources listed in the current index.',
    'source_link': 'https://github.com/coqui-ai/STT-data/blob/main/dataset_links.md'
}

rows = [cv_entry, open_slr_entry, coqui_entry]

fieldnames = ['dataset', 'source', 'release_or_listing', 'release_date', 'hours_total', 'hours_valid', 'clip_count', 'license', 'speaker_mix', 'notes', 'source_link']

with OUTPUT_CSV.open('w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print(f"Wrote {len(rows)} rows to {OUTPUT_CSV}")
