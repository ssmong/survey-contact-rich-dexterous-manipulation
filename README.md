# Survey: Contact-Rich Dexterous Manipulation

An interactive survey of 150+ papers on contact-rich dexterous manipulation, covering RL-based methods, vision-language-action models, force-aware control, teleoperation, tactile sensing, and dexterous hand hardware.

**Live site:** https://ssmong.github.io/survey-contact-rich-dexterous-manipulation/

Available in English, [Korean](https://ssmong.github.io/survey-contact-rich-dexterous-manipulation/ko/), and [Chinese](https://ssmong.github.io/survey-contact-rich-dexterous-manipulation/zh/).

## Features

- Filterable and sortable tables with global search
- Per-paper detail pages with method summaries
- OpenReview peer review data (where available)
- Hand type filters (Dexterous, Gripper, Bimanual, Full Body)
- Dark / light theme toggle
- Responsive layout

## Structure

```
build.py            # Markdown → HTML build script
content/            # Survey source files (EN/KO/ZH)
  survey.md
  detailed/         # Per-paper detail pages
reviews/            # OpenReview data
scripts/            # Dev utilities (serve, fetch_reviews)
docs/               # Generated site (GitHub Pages)
```

## Building

```bash
python build.py
```

## Local dev server

```bash
pip install livereload
python scripts/serve.py
```

## Author

Yeonseo Lee · Seoul National University
