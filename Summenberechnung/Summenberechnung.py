import threading


class Summenberechnung(threading.Thread):
    """
    Class to calculate the sum between to numbers

    - **methods**
        * :func: __init__ Konstruktor mit Start- und Endpunkt
        * :func: run Der Startpunkt für den Thread, und die threadübergreifende Berechnung von der Summe

    - **How to** use the class Summenberechnung

    :Example:
        >>> s = Summenberechnung(5, 10)
        >>> s.start()
        >>> print(Summenberechnung.value)
    """
    lock=threading.Lock()
    value=0

    def __init__(self, begin, end):
        """
        Konstruktor
        :param begin: Dies ist die Anfangszahl
        :param end:  Dies ist die Endzahl
        """
        threading.Thread.__init__(self)
        self.end=end
        self.begin=begin

    def run(self):
        """
        Die grundlegende Berechnung
        """
        for i in range(self.begin,self.end):
            with Summenberechnung.lock:
                Summenberechnung.value += i


number=input("Zahl eingeben")
while(not number.isnumeric()):
    print("Dies ist keine Zahl")
    number = input("Zahl eingeben")

number = int(number)

part = round(number/3)
for i in range(3):
    if(i==2):
        s = Summenberechnung(i * part, number+1)
    else:
        s = Summenberechnung(i * part, (i + 1) * part)
    s.start()


print(Summenberechnung.value)

