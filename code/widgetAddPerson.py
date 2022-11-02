from PIL import Image
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap

from person_info_window import Ui_Form
from func import f_addPersontodb


class PersonInfoAdd(QWidget, Ui_Form):
    def __init__(self, theme):
        super().__init__()
        self.theme = theme
        self.setupUi(self)
        self.initUI()
        self.changeColor()

    def initUI(self):
        self.btn_addPhoto.clicked.connect(self.photo)
        self.bth_addPerson_done.clicked.connect(self.done)

        self.fname = None

    def photo(self):
        self.fname = QFileDialog.getOpenFileName(self, '', '')[0]

        img = Image.open(self.fname)
        fixed_height = 150
        percent = fixed_height / float(img.size[0])
        width_size = int((float(img.size[1]) * float(percent)))
        img = img.resize((fixed_height, width_size))
        img.save('../photo/result.jpeg')

        self.pixmap = QPixmap('../photo/result.jpeg')
        self.lbl_photo.setPixmap(self.pixmap)

    def done(self):
        name = self.lineEdit_name.text()
        surname = self.lineEdit_surname.text()
        age = self.spinBoxAge.value()
        year = self.calendarWidget.selectedDate()
        year = year.toString('yyyy-MM-dd')
        info = self.plainTextEditInfo.toPlainText()
        path_photo = self.fname

        img = Image.open(path_photo)
        img.save(f"people/{name}_{surname}")

        f_addPersontodb(name, surname, age, year, info, path_photo)
        self.close()

    def changeColor(self):
        if self.theme == 'dark':
            self.setDarkTheme()
        elif self.theme == 'light':
            self.setLightTheme()

    def setLightTheme(self):
        self.setStyleSheet('background-color: #f4f5f6')
        self.plainTextEditInfo.setStyleSheet('color: #0b1016; background-color: #cacfd5')
        self.btn_addPhoto.setStyleSheet('color: #0b1016; background-color: #cacfd5')
        self.bth_addPerson_done.setStyleSheet('color: #0b1016; background-color: #cacfd5')
        self.lineEdit_name.setStyleSheet('color: #0b1016; background-color: #cacfd5')
        self.lineEdit_surname.setStyleSheet('color: #0b1016; background-color: #cacfd5')
        self.spinBoxAge.setStyleSheet('color: #0b1016; background-color: #cacfd5')
        self.lbl_name.setStyleSheet('color: #0b1016')
        self.lbl_surname.setStyleSheet('color: #0b1016')
        self.lbl_age.setStyleSheet('color: #0b1016')
        self.lbl_year.setStyleSheet('color: #0b1016')
        self.lbl_info.setStyleSheet('color: #0b1016')

    def setDarkTheme(self):
        self.setStyleSheet('background-color: #38444c')
        self.plainTextEditInfo.setStyleSheet('color: #f0f2f3; background-color: #697278')
        self.btn_addPhoto.setStyleSheet('color: #f0f2f3; background-color: #697278')
        self.bth_addPerson_done.setStyleSheet('color: #f0f2f3; background-color: #697278')
        self.lineEdit_name.setStyleSheet('color: #f0f2f3; background-color: #697278')
        self.lineEdit_surname.setStyleSheet('color: #f0f2f3; background-color: #697278')
        self.spinBoxAge.setStyleSheet('color: #f0f2f3; background-color: #697278')
        self.lbl_name.setStyleSheet('color: #f0f2f3')
        self.lbl_surname.setStyleSheet('color: #f0f2f3')
        self.lbl_age.setStyleSheet('color: #f0f2f3')
        self.lbl_year.setStyleSheet('color: #f0f2f3')
        self.lbl_info.setStyleSheet('color: #f0f2f3')
