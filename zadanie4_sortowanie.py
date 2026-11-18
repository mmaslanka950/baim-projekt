"""ZADANIE 4: Zabezpiecz sortowanie listy produktów.

Nazw kolumn ani kierunku sortowania (ASC / DESC) nie da się podać jako parametr
(znak ?), więc używa się BIAŁEJ LISTY: kod sprawdza, czy wartość od użytkownika
jest na liście dozwolonych, a jeśli nie, używa wartości domyślnej.

Twoje zadanie: uzupełnij funkcję lista() tak, aby:
  - kolumna mogła być tylko 'name' lub 'price' (domyślnie 'name'),
  - kierunek mógł być tylko 'ASC' lub 'DESC' (domyślnie 'ASC'),
  - wielkość liter w kierunku nie miała znaczenia ('desc' też działa jako DESC).

Uruchom:  python3 zadanie4_sortowanie.py
"""
from baza import polacz

db = polacz()

DOZWOLONE_KOLUMNY = ["name", "price"]
DOZWOLONE_KIERUNKI = ["ASC", "DESC"]


# ---------------------------------------------------------------
# TODO: popraw dwie linijki: 'kolumna' i 'kierunek'
# Podpowiedź: kolumna = sortuj_po if sortuj_po in DOZWOLONE_KOLUMNY else "name"
#             Dla kierunku najpierw zamień tekst na wielkie litery (.upper()).
def lista(sortuj_po, kierunek="ASC"):
    kolumna = sortuj_po
    kierunek = kierunek
    zapytanie = f"SELECT name, price FROM products ORDER BY {kolumna} {kierunek}"
    return db.execute(zapytanie).fetchall()
# ---------------------------------------------------------------


# ----- automatyczne sprawdzenie (nie zmieniaj) -----
def sprawdz():
    problemy = []

    try:
        ceny = [w[1] for w in lista("price", "DESC")]
        if ceny != sorted(ceny, reverse=True):
            problemy.append("sortowanie po price malejąco nie działa")
        nazwy = [w[0] for w in lista("name", "asc")]
        if nazwy != sorted(nazwy):
            problemy.append("sortowanie po name rosnąco (małe litery 'asc') nie działa")
    except Exception as e:
        problemy.append(f"poprawne sortowanie zgłosiło błąd: {e}")

    zle = [
        ("nieistnieje", "ASC"),
        ("price; DROP TABLE products", "ASC"),
        ("(SELECT 1)", "ASC"),
        ("name", "ASC; DROP TABLE products"),
        ("name", "DESC, price"),
    ]
    for kol, kier in zle:
        try:
            wynik = lista(kol, kier)
            if len(wynik) != 5:
                problemy.append(f"dla ({kol!r}, {kier!r}) zwrócono złą liczbę wierszy")
        except Exception as e:
            problemy.append(f"niedozwolona wartość ({kol!r}, {kier!r}) wywołała błąd: {e}")

    if problemy:
        print("JESZCZE NIE:")
        for p in problemy:
            print("  -", p)
    else:
        print("ZALICZONE: sortowanie przyjmuje tylko dozwolone wartości.")


sprawdz()
