from PySide.QtCore import *
from PySide.QtGui import *
from View import Ui_MainWindow
import sys
from Model import Model


class Controller(QMainWindow):
    """
    Der Controller steuert das ganze Frame, und die Zugriffe der Buttons
    """

    form=0
    number = -1

    def __init__(self, parent=None):
        """
        Konstruktor
        :param parent:
        """
        super().__init__(parent)
        self.form = Ui_MainWindow()
        self.form.setupUi(self)
        self.m = Model()
        self.buttonsConnect()

    def buttonsConnect(self):
        """
        Verbindet die Buttons mit der ausführenden Methode
        """
        for i in range(15):
            s="self.form.b%(number)s.clicked.connect(self.button)" %\
            {"number":i}
            exec(s)
        self.form.bEnde.clicked.connect(self.button)
        self.form.bNeu.clicked.connect(self.button)


    def button(self):
        """
        Diese Methode führt die Statistik des Models, abhängig von den gedrückten Buttons
        :return:
        """
        button = self.sender()
        if isinstance(button, QPushButton):
            self.form.lGesamt.setText(str(self.m.gesamt()))
            if button.text().isnumeric():
                if int(button.text())== self.number+1:
                    self.number+=1
                    button.setDisabled(True)
                    self.form.lKorrekt.setText(str(self.m.korrekt()))
                    self.form.lOffen.setText(str(self.m.offen()))
                else:
                    self.form.lFalsch.setText(str(self.m.falsch()))
            else:
                if int(button==self.form.bNeu):
                    self.number = -1
                    self.form.lSpiele.setText(str(self.m.reset()))
                    self.form.lGesamt.setText("0")
                    self.form.lKorrekt.setText("0")
                    self.form.lFalsch.setText("0")
                    self.form.lOffen.setText("15")
                    for i in range(15):
                        s = "self.form.b%(number)s.setEnabled(True)" % \
                            {"number": i}
                        exec(s)

                if int(button==self.form.bEnde):
                    sys.exit("Goodbye")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())