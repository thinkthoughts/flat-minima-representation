from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"
FIGURES = ROOT / "figures"

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)
    return path
