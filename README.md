# Laboratorium: SQL Injection (4 zadania)

Wszystkie zadania to proste skrypty w Pythonie. Nie trzeba nic instalować,
wystarczy Python 3 (biblioteka sqlite3 jest wbudowana). Baza danych jest
tworzona w pamięci przy każdym uruchomieniu, więc niczego nie da się zepsuć.

## Jak pracować

1. Otwórz plik zadania w edytorze (np. Notatnik, VS Code, IDLE).
2. Znajdź miejsce oznaczone `TODO` i uzupełnij je.
3. Uruchom plik w terminalu:

```
python3 zadanie1_atak.py
```

(na Windowsie często `python zadanie1_atak.py`)

4. Program wypisze `ZALICZONE` albo `JESZCZE NIE` z podpowiedzią, co poprawić.

## Zadania

| Plik | Co robisz | Temat z prezentacji |
|------|-----------|---------------------|
| `zadanie1_atak.py` | Logujesz się jako konkretny użytkownik (anna) bez hasła | Komentarz SQL i warunek OR |
| `zadanie2_napraw.py` | Naprawiasz dwie podatne funkcje (logowanie i wyszukiwarka z LIKE) | Obrona 1 |
| `zadanie3_union.py` | Wyciągasz loginy i hasła, ustalając najpierw liczbę kolumn | UNION SELECT |
| `zadanie4_sortowanie.py` | Zabezpieczasz sortowanie (kolumna i kierunek) białą listą | Obrona 2 |

Zalecana kolejność: 1, 2, 3, 4. Gotowe rozwiązania są w folderze `rozwiazania/`
(zajrzyj tam dopiero po własnej próbie).

## Ważne

Ćwiczenia wykonuj tylko w tym laboratorium. Atakowanie cudzych systemów
bez zgody właściciela jest przestępstwem (art. 267 k.k.).
