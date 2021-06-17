# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AutoCalv1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# todo fix whats above this
# todo fix imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QVBoxLayout, QLabel, QDesktopWidget
import sys
import config
import database
import main


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self, title, msg):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(350, 100)
        layout = QVBoxLayout()
        self.label = QLabel(msg)
        layout.addWidget(self.label)
        self.setLayout(layout)

        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        widget = self.geometry()
        x = ag.width() - widget.width() - 300
        y = 2 * ag.height() - sg.height() - widget.height() - 200
        self.move(x, y)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 500)
        MainWindow.setMinimumSize(QtCore.QSize(710, 500))
        MainWindow.setMaximumSize(QtCore.QSize(710, 500))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setBaseSize(QtCore.QSize(700, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.MainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTabWidget.setGeometry(QtCore.QRect(0, -10, 700, 500))
        self.MainTabWidget.setMinimumSize(QtCore.QSize(500, 400))
        self.MainTabWidget.setMaximumSize(QtCore.QSize(800, 600))
        self.MainTabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.MainTabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.MainTabWidget.setObjectName("MainTabWidget")

        self.Tab_Home = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Tab_Home.setFont(font)
        self.Tab_Home.setStyleSheet("")
        self.Tab_Home.setObjectName("Tab_Home")
        self.groupBox_2 = QtWidgets.QGroupBox(self.Tab_Home)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 19, 681, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_UpdateDatabase = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_UpdateDatabase.setGeometry(QtCore.QRect(12, 40, 231, 71))
        self.btn_UpdateDatabase.setObjectName("pushButton_3")
        self.btn_UpdateDatabase.clicked.connect(lambda: self.click_run_program())
        self.btn_UpdateDatabase.setStyleSheet("background-color: rgb(0, 176, 80);")

        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(17, 120, 661, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(250, 40, 421, 71))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.Tab_Home)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 199, 681, 251))
        self.groupBox_3.setObjectName("groupBox_3")

        # WEEKS CHECKBOXES
        self.check1 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check1.setGeometry(QtCore.QRect(30, 50, 51, 20))
        self.check1.setObjectName("check1")
        self.check2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check2.setGeometry(QtCore.QRect(30, 80, 51, 20))
        self.check2.setObjectName("check2")
        self.check3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check3.setGeometry(QtCore.QRect(30, 110, 51, 20))
        self.check3.setObjectName("check3")
        self.check4 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check4.setGeometry(QtCore.QRect(30, 140, 51, 20))
        self.check4.setObjectName("check4")
        self.check5 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check5.setGeometry(QtCore.QRect(30, 170, 51, 20))
        self.check5.setObjectName("check5")
        self.check6 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check6.setGeometry(QtCore.QRect(90, 50, 51, 20))
        self.check6.setObjectName("check6")
        self.check7 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check7.setGeometry(QtCore.QRect(90, 80, 51, 20))
        self.check7.setObjectName("check7")
        self.check8 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check8.setGeometry(QtCore.QRect(90, 110, 51, 20))
        self.check8.setObjectName("check8")
        self.check9 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check9.setGeometry(QtCore.QRect(90, 140, 51, 20))
        self.check9.setObjectName("check9")
        self.check10 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check10.setGeometry(QtCore.QRect(90, 170, 51, 20))
        self.check10.setObjectName("check10")
        self.check11 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check11.setGeometry(QtCore.QRect(150, 50, 51, 20))
        self.check11.setObjectName("check11")
        self.check12 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check12.setGeometry(QtCore.QRect(150, 80, 51, 20))
        self.check12.setObjectName("check12")
        self.check13 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check13.setGeometry(QtCore.QRect(150, 110, 51, 20))
        self.check13.setObjectName("check13")
        self.check14 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check14.setGeometry(QtCore.QRect(150, 140, 51, 20))
        self.check14.setObjectName("check14")
        self.check15 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check15.setGeometry(QtCore.QRect(150, 170, 51, 20))
        self.check15.setObjectName("check15")
        self.check16 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check16.setGeometry(QtCore.QRect(210, 50, 51, 20))
        self.check16.setObjectName("check11")
        self.check17 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check17.setGeometry(QtCore.QRect(210, 80, 51, 20))
        self.check17.setObjectName("check20")
        self.check18 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check18.setGeometry(QtCore.QRect(210, 110, 51, 20))
        self.check18.setObjectName("check18")
        self.check19 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check19.setGeometry(QtCore.QRect(210, 140, 51, 20))
        self.check19.setObjectName("check14")
        self.check20 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check20.setGeometry(QtCore.QRect(210, 170, 51, 20))
        self.check20.setObjectName("check20")
        self.check21 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check21.setGeometry(QtCore.QRect(270, 50, 51, 20))
        self.check21.setObjectName("check21")
        self.check22 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check22.setGeometry(QtCore.QRect(270, 80, 51, 20))
        self.check22.setObjectName("check22")
        self.check23 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check23.setGeometry(QtCore.QRect(270, 110, 51, 20))
        self.check23.setObjectName("check23")
        self.check24 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check24.setGeometry(QtCore.QRect(270, 140, 51, 20))
        self.check24.setObjectName("check22")
        self.check25 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check25.setGeometry(QtCore.QRect(270, 170, 51, 20))
        self.check25.setObjectName("check22")
        self.check26 = QtWidgets.QCheckBox(self.groupBox_3)
        self.check26.setGeometry(QtCore.QRect(330, 50, 51, 20))
        self.check26.setObjectName("check26")
        self.check_all = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_all.setGeometry(QtCore.QRect(30, 220, 200, 20))
        self.check_all.setObjectName("check_all")
        self.check_all.toggled.connect(self.click_check_all)
        self.all_checkboxes = [0, self.check1, self.check2, self.check3, self.check4,
                               self.check5, self.check6, self.check7, self.check8, self.check9,
                               self.check10, self.check11, self.check12, self.check13, self.check14,
                               self.check15, self.check16, self.check17, self.check18, self.check19,
                               self.check20, self.check21, self.check22, self.check23, self.check24,
                               self.check25, self.check26]
        self.btn_ClearWeeks = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_ClearWeeks.setGeometry(QtCore.QRect(400, 40, 221, 51))
        self.btn_ClearWeeks.setObjectName("btn_ClearWeeks")
        self.btn_ClearWeeks.clicked.connect(lambda: self.click_clear_weeks())
        self.label_clear_warning = QtWidgets.QLabel(self.groupBox_3)
        self.label_clear_warning.setGeometry(QtCore.QRect(410, 110, 181, 61))
        self.label_clear_warning.setObjectName("label_clear_warning")
        self.label_clear_warning.setStyleSheet("color: red")

        # ****************** TAB SETUP ***************************************
        self.MainTabWidget.addTab(self.Tab_Home, "")
        self.Tab_Setup = QtWidgets.QWidget()
        self.Tab_Setup.setObjectName("Tab_Setup")
        # CALENDAR ID %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.lineEdit = QtWidgets.QLineEdit(self.Tab_Setup)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 421, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(config.get_cal_id())
        font = self.lineEdit.font()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.label = QtWidgets.QLabel(self.Tab_Setup)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 41))
        self.label.setObjectName("label")
        self.btn_saveCalendarID = QtWidgets.QPushButton(self.Tab_Setup)
        self.btn_saveCalendarID.setGeometry(QtCore.QRect(580, 10, 111, 31))
        self.btn_saveCalendarID.setObjectName("pushButton")
        self.btn_saveCalendarID.clicked.connect(self.click_update_calendar_id)
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # SAVE FILTER
        self.groupBox = QtWidgets.QGroupBox(self.Tab_Setup)
        self.groupBox.setGeometry(QtCore.QRect(100, 69, 500, 371))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_filteredWords = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_filteredWords.setGeometry(QtCore.QRect(10, 40, 480, 271))
        self.textEdit_filteredWords.setObjectName("textEdit")
        self.textEdit_filteredWords.setText(config.get_bad_words_str())
        self.btn_SaveFilter = QtWidgets.QPushButton(self.groupBox)
        self.btn_SaveFilter.setGeometry(QtCore.QRect(105, 317, 301, 41))
        self.btn_SaveFilter.setObjectName("btn_SaveFilter")
        self.btn_SaveFilter.clicked.connect(lambda: self.click_save_filter())
        self.MainTabWidget.addTab(self.Tab_Setup, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        # *************************** TAB COLORS *****************************
        # YELLOW %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.btn_save_yellow = QtWidgets.QPushButton(self.tab)
        self.btn_save_yellow.setGeometry(QtCore.QRect(270, 50, 61, 91))
        self.btn_save_yellow.setObjectName("pushButton_5")
        self.btn_save_yellow.clicked.connect(lambda: self.click_update_color(self.textEdit_yellow.toPlainText(), 'Yellow'))
        self.label_yellow = QtWidgets.QLabel(self.tab)
        self.label_yellow.setGeometry(QtCore.QRect(40, 20, 111, 21))
        self.label_yellow.setObjectName("label_3")
        self.textEdit_yellow = QtWidgets.QTextEdit(self.tab)
        self.textEdit_yellow.setGeometry(QtCore.QRect(30, 50, 231, 87))
        self.textEdit_yellow.setObjectName("textEdit_2")
        self.textEdit_yellow.setText(config.get_color_filter('Yellow'))
        font = self.textEdit_yellow.font()
        font.setPointSize(12)
        self.textEdit_yellow.setFont(font)
        # CYAN %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.btn_save_cyan = QtWidgets.QPushButton(self.tab)
        self.btn_save_cyan.setGeometry(QtCore.QRect(270, 200, 61, 91))
        self.btn_save_cyan.setObjectName("btn_save_cyan")
        self.btn_save_cyan.clicked.connect(
            lambda: self.click_update_color(self.textEdit_cyan.toPlainText(), 'Cyan'))
        self.textEdit_cyan = QtWidgets.QTextEdit(self.tab)
        self.textEdit_cyan.setGeometry(QtCore.QRect(30, 200, 231, 87))
        self.textEdit_cyan.setObjectName("textEdit_cyan")
        self.textEdit_cyan.setText(config.get_color_filter('Cyan'))
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 111, 21))
        self.label_4.setObjectName("label_4")
        self.textEdit_cyan.setFont(font)
        # RED %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.btn_save_red = QtWidgets.QPushButton(self.tab)
        self.btn_save_red.setGeometry(QtCore.QRect(600, 50, 61, 91))
        self.btn_save_red.setObjectName("btn_save_red")
        self.btn_save_red.clicked.connect(
            lambda: self.click_update_color(self.textEdit_red.toPlainText(), 'Red'))
        self.textEdit_red = QtWidgets.QTextEdit(self.tab)
        self.textEdit_red.setGeometry(QtCore.QRect(360, 50, 231, 87))
        self.textEdit_red.setObjectName("textEdit_red")
        self.textEdit_red.setText(config.get_color_filter('Red'))
        self.textEdit_red.setFont(font)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(370, 20, 111, 21))
        self.label_5.setObjectName("label_5")
        # PURPLE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.btn_save_purple = QtWidgets.QPushButton(self.tab)
        self.btn_save_purple.setGeometry(QtCore.QRect(600, 200, 61, 91))
        self.btn_save_purple.setObjectName("btn_save_purple")
        self.btn_save_purple.clicked.connect(
            lambda: self.click_update_color(self.textEdit_purple.toPlainText(), 'Purple'))
        self.textEdit_purple = QtWidgets.QTextEdit(self.tab)
        self.textEdit_purple.setGeometry(QtCore.QRect(360, 200, 231, 87))
        self.textEdit_purple.setObjectName("textEdit_purple")
        self.textEdit_purple.setText(config.get_color_filter('Purple'))
        self.textEdit_purple.setFont(font)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(370, 170, 111, 21))
        self.label_6.setObjectName("label_6")
        # WHITE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.pushButton_white = QtWidgets.QPushButton(self.tab)
        self.pushButton_white.setGeometry(QtCore.QRect(270, 350, 61, 91))
        self.pushButton_white.setObjectName("pushButton_white")
        self.pushButton_white.clicked.connect(
            lambda: self.click_update_color(self.textEdit_white.toPlainText(), 'White'))
        self.textEdit_white = QtWidgets.QTextEdit(self.tab)
        self.textEdit_white.setGeometry(QtCore.QRect(30, 350, 231, 87))
        self.textEdit_white.setObjectName("textEdit_white")
        self.textEdit_white.setText(config.get_color_filter('White'))
        self.textEdit_white.setFont(font)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(40, 320, 111, 21))
        self.label_7.setObjectName("label_7")
        # GREEN %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.pushButton_green = QtWidgets.QPushButton(self.tab)
        self.pushButton_green.setGeometry(QtCore.QRect(600, 350, 61, 91))
        self.pushButton_green.setObjectName("pushButton_green")
        self.pushButton_green.clicked.connect(
            lambda: self.click_update_color(self.textEdit_green.toPlainText(), 'Green'))
        self.textEdit_green = QtWidgets.QTextEdit(self.tab)
        self.textEdit_green.setGeometry(QtCore.QRect(360, 350, 231, 87))
        self.textEdit_green.setObjectName("textEdit_green")
        self.textEdit_green.setText(config.get_color_filter('Green'))
        self.textEdit_green.setFont(font)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(370, 320, 111, 21))
        self.label_8.setObjectName("label_8")
        # END OF COLORS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        # ****************** TAB HELP ***********************************
        self.MainTabWidget.addTab(self.tab, "")
        self.Tab_Help = QtWidgets.QWidget()
        self.Tab_Help.setObjectName("Tab_Help")
        self.textBrowser = QtWidgets.QTextBrowser(self.Tab_Help)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 661, 431))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("developed by aviv drori")  # todo make it better
        self.MainTabWidget.addTab(self.Tab_Help, "")
        MainWindow.setCentralWidget(self.centralwidget)

        # ********** MAIN **********************************************
        self.retranslateUi(MainWindow)
        self.MainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def popup_msg(self, title, msg):
        self.popup = AnotherWindow(title, msg)
        self.popup.show()

    def click_update_color(self, words, color):
        config.set_color_filter(words, color)

    def click_update_calendar_id(self):
        config.set_cal_id(self.lineEdit.text())
        self.popup_msg("Calendar ID saved", "Calendar ID has been updated.\nNow rerun the update.")

    def click_run_program(self):
        self.progressBar.setValue(0)
        main.update_database()
        x=0
        while x < 100:
            x += 0.001
            self.progressBar.setValue(int(x))
        self.popup_msg("Calendar Updated.", "The excel has been rewritten.")

    def click_save_filter(self):
        config.set_bad_words(self.textEdit_filteredWords.toPlainText())

    def click_clear_weeks(self):
        weeks_to_clear = []
        for i in range(1, 27):
            if self.all_checkboxes[i].isChecked():
                weeks_to_clear.append(i)
        if len(weeks_to_clear) != 0:
            database.clear_events(weeks_to_clear)
            self.popup_msg("Cleared Weeks:",
                           "Successfully cleared weeks " +
                           ','.join(str(x) for x in weeks_to_clear))
            database.save()

    def click_check_all(self):
        is_checked = self.check_all.isChecked()
        for i in range(1, 27):
            self.all_checkboxes[i].setChecked(is_checked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Calendar v1"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Update Database"))
        self.btn_UpdateDatabase.setText(_translate("MainWindow", "Run Update"))
        self.label_2.setText(_translate("MainWindow", "Run the main program: get the events from\n"
                                        "Google Calendar and write to database."))
        self.groupBox_3.setTitle(_translate("MainWindow", "Clear Weeks"))
        self.check1.setText(_translate("MainWindow", "1"))
        self.check2.setText(_translate("MainWindow", "2"))
        self.check3.setText(_translate("MainWindow", "3"))
        self.check4.setText(_translate("MainWindow", "4"))
        self.check6.setText(_translate("MainWindow", "6"))
        self.check5.setText(_translate("MainWindow", "5"))
        self.check7.setText(_translate("MainWindow", "7"))
        self.check8.setText(_translate("MainWindow", "8"))
        self.check9.setText(_translate("MainWindow", "9"))
        self.check10.setText(_translate("MainWindow", "10"))
        self.check11.setText(_translate("MainWindow", "11"))
        self.check12.setText(_translate("MainWindow", "12"))
        self.check13.setText(_translate("MainWindow", "13"))
        self.check14.setText(_translate("MainWindow", "14"))
        self.check15.setText(_translate("MainWindow", "15"))
        self.check16.setText(_translate("MainWindow", "16"))
        self.check17.setText(_translate("MainWindow", "17"))
        self.check18.setText(_translate("MainWindow", "18"))
        self.check19.setText(_translate("MainWindow", "19"))
        self.check20.setText(_translate("MainWindow", "20"))
        self.check21.setText(_translate("MainWindow", "21"))
        self.check22.setText(_translate("MainWindow", "22"))
        self.check23.setText(_translate("MainWindow", "23"))
        self.check24.setText(_translate("MainWindow", "24"))
        self.check25.setText(_translate("MainWindow", "25"))
        self.check26.setText(_translate("MainWindow", "26"))
        self.check_all.setText(_translate("MainWindow", "Select All"))
        self.btn_ClearWeeks.setText(_translate("MainWindow", "Clear selected weeks"))
        self.label_clear_warning.setText(_translate("MainWindow", "Warning!\n"
                                                    "This is irreversible!"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.Tab_Home), _translate("MainWindow", "Home"))
        self.label.setText(_translate("MainWindow", "Calendar ID:"))
        self.btn_saveCalendarID.setText(_translate("MainWindow", "Save"))
        self.groupBox.setTitle(_translate("MainWindow", "Filter:"))
        self.btn_SaveFilter.setText(_translate("MainWindow", "Save Filter"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.Tab_Setup), _translate("MainWindow", "Setup"))
        self.btn_save_yellow.setText(_translate("MainWindow", "Save"))
        self.label_yellow.setText(_translate("MainWindow", "Yellow:"))
        self.btn_save_cyan.setText(_translate("MainWindow", "Save"))
        self.label_4.setText(_translate("MainWindow", "Cyan:"))
        self.btn_save_red.setText(_translate("MainWindow", "Save"))
        self.label_5.setText(_translate("MainWindow", "Red:"))
        self.btn_save_purple.setText(_translate("MainWindow", "Save"))
        self.label_6.setText(_translate("MainWindow", "Purple:"))
        self.pushButton_white.setText(_translate("MainWindow", "Save"))
        self.label_7.setText(_translate("MainWindow", "White:"))
        self.pushButton_green.setText(_translate("MainWindow", "Save"))
        self.label_8.setText(_translate("MainWindow", "Green:"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.tab), _translate("MainWindow", "Colors"))
        self.MainTabWidget.setTabText(self.MainTabWidget.indexOf(self.Tab_Help), _translate("MainWindow", "Help"))


if __name__ == "__main__":
    # update:
    config.read_setup_files()
    config.read_color_file()
    # default:
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
