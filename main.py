import math
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QLineEdit
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFontDatabase, QIntValidator
import sys
import os

resource_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

if getattr(sys, 'frozen', False):
    RELATIVE_PATH = os.path.dirname(sys.executable)
else:
    RELATIVE_PATH = os.path.dirname(__file__)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        QFontDatabase.addApplicationFont(os.path.join(resource_path, '3270-Regular.otf'))
        loadUi(os.path.join(resource_path, 'MainWindow.ui'), self)
        for child_widget in self.findChildren(QtWidgets.QWidget):
            if isinstance(child_widget, QtWidgets.QLineEdit):
                child_widget.setValidator(QIntValidator())
        self.q1d1.editingFinished.connect(lambda:self.totalScrapValue(0))
        self.q1d2.editingFinished.connect(lambda:self.totalScrapValue(0))
        self.q1d3.editingFinished.connect(lambda:self.totalScrapValue(0))
        self.q1sold.editingFinished.connect(lambda:self.totalScrapSold(0))
        self.q2.editingFinished.connect(lambda:self.newQuota(1))
        self.q2d1.editingFinished.connect(lambda:self.totalScrapValue(1))
        self.q2d2.editingFinished.connect(lambda:self.totalScrapValue(1))
        self.q2d3.editingFinished.connect(lambda:self.totalScrapValue(1))
        self.q2sold.editingFinished.connect(lambda:self.totalScrapSold(1))
        self.q3.editingFinished.connect(lambda:self.newQuota(2))
        self.q3d1.editingFinished.connect(lambda:self.totalScrapValue(2))
        self.q3d2.editingFinished.connect(lambda:self.totalScrapValue(2))
        self.q3d3.editingFinished.connect(lambda:self.totalScrapValue(2))
        self.q3sold.editingFinished.connect(lambda:self.totalScrapSold(2))
        self.q4.editingFinished.connect(lambda:self.newQuota(3))
        self.q4d1.editingFinished.connect(lambda:self.totalScrapValue(3))
        self.q4d2.editingFinished.connect(lambda:self.totalScrapValue(3))
        self.q4d3.editingFinished.connect(lambda:self.totalScrapValue(3))
        self.q4sold.editingFinished.connect(lambda:self.totalScrapSold(3))
        self.q5.editingFinished.connect(lambda:self.newQuota(4))
        self.q5d1.editingFinished.connect(lambda:self.totalScrapValue(4))
        self.q5d2.editingFinished.connect(lambda:self.totalScrapValue(4))
        self.q5d3.editingFinished.connect(lambda:self.totalScrapValue(4))
        self.q5sold.editingFinished.connect(lambda:self.totalScrapSold(4))
        self.q6.editingFinished.connect(lambda:self.newQuota(5))
        self.q6d1.editingFinished.connect(lambda:self.totalScrapValue(5))
        self.q6d2.editingFinished.connect(lambda:self.totalScrapValue(5))
        self.q6d3.editingFinished.connect(lambda:self.totalScrapValue(5))
        self.q6sold.editingFinished.connect(lambda:self.totalScrapSold(5))
        self.q7.editingFinished.connect(lambda:self.newQuota(6))
        self.q7d1.editingFinished.connect(lambda:self.totalScrapValue(6))
        self.q7d2.editingFinished.connect(lambda:self.totalScrapValue(6))
        self.q7d3.editingFinished.connect(lambda:self.totalScrapValue(6))
        self.q7sold.editingFinished.connect(lambda:self.totalScrapSold(6))
        self.q8.editingFinished.connect(lambda:self.newQuota(7))
        self.q8d1.editingFinished.connect(lambda:self.totalScrapValue(7))
        self.q8d2.editingFinished.connect(lambda:self.totalScrapValue(7))
        self.q8d3.editingFinished.connect(lambda:self.totalScrapValue(7))
        self.q8sold.editingFinished.connect(lambda:self.totalScrapSold(7))
        self.q9.editingFinished.connect(lambda:self.newQuota(8))
        self.q9d1.editingFinished.connect(lambda:self.totalScrapValue(8))
        self.q9d2.editingFinished.connect(lambda:self.totalScrapValue(8))
        self.q9d3.editingFinished.connect(lambda:self.totalScrapValue(8))
        self.q9sold.editingFinished.connect(lambda:self.totalScrapSold(8))
        self.q10.editingFinished.connect(lambda:self.newQuota(9))
        self.q10d1.editingFinished.connect(lambda:self.totalScrapValue(9))
        self.q10d2.editingFinished.connect(lambda:self.totalScrapValue(9))
        self.q10d3.editingFinished.connect(lambda:self.totalScrapValue(9))
        self.q10sold.editingFinished.connect(lambda:self.totalScrapSold(9))
        self.q11.editingFinished.connect(lambda:self.newQuota(10))
        self.q11d1.editingFinished.connect(lambda:self.totalScrapValue(10))
        self.q11d2.editingFinished.connect(lambda:self.totalScrapValue(10))
        self.q11d3.editingFinished.connect(lambda:self.totalScrapValue(10))
        self.q11sold.editingFinished.connect(lambda:self.totalScrapSold(10))
        self.q12.editingFinished.connect(lambda:self.newQuota(11))
        self.q12d1.editingFinished.connect(lambda:self.totalScrapValue(11))
        self.q12d2.editingFinished.connect(lambda:self.totalScrapValue(11))
        self.q12d3.editingFinished.connect(lambda:self.totalScrapValue(11))
        self.q12sold.editingFinished.connect(lambda:self.totalScrapSold(11))
        self.q13.editingFinished.connect(lambda:self.newQuota(12))
        self.q13d1.editingFinished.connect(lambda:self.totalScrapValue(12))
        self.q13d2.editingFinished.connect(lambda:self.totalScrapValue(12))
        self.q13d3.editingFinished.connect(lambda:self.totalScrapValue(12))
        self.q13sold.editingFinished.connect(lambda:self.totalScrapSold(12))
        self.q14.editingFinished.connect(lambda:self.newQuota(13))
        self.q14d1.editingFinished.connect(lambda:self.totalScrapValue(13))
        self.q14d2.editingFinished.connect(lambda:self.totalScrapValue(13))
        self.q14d3.editingFinished.connect(lambda:self.totalScrapValue(13))
        self.q14sold.editingFinished.connect(lambda:self.totalScrapSold(13))
        self.q15.editingFinished.connect(lambda:self.newQuota(14))
        self.q15d1.editingFinished.connect(lambda:self.totalScrapValue(14))
        self.q15d2.editingFinished.connect(lambda:self.totalScrapValue(14))
        self.q15d3.editingFinished.connect(lambda:self.totalScrapValue(14))
        self.q15sold.editingFinished.connect(lambda:self.totalScrapSold(14))
        self.q16.editingFinished.connect(lambda:self.newQuota(15))
        self.q16d1.editingFinished.connect(lambda:self.totalScrapValue(15))
        self.q16d2.editingFinished.connect(lambda:self.totalScrapValue(15))
        self.q16d3.editingFinished.connect(lambda:self.totalScrapValue(15))
        self.q16sold.editingFinished.connect(lambda:self.totalScrapSold(15))
        self.q17.editingFinished.connect(lambda:self.newQuota(16))
        self.q17d1.editingFinished.connect(lambda:self.totalScrapValue(16))
        self.q17d2.editingFinished.connect(lambda:self.totalScrapValue(16))
        self.q17d3.editingFinished.connect(lambda:self.totalScrapValue(16))
        self.q17sold.editingFinished.connect(lambda:self.totalScrapSold(16))
        self.q18.editingFinished.connect(lambda:self.newQuota(17))
        self.q18d1.editingFinished.connect(lambda:self.totalScrapValue(17))
        self.q18d2.editingFinished.connect(lambda:self.totalScrapValue(17))
        self.q18d3.editingFinished.connect(lambda:self.totalScrapValue(17))
        self.q18sold.editingFinished.connect(lambda:self.totalScrapSold(17))
        self.q19.editingFinished.connect(lambda:self.newQuota(18))
        self.q19d1.editingFinished.connect(lambda:self.totalScrapValue(18))
        self.q19d2.editingFinished.connect(lambda:self.totalScrapValue(18))
        self.q19d3.editingFinished.connect(lambda:self.totalScrapValue(18))
        self.q19sold.editingFinished.connect(lambda:self.totalScrapSold(18))
        self.q20.editingFinished.connect(lambda:self.newQuota(19))
        self.q20d1.editingFinished.connect(lambda:self.totalScrapValue(19))
        self.q20d2.editingFinished.connect(lambda:self.totalScrapValue(19))
        self.q20d3.editingFinished.connect(lambda:self.totalScrapValue(19))
        self.q20sold.editingFinished.connect(lambda:self.totalScrapSold(19))
        self.q21.editingFinished.connect(lambda:self.newQuota(20))
        self.q21d1.editingFinished.connect(lambda:self.totalScrapValue(20))
        self.q21d2.editingFinished.connect(lambda:self.totalScrapValue(20))
        self.q21d3.editingFinished.connect(lambda:self.totalScrapValue(20))
        self.q21sold.editingFinished.connect(lambda:self.totalScrapSold(20))
        self.q22.editingFinished.connect(lambda:self.newQuota(21))
        self.q22d1.editingFinished.connect(lambda:self.totalScrapValue(21))
        self.q22d2.editingFinished.connect(lambda:self.totalScrapValue(21))
        self.q22d3.editingFinished.connect(lambda:self.totalScrapValue(21))
        self.q22sold.editingFinished.connect(lambda:self.totalScrapSold(21))
        self.q23.editingFinished.connect(lambda:self.newQuota(22))
        self.q23d1.editingFinished.connect(lambda:self.totalScrapValue(22))
        self.q23d2.editingFinished.connect(lambda:self.totalScrapValue(22))
        self.q23d3.editingFinished.connect(lambda:self.totalScrapValue(22))
        self.q23sold.editingFinished.connect(lambda:self.totalScrapSold(22))
        self.q24.editingFinished.connect(lambda:self.newQuota(23))
        self.q24d1.editingFinished.connect(lambda:self.totalScrapValue(23))
        self.q24d2.editingFinished.connect(lambda:self.totalScrapValue(23))
        self.q24d3.editingFinished.connect(lambda:self.totalScrapValue(23))
        self.q24sold.editingFinished.connect(lambda:self.totalScrapSold(23))
        self.q25.editingFinished.connect(lambda:self.newQuota(24))
        self.q25d1.editingFinished.connect(lambda:self.totalScrapValue(24))
        self.q25d2.editingFinished.connect(lambda:self.totalScrapValue(24))
        self.q25d3.editingFinished.connect(lambda:self.totalScrapValue(24))
        self.q25sold.editingFinished.connect(lambda:self.totalScrapSold(24))
        self.pageUp.clicked.connect(self.pageUpFunction)
        self.pageDown.clicked.connect(self.pageDownFunction)
        self.resetButton.clicked.connect(self.resetAll)
        self.GoalValue.editingFinished.connect(self.updateStats)
        self.QuotaHighRadio.clicked.connect(self.highRadio)
        self.QuotaNumRadio.clicked.connect(self.numRadio)
        self.CreditsButton.clicked.connect(self.creditsFunction)
        self.CalculatorButton.clicked.connect(self.calculatorFunction)
        self.CalculatorShip.editingFinished.connect(self.overtimeCalculator)
        self.CalculatorDesired.editingFinished.connect(self.overtimeCalculator)
        self.CalculatorBuy.editingFinished.connect(self.overtimeCalculator)

    def overtimeCalculator(self):
        if self.CalculatorDesired.text() == "":
            tempDesired = 0
        else:
            tempDesired = int(self.CalculatorDesired.text())
        if self.CalculatorShip.text() == "":
            tempShip = 0
        else:
            tempShip = int(self.CalculatorShip.text())
        needed = math.ceil((int(self.CalculatorQuota.text())+5 * ((tempDesired-tempShip)+15))/6)
        temp = float((int(self.CalculatorBuy.text()))/100)
        temp = 2 - temp
        needed = math.ceil(needed * temp)
        self.CalculatorSell.setText(str(needed))

    def calculatorFunction(self):
        was = self.ButtonStackWidget.currentIndex()
        self.ButtonStackWidget.setCurrentIndex(0)
        if self.ButtonStackWidget.isHidden():
            self.ButtonStackWidget.show()
        else:
            if was == 0:
                self.ButtonStackWidget.hide()

    def creditsFunction(self):
        was = self.ButtonStackWidget.currentIndex()
        self.ButtonStackWidget.setCurrentIndex(1)
        if self.ButtonStackWidget.isHidden():
            self.ButtonStackWidget.show()
        else:
            if was == 1:
                self.ButtonStackWidget.hide()

    def highRadio(self):
        self.GoalValue.setStyleSheet("color: rgb(100, 32, 0); border: 1px solid red; border-color:hex(#ff5100);")
        self.label_23.setStyleSheet("color: rgb(100, 32, 0); border: none;")
        self.label_24.setStyleSheet("color: rgb(100, 32, 0); border: none;")
        self.stat5.setStyleSheet("color: rgb(100, 32, 0); border: none;")
        self.stat6.setStyleSheet("color: rgb(100, 32, 0); border: none;")
        self.GoalValue.setText("n/a")
        self.GoalValue.setReadOnly(True)

    def numRadio(self):
        self.GoalValue.setStyleSheet("color: rgb(255, 81, 0); border: 1px solid red; border-color:hex(#ff5100);")
        self.label_23.setStyleSheet("color: rgb(255, 81, 0); border: none;")
        self.label_24.setStyleSheet("color: rgb(255, 81, 0); border: none;")
        self.stat5.setStyleSheet("color: rgb(255, 81, 0); border: none;")
        self.stat6.setStyleSheet("color: rgb(255, 81, 0); border: none;")
        self.GoalValue.setText("10")
        self.GoalValue.setReadOnly(False)

    def pageUpFunction(self):
        self.QuotaWidget.setCurrentIndex(self.QuotaWidget.currentIndex()+1)

    def pageDownFunction(self):
        self.QuotaWidget.setCurrentIndex(self.QuotaWidget.currentIndex()-1)

    def resetAll(self):
        global totalScrap, totalSold, currShip, nextQuota, allQuotas, averageQuota
        self.QuotaWidget.setCurrentIndex(0)
        self.stat1.setText(str(0))
        self.stat2.setText(str(0))
        self.stat3.setText(str(0))
        self.stat4.setText(str(236.25))
        self.CalculatorQuota.setText("130")
        self.CalculatorDesired.setText("")
        self.CalculatorShip.setText("")
        self.CalculatorBuy.setText("100")
        self.CalculatorSell.setText("0")
        totalScrap = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        totalSold = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        currShip = 0
        nextQuota = [183.125, 236.25, 289.375]
        allQuotas = [130,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        averageQuota = [130,236.25,361.25,517.5,717.5,973.75,1298.75,1705,2205,2811.25,3536.25,4392.5,5392.5,6548.75,7873.75,9380,11080,12986.25,15111.25,17467.5,20067.5,22923.75]
        i=0
        while i < 25:
            if i != 0:
                getattr(self, f"q{i+1}").setText('')
            getattr(self, f"q{i+1}d1").setText('')
            getattr(self, f"q{i+1}d2").setText('')
            getattr(self, f"q{i+1}d3").setText('')
            getattr(self, f"q{i+1}sold").setText('')
            i=i+1
        self.last2Stats()

    def totalScrapValue(self, value):
        global currShip
        d1 = getattr(self, f"q{value+1}d1").text()
        if d1 != '':
            d1 = int(d1)
        d2 = getattr(self, f"q{value+1}d2").text()
        if d2 != '':
            d2 = int(d2)
        d3 = getattr(self, f"q{value+1}d3").text()
        if d3 != '':
            d3 = int(d3)
        totalScrap[value] = [d1, d2, d3]
        #print(totalScrap)
        self.currentShip()

    def newQuota(self, value):
        if getattr(self, f"q{value+1}").text() == '':
            allQuotas[value] = 0
        else:
            allQuotas[value] = int(getattr(self, f"q{value+1}").text())
        self.CalculatorQuota.setText(str(allQuotas[value]))
        nextQuotaCalc()
        self.updateStats()

    def totalScrapSold(self, value):
        global totalSold
        if getattr(self, f"q{value+1}sold").text() == '':
            sold = 0
        else:
            sold = getattr(self, f"q{value+1}sold").text()
        totalSold[value] = int(sold)
        self.currentShip()

    def updateStats(self):
        global currShip
        self.stat1.setText(str(currShip))
        if len(remove_items(flatten_comprehension(totalScrap),'')) != 0:
            self.stat2.setText(str(round(_sum(totalScrap)/int(len(remove_items(flatten_comprehension(totalScrap),''))),2)))
        temp1 = remove_items(allQuotas,'')
        temp = temp1[-1] - averageQuota[len(temp1)-1]
        if temp > 0:
            self.stat3.setText('+' + str(temp))
        else:
            self.stat3.setText(str(temp))
        self.stat4.setText(str(nextQuota[1]))

        self.last2Stats()

    def currentShip(self):
        global currShip, totalSold, totalScrap
        temp1 = _sum(totalScrap)
        temp2 = _sum(totalSold)
        currShip = temp1 - temp2
        self.updateStats()

    def last2Stats(self):
        if self.QuotaNumRadio.isChecked(): # for stat5 and stat6
            i=len(remove_items(allQuotas, ''))
            estimatedNeeded[0] = remove_items(allQuotas, '')[-1]
            estimatedNeeded[1] = estimatedNeeded[0]
            quotaNumber = int(self.GoalValue.text())
            while i <= quotaNumber:
                estimatedNeeded[0] = estimatedNeeded[0] + 100 * (1 + ((i**2)/16))
                estimatedNeeded[1] = estimatedNeeded[1] + estimatedNeeded[0]
                i = i+1
            estimatedNeeded[1] = estimatedNeeded[1] - currShip
            days = (quotaNumber * 3) - len(remove_items(flatten_comprehension(totalScrap),''))
            if days != 0:
                estimatedNeeded[2] = estimatedNeeded[1] / days
                self.stat6.setText(str(estimatedNeeded[0]))
            self.stat5.setText(str(estimatedNeeded[2]))

def nextQuotaCalc():
    global nextQuota, currQuota
    temp1 = remove_items(allQuotas,'')
    temp = temp1[-1]
    nextQuota[1] = temp + 100 * (1 + ((int(len(temp1))**2)/16))
    nextQuota[0] = nextQuota[1] * 0.5
    nextQuota[2] = nextQuota[1] * 1.5
    return

def _sum(arr): # this adds all the values in an array together
    sum = 0
    for i in arr:
        if type(i).__name__ == 'list':
            for j in i:
                if j == '':
                    continue
                sum = sum + j
        else:
            if i == '':
                continue
            sum = sum + i
    return(sum)

def flatten_comprehension(matrix):
    return [item for row in matrix for item in row]

def remove_items(list, item):
    res = [i for i in list if i != item] 
    return res 


totalScrap = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
totalSold = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
currShip = 0
nextQuota = [183.125, 236.25, 289.375]
estimatedNeeded = [2811.25, 10956.25, 365.20] # Final, Sum, Average
allQuotas = [130,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
averageQuota = [130,236.25,361.25,517.5,717.5,973.75,1298.75,1705,2205,2811.25,3536.25,4392.5,5392.5,6548.75,7873.75,9380,11080,12986.25,15111.25,17467.5,20067.5,22923.75]

app=QApplication(sys.argv)
app.setApplicationName("LethalTracker v1.0")
app.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(os.path.join(resource_path, 'icon.ico'))))
mainwindow=Window()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(700)
widget.setFixedHeight(300)
widget.show()
app.exec_()