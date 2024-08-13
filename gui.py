from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QWidget, QLabel, QVBoxLayout
from pathlib import Path
import sys, json
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(259, 257)
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.clicked.connect(self.anno)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda: self.button_1())
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName("plainTextEdit")
        with open('conf.json') as outfile:
            data = json.load(outfile)
        moveFrom = data["moveFrom"]
        moveTo = data["moveTo"]
        for i in range(len(moveFrom)):
            self.plainTextEdit.insertPlainText(moveFrom[i] + "\n")
        self.verticalLayout.addWidget(self.plainTextEdit)
        spacerItem1 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.button_2())
        self.verticalLayout.addWidget(self.pushButton_2)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(moveTo)
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        spacerItem4 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        spacerItem3 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.save_data())
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem5 = QtWidgets.QSpacerItem(17, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Настройки"))
        self.label.setText(_translate("MainWindow", "           Укажите путь к исходникам"))
        self.pushButton_4.setText(_translate("MainWindow", "?"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label_2.setText(_translate("MainWindow", "Укажите путь к хранилищу"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить"))

    def button_2(self):
        dir_name = QFileDialog.getExistingDirectory(None, "Выберите папку")
        if dir_name:
            path = Path(dir_name)
            self.lineEdit.setText(str(path))
    def button_1(self):
        dir_name = QFileDialog.getExistingDirectory(None, "Выберите папку")
        if dir_name:
            path = Path(dir_name)
            self.plainTextEdit.insertPlainText(str(path) + '\n')
    def save_data(self):
        mf = [x for x in self.plainTextEdit.toPlainText().split("\n") if x != '']
        mt = self.lineEdit.text()
        with open('conf.json') as outfile:
            data = json.load(outfile)
        if mt:
            data['moveTo'] = mt
        if mf:
            data['moveFrom'] = mf
        with open('conf.json', 'w') as outfile2:
            json.dump(data, outfile2, indent=2, ensure_ascii=False)
        app.quit()

    def anno(self):
        self.w = AnotherWindow()
        self.w.show()
class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 365)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Аннотация"))
            self.plainTextEdit.setPlainText(_translate("Form", "                                                                Аннотация\n"
                                                               "\n"
                                                               "1. Добавление нескольких папок для плановой очистки дискового пространства.\n"
                                                               "\n"
                                                               "2. Очистка исходных папок производится по принципу - бэкап файлов любого типа ежедневно в заданное время, затем удаление файлов старше 15 дней, при нехватке места на используемом диске.\n"
                                                               "\n"
                                                               "3. Очистка хранилища производится по принципу - удаление файлов любого типа старше 15 дней, если на задействуемом диске < 20 гб. свободного места.\n"
                                                               "\n"
                                                               "4. Программа, после каждой иттерации очистки заносит результат в лог файл - logs.log. \n"
                                                               "\n"
                                                               "4.1. В случае критических ошибок - посылается письмо на почту IT отдела - it@titan-group.ru \n"
                                                               "\n"
                                                               "5. Конфигурация позволяет выбрать папки, откуда необходимо производить очищение (количество влияет на быстродействие), выбирать конечную папку хранилища.\n"
                                                               "\n"
                                                               "!Важно. Первый путь в исходниках - путь к папке с видеозаписями с камер .\n"
                                                               "\n"
                                                            
                                                               ""))
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dl = MainWindow()
    sys.exit(app.exec_())
