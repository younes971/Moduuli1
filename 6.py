

import random

def heita_noppaa():
    return random.randint(1, 6)

def paohjelma():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heita_noppaa()
        print(f"Noppa antoi: {silmaluku}")






import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

def paohjelma():

    tahkot = int(input("Anna nopan tahkojen määrä: "))
    maksimi_silmaluku = tahkot

    silmaluku = 0
    while silmaluku != maksimi_silmaluku:
        silmaluku = heita_noppaa(tahkot)
        print(f"Noppa antoi: {silmaluku}")






def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

def paohjelma():
    while True:

        gallonat = float(input("Anna bensiinimäärä gallonoina (negatiivinen luku lopettaa): "))

        if gallonat < 0:
            print("Ohjelma lopetetaan.")
            break

        litrat = gallonat_litroiksi(gallonat)

        print(f"{gallonat} gallonaa on {litrat:.2f} litraa.")









def laske_summa(luvut):
    return sum(luvut)

def paohjelma():

    testilista = [3, 7, 2, 9, 4]

    summa = laske_summa(testilista)

    print(f"Listan {testilista} summa on: {summa}")







def main():

    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    karsittu_lista = poista_parittomat(alkuperainen_lista)

    print("Alkuperäinen lista:", alkuperainen_lista)
    print("Karsittu lista (vain parilliset):", karsittu_lista)


if __name__ == "__main__":
    main()



