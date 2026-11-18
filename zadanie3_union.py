"""ZADANIE 3: Wyciągnij loginy i hasła przez wyszukiwarkę produktów.

Wyszukiwarka pokazuje produkty z wybranej kategorii (np. 'komputery'),
ale jest PODATNA na SQL Injection.
Twoje zadanie: wpisz taką kategorię, aby wyszukiwarka pokazała też
loginy i hasła z tabeli users.

Uwaga: nie wiesz z góry, ile kolumn zwraca zapytanie. UNION wymaga takiej samej
liczby kolumn po obu stronach. Gdy się pomylisz, baza zgłosi błąd, a program go wypisze.

Uruchom:  python3 zadanie3_union.py
"""
import sqlite3

from baza import polacz

db = polacz()


def szukaj(kategoria):
    zapytanie = f"SELECT name, price, category FROM products WHERE category = '{kategoria}'"
    print("Zapytanie wysłane do bazy:")
    print("  ", zapytanie)
    try:
        return db.execute(zapytanie).fetchall()
    except sqlite3.Error as e:
        print("BŁĄD BAZY:", e)
        return []


# ---------------------------------------------------------------
# TODO: uzupełnij kategorię
# Podpowiedź 1: sprawdzaj liczbę kolumn, próbując: x' UNION SELECT NULL, NULL --
#               i dopisując kolejne NULL, aż błąd zniknie.
# Podpowiedź 2: gdy znasz liczbę kolumn, zamień dwa NULL na login i password,
#               a pozostałe kolumny wypełnij czymkolwiek (np. NULL).
KATEGORIA = "TODO"
# ---------------------------------------------------------------

wyniki = szukaj(KATEGORIA)
print("Wyniki:")
for wiersz in wyniki:
    print("  ", wiersz)

if any(w[0] == "admin" and w[1] == "tajne123" for w in wyniki):
    print("ZALICZONE: wyszukiwarka zdradziła dane z tabeli users.")
else:
    print("JESZCZE NIE: w wynikach nie ma loginów i haseł. Sprawdź podpowiedzi.")
