import unittest
from unittest.mock import Mock, ANY, PropertyMock
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 10
        
        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 4
        
        #Tee maksusuoritus
        self.kassa.osta_lounas(maksukortti_mock)

        # Tarkista että saldo ei ole muuttunut
        self.assertEqual(maksukortti_mock.saldo, 4)

    
    def test_kortille_lisataan_saldoa(self):
        # Luo Mock-olio ja aseta sille alkusaldo
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 0

        # Määritä lataa-metodin toiminta
        def lataa(maara):
            maksukortti_mock.saldo += maara

        # Aseta Mock-oliolle lataa-metodi
        maksukortti_mock.lataa = lataa

        # Kutsu kassan lataa-metodia
        self.kassa.lataa(maksukortti_mock, 10)

        # Tarkista, että saldo on päivitetty oikein
        self.assertEqual(maksukortti_mock.saldo, 10)


    def test_kortille_ei_lisata_negatiivista_summaa(self):
        # Luo Mock-olio ja aseta sille alkusaldo
        maksukortti_mock = Mock()
        maksukortti_mock.saldo = 0

        #Määritä lataa-metodin toiminta
        def lataa(maara):
            if maara < 0:
                return
            maksukortti_mock.saldo += maara

        # Aseta Mock-oliolle lataa-metodi
        maksukortti_mock.lataa = lataa
        
        # Kutsu kassan lataa-metodia
        self.kassa.lataa(maksukortti_mock, -10)

        # Tarkista, että saldo on edelleen sama
        self.assertEqual(maksukortti_mock.saldo, 0)



