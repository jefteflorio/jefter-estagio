class Televisao:
    def __init__(self, canal, volume, mudo):
        self.canal = canal
        self.volume = volume
        self.mudo = mudo

    def alternarMudo(self, mudo):
        if mudo:
            self.mudo = True
        else:
            self.mudo = False
