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

## Building

```bash
python build.py
```

This reads `survey.md` (and `survey_ko.md`, `survey_zh.md`) plus the `detailed_survey/` directories and generates the static site into `docs/`.

## Local dev server

```bash
pip install livereload
python serve.py
```

Auto-rebuilds on changes to source files.

## Author

Yeonseo Lee · Seoul National University
