"""Mała baza testowa używana we wszystkich zadaniach.
Nic tu nie zmieniaj. Baza jest tworzona w pamięci przy każdym uruchomieniu.
"""
import sqlite3


def polacz():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, login TEXT, password TEXT)")
    db.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL, category TEXT)")
    db.executemany(
        "INSERT INTO users (login, password) VALUES (?, ?)",
        [("admin", "tajne123"), ("jan", "haslo456"), ("anna", "qwerty789")],
    )
    db.executemany(
        "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
        [
            ("Laptop", 3500.0, "komputery"),
            ("Mysz", 80.0, "komputery"),
            ("Klawiatura", 150.0, "komputery"),
            ("Telefon", 2000.0, "telefony"),
            ("Etui", 40.0, "telefony"),
        ],
    )
    return db
