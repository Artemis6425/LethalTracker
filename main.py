import math
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QColorDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFontDatabase, QIntValidator
import sys
import os

resource_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))

class SecondWindow(QMainWindow):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        
        self.setFixedHeight(320)
        self.setFixedWidth(650)

        loadUi(os.path.join(resource_path, 'Popout.ui'), self)
        self.setWindowTitle("LethalTracker OBS")
        self.FontButton.clicked.connect(self.fontColor)
        self.BackgroundButton.clicked.connect(self.backColor)
        parent.stat1.textChanged.connect(lambda: self.changeStat(self.stat2, parent.stat1))
        parent.stat2.textChanged.connect(lambda: self.changeStat(self.stat3, parent.stat2))
        parent.stat3.textChanged.connect(lambda: self.changeStat(self.stat4, parent.stat3))
        parent.stat4.textChanged.connect(lambda: self.changeStat2(parent.stat4))
        parent.stat4.textChanged.connect(lambda: self.changeStat(self.stat5, parent.stat4))
        parent.stat5.textChanged.connect(lambda: self.changeStat(self.stat6, parent.stat5))
        parent.stat6.textChanged.connect(lambda: self.changeStat(self.stat7, parent.stat6))

    def changeStat2(self, stat4):
        if stat4.text() == "236.25": # effectively part of the Reset function
            self.stat1.setText("Quota 1: 130")
            return
        temp1 = remove_items(allQuotas,'')
        temp2 = len(temp1)
        self.stat1.setText(f"Quota {temp2}: {temp1[-1]}")

    def changeStat(self, item, parentt):
        item.setText(parentt.text())

    def backColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.widget.setStyleSheet(f"background-color: {color.name()};")

    def fontColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.stat1.setStyleSheet(f"color: {color.name()}; border: none;")
            self.stat2.setStyleSheet(f"color: {color.name()}; border: none;")
            self.stat3.setStyleSheet(f"color: {color.name()}; border: none;")
            self.stat4.setStyleSheet(f"color: {color.name()}; border: none;")
            self.stat5.setStyleSheet(f"color: {color.name()}; border: none;")
            self.stat6.setStyleSheet(f"color: {color.name()}; border: none;")
            self.stat7.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_2.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_3.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_4.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_5.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_6.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_7.setStyleSheet(f"color: {color.name()}; border: none;")
            self.BackgroundButton.setStyleSheet(f"color: {color.name()}; border: 1px solid red; border-color: {color.name()};")
            self.FontButton.setStyleSheet(f"color: {color.name()}; border: 1px solid red; border-color: {color.name()};")

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        QFontDatabase.addApplicationFont(os.path.join(resource_path, '3270-Regular.otf'))
        loadUi(os.path.join(resource_path, 'MainWindow.ui'), self)

        for child_widget in self.findChildren(QtWidgets.QWidget):
            if isinstance(child_widget, QtWidgets.QLineEdit):
                child_widget.setValidator(QIntValidator())

        for i in range (1,26):
            
            if i != 1:
                temp1 = self.findChild(QLineEdit, f"q{i}")
                if temp1:
                    temp1.editingFinished.connect(lambda temp=i-1: self.newQuota(temp))
            temp2 = self.findChild(QLineEdit, f"q{i}d1")
            if temp2:
                temp2.editingFinished.connect(lambda temp=i-1: self.totalScrapValue(temp))
            temp3 = self.findChild(QLineEdit, f"q{i}d2")
            if temp3:
                temp3.editingFinished.connect(lambda temp=i-1: self.totalScrapValue(temp))
            temp4 = self.findChild(QLineEdit, f"q{i}d3")
            if temp4:
                temp4.editingFinished.connect(lambda temp=i-1: self.totalScrapValue(temp))
            temp5 = self.findChild(QLineEdit, f"q{i}sold")
            if temp5:
                temp5.editingFinished.connect(lambda temp=i-1: self.totalScrapSold(temp))
        self.OBSButton.setIcon(QtGui.QIcon(os.path.join(resource_path, 'obs.png')))
        self.OBSButton.clicked.connect(self.openOBSWindow)
        self.ResetWindow.hide()
        self.ResetCancel.clicked.connect(self.resetCancel)
        self.ResetConfirmation.clicked.connect(self.resetAll)
        self.pageUp.clicked.connect(self.pageUpFunction)
        self.pageDown.clicked.connect(self.pageDownFunction)
        self.resetButton.clicked.connect(self.resetWindowFunct)
        self.GoalValue.editingFinished.connect(self.updateStats)
        self.QuotaHighRadio.clicked.connect(self.highRadio)
        self.QuotaNumRadio.clicked.connect(self.numRadio)
        self.CreditsButton.clicked.connect(self.creditsFunction)
        self.CalculatorButton.clicked.connect(self.calculatorFunction)
        self.CalculatorShip.editingFinished.connect(self.overtimeCalculator)
        self.CalculatorDesired.editingFinished.connect(self.overtimeCalculator)
        self.CalculatorBuy.editingFinished.connect(self.overtimeCalculator)
        self.NO_OT.clicked.connect(self.notOvertime)
        self.OT.clicked.connect(self.Overtime)

    def Overtime(self):
        self.CalculatorShip.setStyleSheet("color: rgb(253, 85, 0); border: none;")
        self.label_171.setStyleSheet("color: rgb(253, 85, 0); border: none;")
        self.label_173.setStyleSheet("color: rgb(253, 85, 0); border: none;")
        self.CalculatorDesired.setStyleSheet("color: rgb(253, 85, 0); border: none;")
        self.CalculatorShip.setEnabled(True)
        self.CalculatorDesired.setEnabled(True)
        self.CalculatorShip.setText("")
        self.CalculatorDesired.setText("")
        self.CalculatorSell.setText("0")

    def notOvertime(self):
        self.CalculatorShip.setStyleSheet("color: rgb(100, 32, 0); border: none;")
        self.label_171.setStyleSheet("color: rgb(100, 32, 0); border: none;")
        self.label_173.setStyleSheet("color: rgb(100, 32, 0); border: none;")
        self.CalculatorDesired.setStyleSheet("color: rgb(100, 32, 0); border: none;")
        self.CalculatorShip.setEnabled(False)
        self.CalculatorDesired.setEnabled(False)
        self.CalculatorShip.setText("n/a")
        self.CalculatorDesired.setText("n/a")
        self.overtimeCalculator()

    def openOBSWindow(self):
        try:
            self.second_window
        except AttributeError:
            self.second_window = None

        if self.second_window is None:
            self.second_window = SecondWindow(self)
            self.second_window.show()
        else:
            if self.second_window.isHidden():
                self.second_window.show()

    def resetWindowFunct(self):
        self.ResetWindow.show()

    def resetCancel(self):
        self.ResetWindow.hide()

    def overtimeCalculator(self):
        if self.OT.isChecked():
            deadlineCalc = {
                "0": [-15, 100],
                "1": [0, 76.6666],
                "2": [15, 53.3333],
                "3":[30, 30]
            }
            cb = int(self.CalculatorBuy.text())
            if cb > 3: cb = 3
            cBuy = deadlineCalc[str(cb)]

            if self.CalculatorDesired.text() == "":
                tempDesired = 0
            else:
                tempDesired = int(self.CalculatorDesired.text())
            if self.CalculatorShip.text() == "":
                tempShip = 0
            else:
                tempShip = int(self.CalculatorShip.text())
            if self.CalculatorQuota.text() == "":
                tempQuota = 0
            else:
                tempQuota = int(self.CalculatorQuota.text())
            
            needed = tempQuota

            needed += math.ceil((tempDesired - tempShip - tempQuota - cBuy[0])*(5/6))
            if needed > tempDesired:
                needed = tempDesired
            needed = math.ceil(needed * (100/cBuy[1]))


            self.CalculatorSell.setText(str(needed))
        if self.NO_OT.isChecked():
            needed = math.floor(int(self.CalculatorQuota.text()) / (int(self.CalculatorBuy.text())/100))
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
        if self.OT.isChecked():
            self.CalculatorDesired.setText("")
            self.CalculatorShip.setText("")
            self.CalculatorBuy.setText("100")
            self.CalculatorSell.setText("0")
        if self.NO_OT.isChecked():
            self.overtimeCalculator()
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
        self.ResetWindow.hide()

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
        if self.QuotaHighRadio.isChecked():
            i=len(remove_items(allQuotas, ''))
            lastQuota = remove_items(allQuotas, '')[-1] # last quota
            days = 3* i - len(remove_items(flatten_comprehension(totalScrap), '')) # days left
            if days != 0:
                j = (lastQuota - currShip) / days
            else:
                j = lastQuota - currShip
            self.stat5.setText(str(max(0, j)))
            

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
averageQuota = [130, 364.21, 237.61, 522.46, 725.03, 984.56, 1313.72, 1725.18, 2231.58, 2845.60, 3579.89, 4447.11, 5459.92, 6630.99, 7972.96, 9498.51, 11220.29, 13150.96, 15303.19, 17689.62, 20322.94, 23215.78, 26380.82, 29830.71]

app=QApplication(sys.argv)
app.setApplicationName("LethalTracker v1.32")
app.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(os.path.join(resource_path, 'icon.ico'))))
mainwindow=Window()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(700)
widget.setFixedHeight(300)
widget.show()
app.exec_()
