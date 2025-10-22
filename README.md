# Common-Voice-OpenSLR

This repository now curates Yoruba (`yo`) speech resource metadata drawn from Mozilla Common Voice, OpenSLR, and the Coqui STT dataset index. The curated outputs include:

- `data/yoruba_speech_registry.csv` – consolidated registry capturing release information, coverage metrics, licensing notes, and identified gaps for each source.
- `reports/yoruba_registry_note.pdf` – four-page data note detailing methodology, gap analysis, and a roadmap for improving Yoruba speech resources.
- `docs/zenodo_metadata.json` – draft metadata for publishing the registry and data note on Zenodo.

### Reproducing the registry

```bash
python scripts/build_registry.py
python scripts/note_to_pdf.py
```

Source metadata snapshots (Common Voice Corpus 23.0 JSON, OpenSLR SLR86 catalogue extracts, and the Coqui index) are stored under `data/` for transparency.