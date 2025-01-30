# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(427, 213)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(14, -3, 401, 61))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.p_uyeler = QPushButton(self.centralwidget)
        self.p_uyeler.setObjectName(u"p_uyeler")
        self.p_uyeler.setGeometry(QRect(11, 53, 94, 111))
        self.p_planlistesi = QPushButton(self.centralwidget)
        self.p_planlistesi.setObjectName(u"p_planlistesi")
        self.p_planlistesi.setGeometry(QRect(326, 53, 94, 111))
        self.p_egitmenler = QPushButton(self.centralwidget)
        self.p_egitmenler.setObjectName(u"p_egitmenler")
        self.p_egitmenler.setGeometry(QRect(111, 53, 93, 111))
        self.p_antrenmanp = QPushButton(self.centralwidget)
        self.p_antrenmanp.setObjectName(u"p_antrenmanp")
        self.p_antrenmanp.setGeometry(QRect(210, 53, 110, 111))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 427, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Fitness Club", None))
        self.p_uyeler.setText(QCoreApplication.translate("MainWindow", u"\u00dcyeler", None))
        self.p_planlistesi.setText(QCoreApplication.translate("MainWindow", u"Plan Listesi", None))
        self.p_egitmenler.setText(QCoreApplication.translate("MainWindow", u"E\u011fitmenler", None))
        self.p_antrenmanp.setText(QCoreApplication.translate("MainWindow", u"Antrenman Olu\u015ftur", None))
    # retranslateUi

