import time
class FsmEfe:
    def __init__(self):

        self.ilkRenk = "kirmizi"
        self.ikinciRenk = "sari"
        self.sonRenk = "yesil"

        self.state_renk = "kirmizi"

        self.ilk_renk_zeit = 10
        self.ikinci_renk_zeit = 2
        self.son_renk_zeit = 15

        self.start_sari=0
        self.start_yesil=0
        self.start_kirmizi = time.time()


    def kirmiziyi_yak(self):
        if self.state_renk == self.ilkRenk:
            print(self.state_renk)
            if self.ilk_renk_zeit <= time.time() - self.start_kirmizi:
                self.state_renk = self.ikinciRenk
                self.start_sari = time.time()



    def sariyi_yak(self):
        if self.state_renk == self.ikinciRenk:
            print(self.state_renk)
            if self.ikinci_renk_zeit <= time.time() - self.start_sari:
                self.state_renk = self.sonRenk
                self.start_yesil = time.time()



    def yesili_yak(self):
        if self.state_renk == self.sonRenk:
            print(self.state_renk)
            if self.son_renk_zeit <= time.time() - self.start_yesil:
                self.state_renk = self.ilkRenk
                self.start_kirmizi= time.time()






