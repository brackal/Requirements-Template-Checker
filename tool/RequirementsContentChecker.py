import pandas as pd
import re

# Prozesswortliste
prozesswoerter = [
    "abrufen", "senden", "setzen", "überwachen"
]

# Modalverben
modalverben = ["muss", "sollte", "wird"]

# Bedingungswörter
bedingungen = ["falls", "sobald", "solange"]
verbotene_konjunktionen = ["wenn"]

# Prüffunktion für eine einzelne Anforderung
def pruefe_anforderung(text):
    ergebnisse = {}

    # System benannt
    ergebnisse["System benannt"] = "✔" if "TEST-FW" in text else "✘"

    # Modalverb korrekt verwendet
    ergebnisse["Modalverb korrekt verwendet"] = "✔" if any(mv in text.lower() for mv in modalverben) else "✘"

    # Prozesswort vorhanden & korrekt
    gueltige_prozesswoerter = [pw for pw in prozesswoerter if pw in text]
    ergebnisse["Prozesswort vorhanden & korrekt"] = "✔" if gueltige_prozesswoerter else "✘"

    # Objekt sinnvoll gewählt (unabhängig vom Prozesswort)
    objekt_erkannt = bool(re.search(r"Messwert|Kommunikationsadresse|Wert|ID|Sensor|Systemstatus", text))
    ergebnisse["Objekt sinnvoll gewählt"] = "✔" if objekt_erkannt else "✘"

    # Funktionsart erkennbar
    if "die Möglichkeit bieten" in text:
        ergebnisse["Funktionsart erkennbar"] = "✔ (Benutzerinteraktion)"
    elif "fähig sein" in text:
        ergebnisse["Funktionsart erkennbar"] = "✔ (Schnittstelle)"
    else:
        ergebnisse["Funktionsart erkennbar"] = "✔ (Systemaktivität)"

    # Bedingung korrekt formuliert
    if any(b in text.lower() for b in bedingungen):
        ergebnisse["Bedingung korrekt formuliert"] = "✔"
    elif any(w in text.lower() for w in verbotene_konjunktionen):
        ergebnisse["Bedingung korrekt formuliert"] = "✘"
    else:
        ergebnisse["Bedingung korrekt formuliert"] = "✔ (keine Bedingung)"

    # Satzstruktur korrekt
    ergebnisse["Satzstruktur korrekt"] = "✔" if ergebnisse["Modalverb korrekt verwendet"] == "✔" and ergebnisse["Prozesswort vorhanden & korrekt"] == "✔" else "✘"

    # Semantik eindeutig
    ergebnisse["Semantik eindeutig"] = "✔" if len(text) > 20 else "✘"

    return ergebnisse

# Hauptfunktion
def pruefe_datei(pfad_csv, pfad_excel):
    df = pd.read_csv(pfad_csv)
    pruefungen = []

    for _, row in df.iterrows():
        ergebnisse = pruefe_anforderung(row["Anforderung"])
        pruefungen.append({"Nr.": row["Nr."], "Anforderung": row["Anforderung"], **ergebnisse})

    df_result = pd.DataFrame(pruefungen)
    df_result.to_excel(pfad_excel, index=False)
    print(f"Ergebnisse gespeichert in: {pfad_excel}")

# Beispielaufruf
if __name__ == "__main__":
    pruefe_datei("../requirements/requirements.csv", "checkResults.xlsx")
