from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

kaksinpeli = KPSPelaajaVsPelaaja()
yksinpeli = KPSTekoaly()
haastava_yksinpeli = KPSParempiTekoaly()

def main():

    print("Valitse pelataanko"
            "\n (a) Ihmistä vastaan"
            "\n (b) Tekoälyä vastaan"
            "\n (c) Parannettua tekoälyä vastaan"
            "\nMuilla valinnoilla lopetetaan"
            )

    vastaus = input()
    käynnistapeli(vastaus)


def käynnistapeli(vastaus):
    print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s") 
    if vastaus.endswith("a"):
        kaksinpeli.pelaa()

    elif vastaus.endswith("b"):
        yksinpeli.pelaa()

    elif vastaus.endswith("c"):
        haastava_yksinpeli.pelaa()

if __name__ == "__main__":
    main()
