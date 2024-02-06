import sys
import os
import math
from collections import defaultdict

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QColorDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFontDatabase, QIntValidator


resource_path = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))


class QuotaPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        loadUi(os.path.join(resource_path, "layouts/QuotaPage.ui"), self)


class OBSWindow(QMainWindow):
    def __init__(self, parent=None):
        super(OBSWindow, self).__init__(parent)

        self.setFixedHeight(320)
        self.setFixedWidth(650)

        loadUi(os.path.join(resource_path, "layouts/OBSWindow.ui"), self)
        self.setWindowTitle("LethalTracker OBS")
        self.FontButton.clicked.connect(self.fontColor)
        self.BackgroundButton.clicked.connect(self.backColor)

    def backColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.widget.setStyleSheet(f"background-color: {color.name()};")

    def fontColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ShipScrapInput.setStyleSheet(f"color: {color.name()}; border: none;")
            self.AverageScrapPerDayInput.setStyleSheet(
                f"color: {color.name()}; border: none;"
            )
            self.QuotaDeviationAverageInput.setStyleSheet(
                f"color: {color.name()}; border: none;"
            )
            self.EstimatedNextQuotaInput.setStyleSheet(
                f"color: {color.name()}; border: none;"
            )
            self.EstimatedScrapPerDayNeededInput.setStyleSheet(
                f"color: {color.name()}; border: none;"
            )
            self.EstimatedFinalQuotaInput.setStyleSheet(
                f"color: {color.name()}; border: none;"
            )
            self.stat7.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_2.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_3.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_4.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_5.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_6.setStyleSheet(f"color: {color.name()}; border: none;")
            self.label_7.setStyleSheet(f"color: {color.name()}; border: none;")
            self.BackgroundButton.setStyleSheet(
                f"color: {color.name()}; border: 1px solid red; border-color: {color.name()};"
            )
            self.FontButton.setStyleSheet(
                f"color: {color.name()}; border: 1px solid red; border-color: {color.name()};"
            )


