"""ZADANIE 1: Zaloguj się jako 'anna', nie znając jej hasła.

Funkcja logowanie() jest PODATNA: skleja zapytanie z tekstu.
Uwaga: sprytny trik "zawsze prawdziwy warunek" (OR '1'='1') zaloguje Cię
na PIERWSZE konto z tabeli (czyli admina), a Ty masz wejść dokładnie na konto 'anna'.

Twoje zadanie: ustaw LOGIN i HASLO tak, aby funkcja zalogowała Cię jako 'anna'.
Możesz zmieniać obie wartości.

Uruchom:  python3 zadanie1_atak.py
"""
from baza import polacz

db = polacz()


def logowanie(login, haslo):
    zapytanie = (
        f"SELECT id, login FROM users "
        f"WHERE login = '{login}' AND password = '{haslo}'"
    )
    print("Zapytanie wysłane do bazy:")
    print("  ", zapytanie)
    return db.execute(zapytanie).fetchone()


# ---------------------------------------------------------------
# TODO: uzupełnij LOGIN (HASLO może zostać jakie chcesz)
# Podpowiedź: warunek możesz dopisać przez OR, a resztę zapytania zakomentować.
LOGIN = "TODO"
HASLO = "cokolwiek"
# ---------------------------------------------------------------

wynik = logowanie(LOGIN, HASLO)
print("Wynik:", wynik)

if wynik is not None and wynik[1] == "anna":
    print("ZALICZONE: zalogowano jako anna bez znajomości hasła.")
elif wynik is not None:
    print(f"JESZCZE NIE: zalogowano jako '{wynik[1]}', a miała być 'anna'.")
else:
    print("JESZCZE NIE: nikt nie został zalogowany. Spójrz, jak wygląda zapytanie wyżej.")
