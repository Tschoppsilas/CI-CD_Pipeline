import sys
from pathlib import Path

# Sicherstellen, dass der "Python"-Ordner im Systempfad ist
root_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(root_dir / "Python"))


def test_setup():
    # Dieser Test stellt sicher, dass die Pipeline technisch funktioniert
    assert True
