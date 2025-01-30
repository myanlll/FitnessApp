# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uyeler.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_uyeler(object):
    def setupUi(self, uyeler):
        if not uyeler.objectName():
            uyeler.setObjectName(u"uyeler")
        uyeler.resize(879, 462)
        self.tableWidget = QTableWidget(uyeler)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(4, 165, 871, 291))
        self.gridLayoutWidget = QWidget(uyeler)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(4, 5, 691, 156))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.line_ad = QLineEdit(self.gridLayoutWidget)
        self.line_ad.setObjectName(u"line_ad")

        self.horizontalLayout_4.addWidget(self.line_ad)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.line_soyad = QLineEdit(self.gridLayoutWidget)
        self.line_soyad.setObjectName(u"line_soyad")

        self.horizontalLayout_5.addWidget(self.line_soyad)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.line_dogum = QLineEdit(self.gridLayoutWidget)
        self.line_dogum.setObjectName(u"line_dogum")
        self.line_dogum.setEnabled(True)

        self.horizontalLayout_11.addWidget(self.line_dogum)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 3, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.line_eposta = QLineEdit(self.gridLayoutWidget)
        self.line_eposta.setObjectName(u"line_eposta")

        self.horizontalLayout_6.addWidget(self.line_eposta)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.line_adres = QLineEdit(self.gridLayoutWidget)
        self.line_adres.setObjectName(u"line_adres")
        self.line_adres.setEnabled(True)

        self.horizontalLayout_13.addWidget(self.line_adres)


        self.gridLayout_2.addLayout(self.horizontalLayout_13, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.line_TC = QLineEdit(self.gridLayoutWidget)
        self.line_TC.setObjectName(u"line_TC")

        self.horizontalLayout.addWidget(self.line_TC)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.line_telefon = QLineEdit(self.gridLayoutWidget)
        self.line_telefon.setObjectName(u"line_telefon")

        self.horizontalLayout_8.addWidget(self.line_telefon)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.line_kullanici_id = QLineEdit(self.gridLayoutWidget)
        self.line_kullanici_id.setObjectName(u"line_kullanici_id")
        self.line_kullanici_id.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.line_kullanici_id)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.verticalLayoutWidget = QWidget(uyeler)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(702, 7, 171, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.push_yeni = QPushButton(self.verticalLayoutWidget)
        self.push_yeni.setObjectName(u"push_yeni")

        self.verticalLayout.addWidget(self.push_yeni)

        self.push_guncelle = QPushButton(self.verticalLayoutWidget)
        self.push_guncelle.setObjectName(u"push_guncelle")

        self.verticalLayout.addWidget(self.push_guncelle)

        self.push_kaydet = QPushButton(self.verticalLayoutWidget)
        self.push_kaydet.setObjectName(u"push_kaydet")

        self.verticalLayout.addWidget(self.push_kaydet)

        self.push_sil = QPushButton(self.verticalLayoutWidget)
        self.push_sil.setObjectName(u"push_sil")

        self.verticalLayout.addWidget(self.push_sil)

        self.push_ara = QPushButton(self.verticalLayoutWidget)
        self.push_ara.setObjectName(u"push_ara")

        self.verticalLayout.addWidget(self.push_ara)


        self.retranslateUi(uyeler)

        QMetaObject.connectSlotsByName(uyeler)
    # setupUi

    def retranslateUi(self, uyeler):
        uyeler.setWindowTitle(QCoreApplication.translate("uyeler", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("uyeler", u"Ad", None))
        self.label_5.setText(QCoreApplication.translate("uyeler", u"Soyad", None))
        self.label_11.setText(QCoreApplication.translate("uyeler", u"Do\u011fum Tarihi", None))
        self.label_6.setText(QCoreApplication.translate("uyeler", u"E-Posta", None))
        self.label_13.setText(QCoreApplication.translate("uyeler", u"Adres", None))
        self.label.setText(QCoreApplication.translate("uyeler", u"TC Kimlik", None))
        self.label_8.setText(QCoreApplication.translate("uyeler", u"Telefon No:", None))
        self.label_7.setText(QCoreApplication.translate("uyeler", u"\u00dcye ID", None))
        self.push_yeni.setText(QCoreApplication.translate("uyeler", u"Yeni", None))
        self.push_guncelle.setText(QCoreApplication.translate("uyeler", u"G\u00fcncelle", None))
        self.push_kaydet.setText(QCoreApplication.translate("uyeler", u"Kaydet", None))
        self.push_sil.setText(QCoreApplication.translate("uyeler", u"Sil", None))
        self.push_ara.setText(QCoreApplication.translate("uyeler", u"Ara", None))
    # retranslateUi

