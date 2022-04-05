import sqlite3

def create(data):
    cur.execute(
        "INSERT INTO persons "
        "(RodneCislo, Jmeno, Prijmeni, Narozeni, Mesto) "
        "VALUES (data[1], data[2], data[3], data[4], data[5]);"
    "")
    con.commit()

def delete(data):
    cur.execute(
        "UPDATE persons "
        "SET (RodneCislo, Jmeno, Prijmeni, Narozeni, Mesto)"
        "VALUES (data[1], data[2], data[3], data[4], data[5])"
        "WHERE RodneCislo = data[1];"
    "")
    con.commit()

def update(data):
    cur.execute(
        "INSERT INTO persons "
        "(RodneCislo, Jmeno, Prijmeni, Narozeni, Mesto) "
        "VALUES (data[1], data[2], data[3], data[4], data[5]);"
    "")

con = sqlite3.connect("example.db")
# na jaký soubor se připojujeme

cur = con.cursor()
# jakou DB používáme

"""
cur.execute("CREATE TABLE persons ("
    "RodneCislo int primary key,"
    "Jmeno varchar(255),"
    "Prijmeni varchar(255),"
    "Narozeni varchar(255),"
    "Mesto varchar(255)"
");")
"""

#cur.execute("DROP TABLE persons")

data = cur.execute("SELECT * FROM persons;")

for row in data:
    print(row)

con.commit()
con.close()