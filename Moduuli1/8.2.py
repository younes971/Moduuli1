import mysql.connector


def hae_lentokentat_maittain(maakoodi):
    # Yhdistetään tietokantaan
    yhteys = mysql.connector.connect(
        user="Younes",
        host="localhost",
        password="lalamouka",
        database="flight_game",
    )

    # Luodaan kursori tietokantakyselyä varten
    kursori = yhteys.cursor()

    # SQL-kysely, joka ryhmittelee lentokentät tyypin mukaan ja laskee määrät
    sql = """
        SELECT type, COUNT(*) as count
        FROM airport
        WHERE iso_country = %s
        GROUP BY type
    """
    kursori.execute(sql, (maakoodi,))

    # Haetaan tulokset
    tulokset = kursori.fetchall()

    # Suljetaan kursori ja yhteys
    kursori.close()
    yhteys.close()

    # Tulostetaan lentokenttien määrät tyypeittäin
    if tulokset:
        print(f"Lentokenttien lukumäärät maassa {maakoodi}:")
        for tyyppi, maara in tulokset:
            print(f"{tyyppi}: {maara} kpl")
    else:
        print(f"Ei lentokenttiä löytynyt maasta {maakoodi}.")


# Kysytään käyttäjältä maakoodi
maakoodi = input("Anna maan maakoodi (esim. FI): ").upper()

# Haetaan ja tulostetaan lentokenttien lukumäärät tyypeittäin
hae_lentokentat_maittain(maakoodi)
