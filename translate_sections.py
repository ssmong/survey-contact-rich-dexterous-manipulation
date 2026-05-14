"""Translate detailed survey files from English to Korean for sections 5, 6, 7.

Applies structural label replacements and section-level heading translations.
"""
import re
from pathlib import Path

SOURCE_DIR = Path(r"C:\Users\Yeonseo\Documents\2_Job\survey-contact-rich-dexterous-manipulation\detailed_survey")
TARGET_DIR = Path(r"C:\Users\Yeonseo\Documents\2_Job\survey-contact-rich-dexterous-manipulation\detailed_survey_ko")

# Bold label translations (longest first to avoid partial replacement)
BOLD_LABEL_PAIRS = [
    ("Architecture/Parameters:", "아키텍처/파라미터:"),
    ("Code/data availability:", "코드/데이터 공개:"),
    ("Key Methodology:", "핵심 방법론:"),
    ("Key methodology:", "핵심 방법론:"),
    ("Main Contributions:", "주요 기여:"),
    ("Main contributions:", "주요 기여:"),
    ("Quantitative results:", "정량적 결과:"),
    ("Limitations/Gaps:", "한계점:"),
    ("Open weights/code:", "공개 가중치/코드:"),
    ("Hand Hardware:", "핸드 하드웨어:"),
    ("Hand hardware:", "핸드 하드웨어:"),
    ("Sim Platform:", "시뮬레이션 플랫폼:"),
    ("Sim platform:", "시뮬레이션 플랫폼:"),
    ("Venue/Year:", "학회/연도:"),
    ("Full Title:", "전체 제목:"),
    ("Full title:", "전체 제목:"),
    ("Authors:", "저자:"),
    ("Results:", "결과:"),
    ("Tasks:", "작업:"),
    ("Training data:", "훈련 데이터:"),
    ("Architecture:", "아키텍처:"),
    ("Action space:", "행동 공간:"),
    ("Dex hand support?", "다지 핸드 지원:"),
    ("Force/impedance output?", "힘/임피던스 출력:"),
    ("Robot platform:", "로봇 플랫폼:"),
    ("What is output:", "출력:"),
    ("How K/D are determined:", "K/D 결정 방법:"),
    ("RL algorithm:", "RL 알고리즘:"),
    ("Sim2Real?", "Sim2Real 여부:"),
    ("Object count:", "객체 수:"),
    ("Inclusion rationale:", "포함 근거:"),
    ("Code availability:", "코드 공개:"),
]

# Dash-prefixed label translations (for "- **Label:**" patterns inside sections)
DASH_LABEL_PAIRS = [
    ("Inference latency:", "추론 지연 시간:"),
    ("Deployment hardware:", "배포 하드웨어:"),
    ("Real-time capable?", "실시간 가능 여부:"),
    ("Collection method:", "수집 방법:"),
    ("Teleop equipment:", "원격 조작 장비:"),
    ("Publicly available?", "공개 여부:"),
    ("Dataset used:", "사용 데이터셋:"),
    ("Data format:", "데이터 포맷:"),
    ("Data scale:", "데이터 규모:"),
]

# Section heading translations
HEADING_PAIRS = [
    ("## Inference / Deployment", "## 추론 / 배포"),
    ("## Dataset / Data Collection", "## 데이터셋 / 데이터 수집"),
    ("### Cross-cutting Observations", "### 분야 횡단 관찰"),
    ("## Cross-cutting Observations", "## 분야 횡단 관찰"),
    ("### Cross-cutting observations", "### 분야 횡단 관찰"),
    ("## Cross-cutting observations", "## 분야 횡단 관찰"),
    ("## File Index", "## 파일 색인"),
    ("### VLA Foundation Model Families", "### VLA 기반 모델 패밀리"),
    ("### Other Major VLAs", "### 기타 주요 VLA"),
    ("### Visuomotor Policies", "### 시각운동 정책"),
    ("## Version History", "## 버전 이력"),
    ("## Robot Platforms", "## 로봇 플랫폼"),
    ("## Comparison with Other Major VLA Families", "## 다른 주요 VLA 패밀리와의 비교"),
]

# Sim-only limitation note translation
SIM_ONLY_PAIR = (
    "**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.",
    "**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.",
)


def translate_file(source_path: Path, target_path: Path) -> None:
    """Read source, apply structured label translations, write to target."""
    content = source_path.read_text(encoding="utf-8")

    # Bold label replacements
    for eng, kor in BOLD_LABEL_PAIRS:
        content = content.replace(f"**{eng}**", f"**{kor}**")

    # Dash-prefixed label replacements
    for eng, kor in DASH_LABEL_PAIRS:
        content = content.replace(f"- **{eng}**", f"- **{kor}**")

    # Section heading replacements
    for eng, kor in HEADING_PAIRS:
        content = content.replace(eng, kor)

    # Sim-only limitation note
    content = content.replace(SIM_ONLY_PAIR[0], SIM_ONLY_PAIR[1])

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(content, encoding="utf-8")


def main() -> None:
    sections = ["section5", "section6", "section7"]
    count = 0
    for section in sections:
        src_dir = SOURCE_DIR / section
        if not src_dir.exists():
            print(f"Source directory not found: {src_dir}")
            continue
        for md_file in sorted(src_dir.glob("*.md")):
            target_file = TARGET_DIR / section / md_file.name
            translate_file(md_file, target_file)
            count += 1
            print(f"  Translated: {section}/{md_file.name}")

    print(f"\nTotal files translated: {count}")


if __name__ == "__main__":
    main()