class Window(QMainWindow):
    @property
    def quota_deviation(self):
        return self._quota_deviation

    @quota_deviation.setter
    def quota_deviation(self, value):
        value = round(value, 3)
        self._quota_deviation = value
        self.QuotaDeviationAverageInput.setText(f"{'+' if value>0 else ''} {value}")
        if self.obs_window:
            self.obs_window.QuotaDeviationAverage.setText(
                f"{'+' if value>0 else ''} {value}"
            )

    @property
    def estimated_next_quota(self):
        return self._estimated_next_quota

    @estimated_next_quota.setter
    def estimated_next_quota(self, value):
        value = round(value, 3)
        self._estimated_next_quota = value
        self.EstimatedNextQuotaInput.setText(str(value))
        if self.obs_window:
            self.obs_window.EstimatedNextQuota.setText(str(value))

    @property
    def estimated_final_quota(self):
        return self._estimated_final_quota

    @estimated_final_quota.setter
    def estimated_final_quota(self, value):
        value = round(value, 3)
        self._estimated_final_quota = value
        self.EstimatedFinalQuotaInput.setText(str(value))
        if self.obs_window:
            self.obs_window.EstimatedFinalQuota.setText(str(value))

    @property
    def estimated_scrap_per_day(self):
        return self._estimated_scrap_per_day

    @estimated_scrap_per_day.setter
    def estimated_scrap_per_day(self, value):
        value = round(value, 3)
        self._estimated_scrap_per_day = value
        self.EstimatedScrapPerDayNeededInput.setText(str(value))
        if self.obs_window:
            self.obs_window.EstimatedScrapPerDayNeeded.setText(str(value))

    @property
    def calculator_current_quota(self):
        return self._calculator_current_quota

    @calculator_current_quota.setter
    def calculator_current_quota(self, value):
        self._calculator_current_quota = value
        self.CalculatorQuota.setText(str(value))
        if self.obs_window:
            self.obs_window.CurrentQuota.setText(
                f"Quota {self.getCurrentQuotaNo()}: {value}"
            )

    @property
    def scrap_on_ship(self):
        return self._scrap_on_ship

    @scrap_on_ship.setter
    def scrap_on_ship(self, value):
        self._scrap_on_ship = value
        self.ShipScrapInput.setText(str(value))
        if self.obs_window:
            self.obs_window.ShipScrap.setText(str(value))

    @property
    def average_scrap_per_day(self):
        return self._average_scrap_per_day

    @average_scrap_per_day.setter
    def average_scrap_per_day(self, value):
        value = round(value, 3)
        self._average_scrap_per_day = value
        self.AverageScrapPerDayInput.setText(str(value))
        if self.obs_window:
            self.obs_window.AverageScrapPerDay.setText(str(value))

    def __init__(self):
        super().__init__()

        QFontDatabase.addApplicationFont(
            os.path.join(resource_path, "3270-Regular.otf")
        )
        loadUi(os.path.join(resource_path, "layouts/MainWindow.ui"), self)

        # Data
        self.quotaData = defaultdict(lambda: {"quota": 130, "sold": 0, "days": {}})
        self.quotaData[1]["quota"] = 130
        self.averageQuota = [
            130,
            236.25,
            361.25,
            517.5,
            717.5,
            973.75,
            1298.75,
            1705,
            2205,
            2811.25,
            3536.25,
            4392.5,
            5392.5,
            6548.75,
            7873.75,
            9380,
            11080,
            12986.25,
            15111.25,
            17467.5,
            20067.5,
            22923.75,
        ]

        self.obs_window = None

        # Properties
        self._quota_deviation = 0
        self._average_scrap_per_day = 0
        self._calculator_current_quota = 0
        self._estimated_final_quota = 0
        self._estimated_next_quota = 0
        self._estimated_scrap_per_day = 0
        self._scrap_on_ship = 0

        # Set validation for line inputs
        for child_widget in self.findChildren(QtWidgets.QWidget):
            if isinstance(child_widget, QtWidgets.QLineEdit):
                child_widget.setValidator(QIntValidator())

        # Set connections for quota pages
        for quota_no in range(1, 26):
            if quota_no != 1:
                if quota_amount_input := self.findChild(QLineEdit, f"q{quota_no}"):
                    quota_amount_input.textEdited.connect(
                        lambda amount, quota_no=quota_no: self.setQuotaAmount(
                            quota_no, amount
                        )
                    )
            for day in range(1, 4):
                if scrap_value_input := self.findChild(QLineEdit, f"q{quota_no}d{day}"):
                    scrap_value_input.textEdited.connect(
                        lambda scrap_value, day=day, quota_no=quota_no: self.setScrapValue(
                            quota_no, day, scrap_value
                        )
                    )

            if scrap_sold_input := self.findChild(QLineEdit, f"q{quota_no}sold"):
                scrap_sold_input.textEdited.connect(
                    lambda scrap_value, quota_no=quota_no: self.setScrapSold(
                        quota_no, scrap_value
                    )
                )
        # Set connection for everything else
        self.OBSButton.setIcon(QtGui.QIcon(os.path.join(resource_path, "obs.png")))
        self.OBSButton.clicked.connect(self.openOBSWindow)

        self.resetButton.clicked.connect(self.resetWindowFunct)
        self.ResetDialogWindow.hide()
        self.ResetDialogWindowCancelButton.clicked.connect(self.resetCancel)
        self.ResetDialogWindowConfirmButton.clicked.connect(self.resetAll)

        self.pageUp.clicked.connect(self.pageUpFunction)
        self.pageDown.clicked.connect(self.pageDownFunction)
        self.GoalValue.editingFinished.connect(self.updateQuotaFields)  # done
        self.QuotaHighRadio.clicked.connect(self.highRadio)
        self.QuotaNumRadio.clicked.connect(self.numRadio)
        self.CreditsButton.clicked.connect(self.creditsFunction)
        self.CalculatorButton.clicked.connect(self.calculatorFunction)
        self.CalculatorShip.editingFinished.connect(self.overtimeCalculator)
        self.CalculatorDesired.editingFinished.connect(self.overtimeCalculator)
        self.CalculatorBuy.editingFinished.connect(self.overtimeCalculator)
        self.NO_OT.clicked.connect(self.notOvertime)
        self.OT.clicked.connect(self.Overtime)

    @staticmethod
    def approximateNextQuotaAmount(quotas_completed, last_quota_amount):
        return last_quota_amount + 100 * (1 + ((quotas_completed**2) / 16))

    def getCurrentQuotaNo(self):
        return max(self.quotaData.keys())

    def getDaysLeft(self):
        # Return days left in current quota
        current_quota_no = self.getCurrentQuotaNo()
        keys = self.quotaData[current_quota_no]["days"].keys()
        return 3 - max(keys) if keys else 3

    def getDaysPassed(self):
        current_quota_no = self.getCurrentQuotaNo()
        return 3 * (current_quota_no - 1) + (3 - self.getDaysLeft())

    def getDaysLeftTotal(self):
        quota_goal = int(self.GoalValue.text())  # FIXME: Decouple
        current_quota_no = self.getCurrentQuotaNo()
        return (quota_goal - current_quota_no) * 3 + self.getDaysLeft()

    def getTotalScrap(self):
        total = 0
        for _, v in self.quotaData.items():
            # print(total, v["days"].values())
            total += sum(v["days"].values())
        return total

    def getTotalSold(self):
        total = 0
        for _, v in self.quotaData.items():
            total += v["sold"]
        return total

    def getQuotaAmount(self, quota_no):
        quota_dict = self.quotaData.get(quota_no)
        if not quota_dict:
            return None
        return quota_dict["quota"]

    def setQuotaAmount(self, quota_no, amount):
        self.quotaData[quota_no]["quota"] = int(amount) if amount.isnumeric() else 0
        print(self.quotaData.items())
        self.updateQuotaFields()

    def getScrapValue(self, quota_no, day):
        quota_dict = self.quotaData.get(quota_no)
        if not quota_dict:
            return None
        return quota_dict["days"].get(day)

    def setScrapValue(self, quota_no, day, scrap_value):
        self.quotaData[quota_no]["days"][day] = (
            int(scrap_value) if scrap_value.isnumeric() else 0
        )
        self.updateScrapFields()

    def getScrapSold(self, quota_no):
        quota_dict = self.quotaData.get(quota_no)
        if not quota_dict:
            return None
        return quota_dict["sold"]

    def setScrapSold(self, quota_no, scrap_value):
        self.quotaData[quota_no]["sold"] = (
            int(scrap_value) if scrap_value.isnumeric() else 0
        )
        self.updateScrapFields()

    def updateQuotaFields(self):
        self.updateQuotaDeviation()
        self.updateNextQuotaPrediction()
        self.updateScrapPerDayPredictionAndFinalQuota()

        # This is separate to remind that calculator quta need better input
        # TODO:
        self.calculator_current_quota = self.getQuotaAmount(self.getCurrentQuotaNo())

    def updateQuotaDeviation(self):
        current_quota_no = self.getCurrentQuotaNo()
        self.quota_deviation = (
            self.averageQuota[current_quota_no - 1]
            - self.quotaData[current_quota_no]["quota"]
        )
        print(self.quota_deviation)

    def updateNextQuotaPrediction(self):
        current_quota_no = self.getCurrentQuotaNo()
        current_quota_amount = self.quotaData[current_quota_no]["quota"]

        self.estimated_next_quota = self.approximateNextQuotaAmount(
            current_quota_no, current_quota_amount
        )

    def updateScrapPerDayPredictionAndFinalQuota(self):
        current_quota_no = self.getCurrentQuotaNo()
        current_quota_amount = self.quotaData[current_quota_no]["quota"]
        if self.QuotaNumRadio.isChecked():
            quota_goal = int(self.GoalValue.text())
            total_scrap_needed = current_quota_amount
            estimated_final_quota = current_quota_amount
            i = current_quota_no
            while i <= quota_goal:
                estimated_final_quota = self.approximateNextQuotaAmount(
                    i, estimated_final_quota
                )
                total_scrap_needed += estimated_final_quota
                i += 1
            self.estimated_scrap_per_day = total_scrap_needed / self.getDaysLeftTotal()
            self.estimated_final_quota = estimated_final_quota
        if self.QuotaHighRadio.isChecked():
            days_left = self.getDaysLeft()
            self.estimated_scrap_per_day = (
                (current_quota_amount / days_left) if days_left != 0 else 0
            )

    def updateScrapFields(self):
        self.updateScrapOnShip()
        self.updateAverageScrapPerDay()

    def updateScrapOnShip(self):
        self.scrap_on_ship = self.getTotalScrap() - self.getTotalSold()

    def updateAverageScrapPerDay(self):
        self.average_scrap_per_day = self.getTotalScrap() / self.getDaysPassed()

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
        if self.obs_window is None:
            self.obs_window = OBSWindow(self)
            self.obs_window.show()
        else:
            if self.obs_window.isHidden():
                self.obs_window.show()

    def resetWindowFunct(self):
        self.ResetDialogWindow.show()

    def resetCancel(self):
        self.ResetDialogWindow.hide()

    def overtimeCalculator(self):
        if self.OT.isChecked():
            if self.CalculatorDesired.text() == "":
                tempDesired = 0
            else:
                tempDesired = int(self.CalculatorDesired.text())
            if self.CalculatorShip.text() == "":
                tempShip = 0
            else:
                tempShip = int(self.CalculatorShip.text())
            needed = math.floor(
                (int(self.CalculatorQuota.text()) + 5 * ((tempDesired - tempShip) + 15))
                / 6
            )
            temp = float((int(self.CalculatorBuy.text())) / 100)
            temp = 2 - temp
            needed = math.floor(needed * temp)
            self.CalculatorSell.setText(str(needed))
        if self.NO_OT.isChecked():
            needed = math.floor(
                int(self.CalculatorQuota.text())
                / (int(self.CalculatorBuy.text()) / 100)
            )
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
        self.GoalValue.setStyleSheet(
            "color: rgb(100, 32, 0); border: 1px solid red; border-color:hex(#ff5100);"
        )
        self.label_23.setStyleSheet("color: rgb(100, 32, 0); border: none;")
        self.label_24.setStyleSheet("color: rgb(100, 32, 0); border: none;")
        self.EstimatedScrapPerDayNeededInput.setStyleSheet(
            "color: rgb(100, 32, 0); border: none;"
        )
        self.EstimatedFinalQuotaInput.setStyleSheet(
            "color: rgb(100, 32, 0); border: none;"
        )
        self.GoalValue.setText("n/a")
        self.GoalValue.setReadOnly(True)

    def numRadio(self):
        self.GoalValue.setStyleSheet(
            "color: rgb(255, 81, 0); border: 1px solid red; border-color:hex(#ff5100);"
        )
        self.label_23.setStyleSheet("color: rgb(255, 81, 0); border: none;")
        self.label_24.setStyleSheet("color: rgb(255, 81, 0); border: none;")
        self.EstimatedScrapPerDayNeededInput.setStyleSheet(
            "color: rgb(255, 81, 0); border: none;"
        )
        self.EstimatedFinalQuotaInput.setStyleSheet(
            "color: rgb(255, 81, 0); border: none;"
        )
        self.GoalValue.setText("10")
        self.GoalValue.setReadOnly(False)

    def pageUpFunction(self):
        self.QuotaWidget.setCurrentIndex(self.QuotaWidget.currentIndex() + 1)

    def pageDownFunction(self):
        self.QuotaWidget.setCurrentIndex(self.QuotaWidget.currentIndex() - 1)

    def resetAll(self):
        self.QuotaWidget.setCurrentIndex(0)
        self.scrap_on_ship = 0
        self.average_scrap_per_day = 0
        self.quota_deviation = 0
        self.estimated_next_quota = 0
        self.calculator_current_quota = 130
        if self.OT.isChecked():
            self.CalculatorDesired.setText("")
            self.CalculatorShip.setText("")
            self.CalculatorBuy.setText("100")
            self.CalculatorSell.setText("0")
        if self.NO_OT.isChecked():
            self.overtimeCalculator()
        i = 0
        self.quotaData = defaultdict(lambda: {"quota": 130, "sold": 0, "days": {}})
        self.quotaData[1]["quota"] = 130
        self.updateQuotaFields()
        self.updateQuotaFields()
        while i < 25:
            if i != 0:
                getattr(self, f"q{i+1}").setText("")
            for day in range(1, 4):
                getattr(self, f"q{i+1}d{day}").setText("")
            getattr(self, f"q{i+1}sold").setText("")
            i += 1
        self.ResetDialogWindow.hide()


app = QApplication(sys.argv)
app.setApplicationName("LethalTracker v1.3")
app.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(os.path.join(resource_path, "icon.ico"))))
mainwindow = Window()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(700)
widget.setFixedHeight(300)
widget.show()
app.exec_()
