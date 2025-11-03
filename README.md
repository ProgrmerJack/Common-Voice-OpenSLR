# Common-Voice-OpenSLR

A curated registry and data note for Yoruba (yo) speech resources aggregated from Mozilla Common Voice, OpenSLR, and the Coqui STT dataset index. This repository collects metadata snapshots, produces a consolidated registry, and generates a short data note that documents methods, coverage, licensing, and remaining gaps for Yoruba speech resources.

## Purpose
- Consolidate and standardize metadata about Yoruba speech datasets from multiple public indexes and archives.
- Make it easy for researchers, dataset maintainers, and funders to understand current coverage, licensing constraints, and where to focus data collection or curation efforts.
- Provide reproducible scripts to rebuild the registry and regenerate the data note so future updates can be tracked.

## What this repository contains
- data/:
  - Source metadata snapshots (e.g., Common Voice Corpus JSON, OpenSLR catalogue extracts, Coqui index JSON) used as input for reproducibility.
  - Outputs such as `yoruba_speech_registry.csv`.
- scripts/:
  - `build_registry.py` — script that reads source snapshots, normalizes fields, computes coverage metrics, and writes `data/yoruba_speech_registry.csv`.
  - `note_to_pdf.py` — script that renders the data note (PDF) from a markdown/LaTeX template and the registry.
- reports/:
  - `yoruba_registry_note.pdf` — an analytic 4-page data note summarizing methodology, gaps, and recommendations.
- docs/:
  - `zenodo_metadata.json` — draft metadata suitable for publishing the registry and data note on Zenodo (adapt before publishing).
- README.md:
  - This file — a user-facing description and reproducibility instructions.

## Key outputs
- data/yoruba_speech_registry.csv
  - A consolidated table summarizing releases for each source dataset with columns such as:
    - source (e.g., Mozilla Common Voice)
    - identifier or dataset id
    - version/release (e.g., 23.0)
    - release_date
    - language_code
    - samples (utterances)
    - hours (approx. total audio hours)
    - license
    - license_url
    - coverage_notes (e.g., demographics, domain)
    - source_url
    - maintainer/contact
    - derived_from (original snapshot file)
    - notes (curation comments / caveats)
- reports/yoruba_registry_note.pdf
  - A concise report that describes data collection methodology, how metrics were computed, license compatibility, and a recommended roadmap for improving Yoruba speech resources.

## Data sources
- Mozilla Common Voice
  - Public JSON release snapshots are included (when available) in `data/`.
- OpenSLR
  - Catalog entries and metadata for SLR releases are included in `data/`.
- Coqui STT dataset index
  - Aggregated index entries are included in `data/`.
- Other public sources (added by contributors) may be included when available and documented.

## Reproducing the registry and the data note
1. Create a virtual environment (recommended)
   - python -m venv .venv
   - source .venv/bin/activate  (Linux/macOS)
   - .venv\Scripts\activate     (Windows)
2. Install dependencies
   - pip install -r requirements.txt
   - If there is no requirements file, the main dependencies are typically: pandas, python-dateutil, requests, jinja2, reportlab or pandoc (for PDF rendering). See `scripts/` for exact imports.
3. Run the scripts (from repository root)
   - python scripts/build_registry.py
     - Reads snapshots under `data/`, normalizes fields, and writes `data/yoruba_speech_registry.csv`.
   - python scripts/note_to_pdf.py
     - Reads the registry and produces `reports/yoruba_registry_note.pdf` (requires a working PDF renderer such as pandoc or wkhtmltopdf depending on implementation).
4. Inspect outputs
   - Open `data/yoruba_speech_registry.csv` to review the consolidated metadata.
   - Read `reports/yoruba_registry_note.pdf` for the summary, methodology, and recommended roadmap.

## Notes on reproducibility
- Source snapshots under `data/` are included to allow the registry to be rebuilt even if upstream sites change or remove files. If you want to refresh the snapshots from upstream, add new snapshots to `data/` (follow naming conventions used by scripts).
- The scripts perform normalization heuristics. If a source changes its schema, you may need to update parsing logic in `scripts/`.

## License and licensing guidance
- This repository primarily stores metadata and derived small files (the registry and the data note). The real audio and raw dataset contents are not hosted here.
- Each row in the registry includes a license column and a `license_url`. The registry does not change the license of the original datasets — always consult the original dataset license before reuse, redistribution, or model training.
- Before republishing any combined or redistributed dataset, ensure license compatibility and attribution. For datasets with restrictive or unclear licenses, contact the data maintainers.

## How to contribute
- Add new data source snapshots:
  - Place the original metadata snapshot file in `data/` and follow existing file naming patterns. Then open a pull request describing source and provenance.
- Improve parsers:
  - Edit or extend `scripts/build_registry.py` to support new dataset schemas. Add tests or sample snapshots to `data/` to demonstrate parser behavior.
- Correct metadata:
  - If you find errors in `data/yoruba_speech_registry.csv` or `reports/yoruba_registry_note.pdf`, please open an issue and a PR with fixes and a brief explanation.
- Add analyses:
  - Propose new metrics (e.g., speaker demographics, domain disaggregation) as code changes and document them in the data note.

## Suggested citation
- If you use the registry or the data note in work, please cite:
  - ProgrmerJack. "Common-Voice-OpenSLR: A curated registry of Yoruba (yo) speech resources." GitHub repository, commit <commit-hash>. (Replace with the commit you used.)

## Ethics and responsible use
- The registry is intended to make dataset metadata transparent. It does not replace due diligence about consent, demographic fairness, and privacy for downstream applications.
- When using audio datasets, consider potential harms and follow community best practices for speech data governance, user privacy, and consent.

## Roadmap and future work
- Expand coverage to additional Yoruba resources discovered in academic papers or lesser-known archives.
- Add per-speaker or per-utterance summary stats where available.
- Improve licensing validation and provenance tracking.
- Publish the registry and the data note on Zenodo (draft metadata available at `docs/zenodo_metadata.json`).

## Contact
- Maintainer: ProgrmerJack (GitHub)
- For questions or to propose new data sources, open an issue or a pull request.

## Acknowledgements
- Thanks to Mozilla Common Voice, OpenSLR, and the Coqui community for publicly accessible metadata and indexes that make this registry possible.
