"""Descarrega e valida o conjunto de dados do Sprint 5 da TripleTen."""
import csv
from pathlib import Path
from urllib.request import Request, urlopen

DESTINATION = Path(__file__).resolve().parents[1] / "vehicles_us.csv"
SOURCES = [
    "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_NEW_4_sprint/vehicles.csv",
    "https://raw.githubusercontent.com/Pushkarski/05_used_car_sales_dashboard/main/vehicles_us.csv",
]
COLUMNS = {"price", "odometer", "model", "type", "condition"}

def validate(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        missing = COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Colunas em falta: {sorted(missing)}")
        count = sum(1 for _ in reader)
    if count < 50000:
        raise ValueError(f"CSV demasiado pequeno: {count}")
    return count

def main():
    if DESTINATION.exists():
        try:
            print(f"Dataset válido: {validate(DESTINATION)} anúncios")
            return
        except ValueError:
            pass
    temporary = DESTINATION.with_suffix(".download")
    errors = []
    for source in SOURCES:
        try:
            req = Request(source, headers={"User-Agent": "TripleTen-Sprint5/1.0"})
            with urlopen(req, timeout=60) as response, temporary.open("wb") as output:
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    output.write(chunk)
            count = validate(temporary)
            temporary.replace(DESTINATION)
            print(f"Dataset obtido: {count} anúncios")
            return
        except (OSError, ValueError) as error:
            errors.append(str(error))
            temporary.unlink(missing_ok=True)
    raise RuntimeError("Falha ao obter dataset: " + " | ".join(errors))

if __name__ == "__main__":
    main()
