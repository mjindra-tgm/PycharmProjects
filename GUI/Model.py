class Model(object):
    """
    Nur die Statistik
    """
    __offen=15
    __gesamt=0
    __korrekt=0
    __falsch=0
    __spiele=0

    def __init(self):
        """
        Konstruktor
        """
        super.__init__()

    def offen(self):
        """
         Senkt die Zahl der offenen Züge, und gibt sie zurück.
         :return:  Anzahl der offenen Züge
         """

        self.__offen-=1
        return self.__offen

    def gesamt(self):
        """
         Erhöht die Anzahl der abgeschlossenen Züge, und gibt sie zurück.
         :return:  Anzahl der gesamten Züge
         """
        self.__gesamt+=1
        return self.__gesamt


    def falsch(self):
        """
         Erhöht die Anzahl der falschen Züge, und gibt sie zurück.
         :return:  Anzahl der falschen Züge
         """
        self.__falsch += 1
        return self.__falsch

    def korrekt(self):
        """
         Erhöht die Anzahl der korrekten Züge, und gibt sie zurück.
         :return:  Anzahl der korrekten Züge
         """
        self.__korrekt += 1
        return self.__korrekt

    def spiele(self):
        """
         Erhöht die Anzahl der Spiele, und gibt sie zurück.
         :return:  Anzahl der abgeschlossenen Spiele
         """
        self.__spiele += 1
        return self.__spiele

    def reset(self):
        """
         Starter ein neues Spiel
         :return:  Anzahl der abgeschlossenen Spiele
         """
        self.__gesamt=0
        self.__falsch=0
        self.__korrekt=0
        self.__offen=15
        return self.spiele()
