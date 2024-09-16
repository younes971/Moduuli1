import mysql.connector


def hae_lentokentta(icao_koodi):
    # Yhdistetään tietokantaan
    yhteys = mysql.connector.connect(
        user="Younes",
        host="localhost",
        password="lalamouka",
        database="flight_game",
    )

    # Luodaan kursori tietokantakyselyä varten
    kursori = yhteys.cursor()

    # Suoritetaan SQL-kysely
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao_koodi,))

    # Haetaan tulos
    tulos = kursori.fetchone()

    # Suljetaan kursori ja yhteys
    kursori.close()
    yhteys.close()

    # Tarkistetaan, löytyikö tuloksia
    if tulos:
        lentokentan_nimi, sijaintikunta = tulos
        print(f"Lentokentän nimi: {lentokentan_nimi}, sijaintikunta: {sijaintikunta}")
    else:
        print("Lentokenttää ei löydy kyseisellä ICAO-koodilla.")


# Kysytään käyttäjältä ICAO-koodi
icao_koodi = input("Anna lentokentän ICAO-koodi: ").upper()

# Haetaan ja tulostetaan lentokentän tiedot
hae_lentokentta(icao_koodi)