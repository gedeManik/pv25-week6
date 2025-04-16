import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QColor


class MyForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui", self)  

        self.labelDisplay = self.findChild(QtWidgets.QLabel, "labelDisplay")
        self.sliderFontSize = self.findChild(QtWidgets.QSlider, "horizontalSlider")
        self.sliderBackground = self.findChild(QtWidgets.QSlider, "horizontalSlider_3")
        self.sliderFontColor = self.findChild(QtWidgets.QSlider, "horizontalSlider_2")

        self.sliderFontSize.setRange(20, 60)
        self.sliderFontSize.setValue(40)
        self.sliderBackground.setRange(0, 255)
        self.sliderBackground.setValue(255)
        self.sliderFontColor.setRange(0, 255)
        self.sliderFontColor.setValue(0)

        self.sliderFontSize.valueChanged.connect(self.updateDisplay)
        self.sliderBackground.valueChanged.connect(self.updateDisplay)
        self.sliderFontColor.valueChanged.connect(self.updateDisplay)

        self.updateDisplay()

    def updateDisplay(self):
        font_size = self.sliderFontSize.value()
        bg_value = self.sliderBackground.value()
        font_value = self.sliderFontColor.value()

        bg_color = QColor(bg_value, bg_value, bg_value)
        font_color = QColor(font_value, font_value, font_value)

        style = f"background-color: {bg_color.name()}; color: {font_color.name()}; font-size: {font_size}pt;"
        self.labelDisplay.setStyleSheet(style)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec_())
