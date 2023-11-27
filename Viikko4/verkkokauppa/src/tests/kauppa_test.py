import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
        
        def tilisiirto(nimi,viite,tilinumero, tili_numero, summa):
            if nimi == "pekka" and tilinumero == "12345" and viite == 42 and tili_numero == "33333-44455" and summa == 5:
                return

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        pankki_mock.tilisiirto.side_effect = tilisiirto

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called_once_with("pekka", 42, "12345", "33333-44455", 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostetaan_kaksi_eri_tuotetta_joita_varastossa_on(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 10
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "Hevonen", 5)
        
        def tilisiirto(nimi,viite,tilinumero, tili_numero, summa):
            if nimi == "pekka" and tilinumero == "12345" and viite == 42 and tili_numero == "33333-44455" and summa == 10:
                return

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        pankki_mock.tilisiirto.side_effect = tilisiirto


        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_once_with("pekka", 42, "12345", "33333-44455", 10)
    
    def test_ostetaan_kaksi_samaa_tuotetta_joita_varastossa_on(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 10
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "Hevonen", 5)
        
        def tilisiirto(nimi,viite,tilinumero, tili_numero, summa):
            if nimi == "pekka" and tilinumero == "12345" and viite == 42 and tili_numero == "33333-44455" and summa == 10:
                return

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        pankki_mock.tilisiirto.side_effect = tilisiirto


        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_once_with("pekka", 42, "12345", "33333-44455", 10)
    

    def test_ostetaan_kaksi_tuotetta_joita_toinen_on_loppu(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 0
        
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "Hevonen", 5)
        
        def tilisiirto(nimi,viite,tilinumero, tili_numero, summa):
            if nimi == "pekka" and tilinumero == "12345" and viite == 42 and tili_numero == "33333-44455" and summa == 5:
                return

        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        pankki_mock.tilisiirto.side_effect = tilisiirto


        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        pankki_mock.tilisiirto.assert_called_once_with("pekka", 42, "12345", "33333-44455", 5)

    def test_edellinen_asiointi_nollataan(self):
    