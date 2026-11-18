"""ZADANIE 2: Napraw DWIE podatne funkcje.

Obie funkcje (logowanie i szukaj_produkt) sklejają zapytanie z tekstu.
Twoje zadanie: zamień obie na zapytania parametryzowane.

W bibliotece sqlite3 parametr oznacza się znakiem ?, a wartości podaje osobno:
    db.execute("SELECT ... WHERE a = ? AND b = ?", (wartosc_a, wartosc_b))

Uwaga do drugiej funkcji: wyszukiwanie używa LIKE z znakami % po obu stronach.
Znaków % NIE wpisuje się w zapytaniu w cudzysłowie. Dopisz je do wartości,
którą przekazujesz jako parametr.

Uruchom:  python3 zadanie2_napraw.py
Program sam sprawdzi, czy obie funkcje działają i czy są odporne na atak.
"""
from baza import polacz

db = polacz()


# ---------------------------------------------------------------
# TODO 1: przepisz tę funkcję tak, aby używała znaków ?
def logowanie(login, haslo):
    zapytanie = (
        f"SELECT id, login FROM users "
        f"WHERE login = '{login}' AND password = '{haslo}'"
    )
    return db.execute(zapytanie).fetchone()


# TODO 2: przepisz tę funkcję tak, aby używała znaku ?
def szukaj_produkt(fraza):
    zapytanie = f"SELECT name, price FROM products WHERE name LIKE '%{fraza}%'"
    return db.execute(zapytanie).fetchall()
# ---------------------------------------------------------------


# ----- automatyczne sprawdzenie (nie zmieniaj) -----
def sprawdz():
    problemy = []

    try:
        if logowanie("admin", "tajne123") is None:
            problemy.append("logowanie: poprawny login i hasło nie działają")
        if logowanie("admin", "zle") is not None:
            problemy.append("logowanie: zalogowało przy złym haśle")
        if logowanie("admin' -- ", "x") is not None:
            problemy.append("logowanie: atak z komentarzem nadal działa")
        if logowanie("' OR '1'='1", "' OR '1'='1") is not None:
            problemy.append("logowanie: atak z OR '1'='1' nadal działa")
    except Exception as e:
        problemy.append(f"logowanie: funkcja zgłosiła błąd: {e}")

    try:
        if ("Mysz", 80.0) not in szukaj_produkt("Mys"):
            problemy.append("szukaj_produkt: fraza 'Mys' nie znajduje myszy")
        if len(szukaj_produkt("t")) < 3:
            problemy.append("szukaj_produkt: fraza 't' powinna znaleźć kilka produktów")
        if szukaj_produkt("zzz' OR '1'='1") != []:
            problemy.append("szukaj_produkt: atak z OR '1'='1' nadal działa")
        if szukaj_produkt("zzz' UNION SELECT login, 0 FROM users -- ") != []:
            problemy.append("szukaj_produkt: atak UNION nadal działa")
    except Exception as e:
        problemy.append(f"szukaj_produkt: funkcja zgłosiła błąd: {e}")

    if problemy:
        print("JESZCZE NIE:")
        for p in problemy:
            print("  -", p)
    else:
        print("ZALICZONE: obie funkcje działają i są odporne na atak.")


sprawdz()
