"""
Passwort-Generator
- Simples Skript zur Erstellung von starken Passwörtern
- Nutzer bestimmt Passwortlänge
- Nutzer bestimmt auszuschließende Zeichen
- Nutzer bestimmt außerdem Zeichenketten, die vorkommen sollen
- Skript schlägt immer mehrere Passwörter vor – Nutzer sucht sich letztlich eines aus, das dann in die Ablage kopiert wird
"""

import string
import random


def generiere_passwort(anz_zeichen, ohne, zeichenkette, anz_passwörter):
    alle_zeichen = string.ascii_letters + string.digits + string.punctuation

    # "Lösche" alle Zeichen aus "ohne" aus "alle_zeichen"
    for c in ohne:
        alle_zeichen = alle_zeichen.replace(c, "")

    passwörter = []

    for i in range(anz_passwörter):
        passwort = [random.choice(alle_zeichen) for j in range(anz_zeichen)]

        i_rndm = random.randrange(anz_zeichen - len(zeichenkette) + 1)
        passwort[i_rndm : i_rndm + len(zeichenkette)] = zeichenkette

        passwörter.append("".join(passwort))

    print("Passwörter: ", passwörter)
    return passwörter


generiere_passwort(10, "abc", "g6<", 3)