KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetti ei voi olla negatiivinen")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetti ei voi olla negatiivinen")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lista = self._luo_lista(self.kapasiteetti)

        self.alkioiden_määrä = 0

    def kuuluu(self, luku):

        for i in range(0, self.alkioiden_määrä):
            if luku == self.lista[i]:
                return True
            
        return False

    def lisaa(self, luku):
    
        if not self.kuuluu(luku):
            self.lista[self.alkioiden_määrä] = luku
            self.alkioiden_määrä = self.alkioiden_määrä + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_määrä % len(self.lista) == 0:
             
                vanha_lista = self.lista.copy()
                self.lista = self._luo_lista(self.alkioiden_määrä + self.kasvatuskoko)
                self.kopioi_lista(vanha_lista, self.lista)
     
            return True

        return False

    def poista(self, luku):
        
        poistetunluvun_kohta = -1
        
        for i in range(0, self.alkioiden_määrä):
            if luku == self.lista[i]:
                poistetunluvun_kohta = i
                self.lista[i] = 0
                break

        if poistetunluvun_kohta != -1:
            for j in range(poistetunluvun_kohta, self.alkioiden_määrä - 1):
                self.lista[j] = self.lista[j + 1]

            self.alkioiden_määrä = self.alkioiden_määrä - 1
            return True

        return False

    def kopioi_lista(self, vanha_lista, nykyinen_lista):
        
        for i in range(0, len(vanha_lista)):
            nykyinen_lista[i] = vanha_lista[i]

    def listan_pituus(self):
        return self.alkioiden_määrä

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_määrä)

        for i in range(0, len(taulu)):
            taulu[i] = self.lista[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_määrä == 0:
            return "{}"
        else:
            return "{" + ", ".join(map(str, self.lista[:self.alkioiden_määrä])) + "}"
