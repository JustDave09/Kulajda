import sqlite3

# vytvoření DB v paměti
#con = sqlite3.connect(":memory:")

con = sqlite3.connect("example.db")
# na jaký soubor se připojujeme

cur = con.cursor()
# jakou DB používáme

cur.execute("SQL doraz")
# spustí sql dotaz v databázi se kterou pracujeme

con.close()
# přeruší spojení s databází


#Úkol: Update/delete/create systém s databází pomocí tkinter