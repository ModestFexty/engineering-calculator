from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
import numpy as np
 
import sys

memory_list = []
 
 
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
 
        # setting title
        self.setWindowTitle("Engeneric Calculator")
 
        # setting geometry
        self.setGeometry(360, 654, 360, 654)
 
        # calling method
        self.UiComponents()

        self.setMaximumWidth(360)

        self.setMaximumHeight(654)
 
        # showing all the widgets
        self.show()

        self.setStyleSheet("Window"
                           "{"
                           "background: black;"
                           "}")

        # method for widgets
    def UiComponents(self):

        self.label = QLabel(self)
 
        # setting geometry to the label
        self.label.setGeometry(5, 5, 350, 73)
 
        # creating label multi line
        self.label.setWordWrap(True)
 
        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border: 2px solid black;"
                                 "background: white;"
                                 "}")
 
        # setting alignment to the label
        self.label.setAlignment(Qt.AlignRight)
 
        # setting font
        self.label.setFont(QFont('Arial', 20))
        
        self.setStyleSheet("QPushButton"
                                       "{"
                                       "background: white;"
                                       "font-size: 20px;"
                                       "}")


        push_sin = QPushButton("sin", self)
        push_sin.setGeometry(5, 126, 85, 40)

        push_cos = QPushButton("cos", self)
        push_cos.setGeometry(93, 126, 85, 40)

        push_tan = QPushButton("tan", self)
        push_tan.setGeometry(180, 126, 87, 40)

        push_cot = QPushButton("cot", self)
        push_cot.setGeometry(270, 126, 85, 40)

        push_arcsin = QPushButton("arcsin", self)
        push_arcsin.setGeometry(5, 170, 85, 40)

        push_arccos = QPushButton("arccos", self)
        push_arccos.setGeometry(93, 170, 85, 40)

        push_arctan = QPushButton("arctan", self)
        push_arctan.setGeometry(180, 170, 87, 40)

        push_arccot = QPushButton("arccot", self)
        push_arccot.setGeometry(270, 170, 85, 40)

        push_per = QPushButton("%", self)
        push_per.setGeometry(5, 214, 85, 40)

        push_fact = QPushButton("x!", self)
        push_fact.setGeometry(93, 214, 85, 40)

        push_rb = QPushButton("(", self)
        push_rb.setGeometry(180, 214, 87, 40)

        push_lb = QPushButton(")", self)
        push_lb.setGeometry(270, 214, 85, 40)

        push_abs = QPushButton("abs", self)
        push_abs.setGeometry(5, 258, 85, 40)

        push_div = QPushButton("div", self)
        push_div.setGeometry(93, 258, 85, 40)

        push_mod = QPushButton("mod", self)
        push_mod.setGeometry(180, 258, 87, 40)

        push_ln = QPushButton("ln", self)
        push_ln.setGeometry(270, 258, 85, 40)

        push_spower = QPushButton("x²", self)
        push_spower.setGeometry(5, 302, 85, 40)

        push_tpower = QPushButton("x³", self)
        push_tpower.setGeometry(93, 302, 85, 40)

        push_cpower = QPushButton("xⁿ", self)
        push_cpower.setGeometry(180, 302, 87, 40)

        push_pi = QPushButton("π", self)
        push_pi.setGeometry(270, 302, 85, 40)

        push_eul = QPushButton("e", self)
        push_eul.setGeometry(5, 346, 85, 40)

        push_sroot = QPushButton("\u00B2\u221A", self)
        push_sroot.setGeometry(93, 346, 85, 40)

        push_troot = QPushButton("\u00B3\u221A", self)
        push_troot.setGeometry(180, 346, 87, 40)

        push_croot = QPushButton("ⁿ\u221A", self)
        push_croot.setGeometry(270, 346, 85, 40)

        push_log = QPushButton("log", self)
        push_log.setGeometry(5, 390, 115, 40)

        push_erfx = QPushButton("erf(x)", self)
        push_erfx.setGeometry(123, 390, 115, 40)

        push_erfcx = QPushButton("erfc(x)", self)
        push_erfcx.setGeometry(241, 390, 114, 40)

        push_memory = QPushButton("M", self)
        push_memory.setGeometry(5, 434, 115, 40)

        push_memout = QPushButton("M+", self)
        push_memout.setGeometry(123, 434, 115, 40)

        push_memdel = QPushButton("M-", self)
        push_memdel.setGeometry(241, 434, 114, 40)

        push1 = QPushButton("1", self)
        push1.setGeometry(5, 478, 85, 40)
 
        push2 = QPushButton("2", self)
        push2.setGeometry(93, 478, 85, 40)

        push3 = QPushButton("3", self)
        push3.setGeometry(180, 478, 87, 40)

        push_mul = QPushButton("*", self)
        push_mul.setGeometry(270, 478, 85, 40)

        push4 = QPushButton("4", self)
        push4.setGeometry(5, 522, 85, 40)

        push5 = QPushButton("5", self)
        push5.setGeometry(93, 522, 85, 40)

        push6 = QPushButton("6", self)
        push6.setGeometry(180, 522, 87, 40)

        push_minus = QPushButton("-", self)
        push_minus.setGeometry(270, 522, 85, 40)

        push7 = QPushButton("7", self)
        push7.setGeometry(5, 566, 85, 40)

        push8 = QPushButton("8", self)
        push8.setGeometry(93, 566, 85, 40)

        push9 = QPushButton("9", self)
        push9.setGeometry(180, 566, 87, 40)

        push_plus = QPushButton("+", self)
        push_plus.setGeometry(270, 566, 85, 40)

        push0 = QPushButton("0", self)
        push0.setGeometry(5, 610, 85, 40)

        push_point = QPushButton(".", self)
        push_point.setGeometry(93, 610, 85, 40)

        push_tiv = QPushButton("/", self)
        push_tiv.setGeometry(180, 610, 87, 40)
 
        push_equal = QPushButton("=", self)
        push_equal.setGeometry(270, 610, 85, 40)

        push_clear = QPushButton("Clear", self)
        push_clear.setGeometry(5, 80, 173, 40)
 
        push_del = QPushButton("Del", self)
        push_del.setGeometry(180, 80, 175, 40)

        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)

        d1_effect = QGraphicsColorizeEffect()
        d1_effect.setColor(QColor(255, 79, 0))
        push_clear.setGraphicsEffect(d1_effect)

        d2_effect = QGraphicsColorizeEffect()
        d2_effect.setColor(QColor(255, 79, 0))
        push_del.setGraphicsEffect(d2_effect)

        m1_effect = QGraphicsColorizeEffect()
        m1_effect.setColor(QColor(153,102,204))
        push_memory.setGraphicsEffect(m1_effect)

        m2_effect = QGraphicsColorizeEffect()
        m2_effect.setColor(QColor(153,102,204))
        push_memout.setGraphicsEffect(m2_effect)

        m3_effect = QGraphicsColorizeEffect()
        m3_effect.setColor(QColor(153,102,204))
        push_memdel.setGraphicsEffect(m3_effect)

 
        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push_tiv.clicked.connect(self.action_tiv)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_del.clicked.connect(self.action_del)
        push_sin.clicked.connect(self.action_sin)
        push_cos.clicked.connect(self.action_cos)
        push_tan.clicked.connect(self.action_tan)
        push_cot.clicked.connect(self.action_cot)
        push_per.clicked.connect(self.action_per)
        push_fact.clicked.connect(self.action_fact)
        push_lb.clicked.connect(self.action_lb)
        push_rb.clicked.connect(self.action_rb)
        push_abs.clicked.connect(self.action_abs)
        push_div.clicked.connect(self.action_div)
        push_mod.clicked.connect(self.action_mod)
        push_ln.clicked.connect(self.action_ln)
        push_spower.clicked.connect(self.action_spower)
        push_cpower.clicked.connect(self.action_cpower)
        push_tpower.clicked.connect(self.action_tpower)
        push_pi.clicked.connect(self.action_pi)
        push_eul.clicked.connect(self.action_eul)
        push_sroot.clicked.connect(self.action_sroot)
        push_troot.clicked.connect(self.action_troot)
        push_croot.clicked.connect(self.action_croot)
        push_memory.clicked.connect(self.action_memory)
        push_memout.clicked.connect(self.action_memout)
        push_memdel.clicked.connect(self.action_memdel)
        push_arcsin.clicked.connect(self.action_arcsin)
        push_arccos.clicked.connect(self.action_arccos)
        push_arctan.clicked.connect(self.action_arctan)
        push_arccot.clicked.connect(self.action_arccot)
        push_log.clicked.connect(self.action_log)
        push_erfx.clicked.connect(self.action_erfx)
        push_erfcx.clicked.connect(self.action_erfcx)
 
 
    def action_equal(self):
        equation = self.label.text()
        try:
            ans = eval(equation)
            self.label.setText(str(ans))
            text = self.label.text()
            if len(text) > 18:
                self.label.setText("overflow")
        except:
            self.label.setText("error")

    def action_lb(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ")")
        if len(text) > 18:
            self.label.setText("overflow")

    def action_rb(self):
        text = self.label.text()
        self.label.setText(text + "(")
        if len(text) > 18:
            self.label.setText("overflow")            
 
    def action_plus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " + ")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action_minus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " - ")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action_mul(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " * ")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action_point(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ".")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action0(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "0")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action1(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "1")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action2(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "2")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action3(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "3")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action4(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "4")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action5(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "5")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action6(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "6")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action7(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "7")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action8(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "8")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action9(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "9")
        if len(text) > 18:
            self.label.setText("overflow")

    def action_memory(self):
        text = self.label.text()
        global memory_list
        memory_list.append(text)
        print(memory_list)

    def action_memout(self):
        try:
            text = self.label.text()
            memory_text = memory_list[0]
            self.label.setText(f"{text}{memory_text}")
        except:
            self.label.setText("no data")

    def action_memdel(self):
        global memory_list
        memory_list.clear()

    def action_log(self):
        try:
            text = self.label.text()
            log = str(math.log(float(text)))
            self.label.setText(log)
        except:
            self.label.setText("error")

    def action_erfx(self):
        try:
            text = self.label.text()
            erfx = str(math.erf(float(text)))
            self.label.setText(erfx)
            if len(text) > 18:
                erfx = round(erfx[18])
        except:
            self.label.setText("error")

    def action_erfcx(self):
        try:
            text = self.label.text()
            erfcx = str(math.erfc(float(text)))
            erfcx = round(erfcx[15])
            self.label.setText(erfcx)
        except:
            self.label.setText("error") 

    def action_sin(self):
        try:
            text = self.label.text()
            sin = str(math.sin(math.radians(float(text))))
            self.label.setText(sin)
        except:
            self.label.setText("error")

    def action_cos(self):
        try:
            text = self.label.text()
            cos = str(math.cos(math.radians(float(text))))
            self.label.setText(cos)
        except:
            self.label.setText("error")

    def action_tan(self):
        try:
            text = self.label.text()
            tan = str(math.tan(math.radians(float(text))))
            self.label.setText(tan)
        except:
            self.label.setText("error")

    def action_cot(self):
        try:
            text = self.label.text()
            cot = str(1/math.tan(math.radians(float(text))))
            self.label.setText(cot)
        except:
            self.label.setText("error")

    def action_arcsin(self):
        try:
            text = self.label.text()
            arcsin = str(np.arcsin(float(text)))
            self.label.setText(arcsin)
        except:
            self.label.setText("error")

    def action_arccos(self):
        try:
            text = self.label.text()
            arccos = str(np.arccos(float(text)))
            self.label.setText(arccos)
        except:
            self.label.setText("error")

    def action_arctan(self):
        try:
            text = self.label.text()
            arctan = str(np.arctan(float(text)))
            self.label.setText(arctan)
        except:
            self.label.setText("error")

    def action_arccot(self):
        try:
            text = self.label.text()
            arccot = str(math.pi/2 - np.arctan(int(text)))
            self.label.setText(arccot)
        except:
            self.label.setText("error")

    def action_per(self):
        try:
            text = self.label.text()
            per = str(eval(text+'/100'))
            self.label.setText(per)
        except:
            self.label.setText("error")

    def action_fact(self):
        try:
            text = self.label.text()
            fact = str(math.factorial(int(text)))
            self.label.setText(fact)
        except:
            self.label.setText("error")

    def action_abs(self):
        try:
            text = self.label.text()
            self.label.setText(text + "abs(")
            if len(text) > 18:
                self.label.setText("overflow")
        except:
            self.label.setText("error")

    def action_mod(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "%")
        if len(text) > 18:
            self.label.setText("overflow")

    def action_tiv(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "/")
        if len(text) > 18:
            self.label.setText("overflow")

    def action_div(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "//")
        if len(text) > 18:
            self.label.setText("overflow")

    def action_ln(self):
        text = self.label.text()
        ln = str(math.log10(int(text)))
        self.label.setText(ln)

    def action_spower(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "**2")
        if len(text) > 18:
            self.label.setText("overflow")

    def action_tpower(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "**3")
        if len(text) > 18:
            self.label.setText("overflow")

    def action_pi(self):
        # appending label text
        text = self.label.text()
        pi = text + str(math.pi)
        self.label.setText(pi)

    def action_eul(self):
        # appending label text
        text = self.label.text()
        eul = text + str(math.e)
        self.label.setText(eul)

    def action_sroot(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "**(1/2)")
        if len(text) > 18:
            self.label.setText("overflow")

    def action_troot(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "**(1/3)")
        if len(text) > 18:
            self.label.setText("overflow")

    def action_croot(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "**(1/")
        if len(text) > 18:
            self.label.setText("overflow")

    def action_cpower(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "**")
        if len(text) > 18:
            self.label.setText("overflow")
 
    def action_clear(self):
        # clearing the label text
        self.label.setText("")
 
    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])
 
 
# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = Window()
 
# start the app
sys.exit(App.exec())