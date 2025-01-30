# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'egitmenler.ui'
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
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_egitmenler(object):
    def setupUi(self, egitmenler):
        if not egitmenler.objectName():
            egitmenler.setObjectName(u"egitmenler")
        egitmenler.resize(1035, 425)
        self.verticalLayoutWidget = QWidget(egitmenler)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(856, 9, 171, 151))
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

        self.gridLayoutWidget = QWidget(egitmenler)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(6, 8, 841, 156))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.line_tecrube = QLineEdit(self.gridLayoutWidget)
        self.line_tecrube.setObjectName(u"line_tecrube")

        self.horizontalLayout_8.addWidget(self.line_tecrube)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.line_egitmen_id = QLineEdit(self.gridLayoutWidget)
        self.line_egitmen_id.setObjectName(u"line_egitmen_id")
        self.line_egitmen_id.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.line_egitmen_id)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.line_egitim_derecesi = QLineEdit(self.gridLayoutWidget)
        self.line_egitim_derecesi.setObjectName(u"line_egitim_derecesi")

        self.horizontalLayout_5.addWidget(self.line_egitim_derecesi)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.line_egitmen_tc = QLineEdit(self.gridLayoutWidget)
        self.line_egitmen_tc.setObjectName(u"line_egitmen_tc")

        self.horizontalLayout.addWidget(self.line_egitmen_tc)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.line_cinsiyet = QLineEdit(self.gridLayoutWidget)
        self.line_cinsiyet.setObjectName(u"line_cinsiyet")

        self.horizontalLayout_6.addWidget(self.line_cinsiyet)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.line_egitmen_ad = QLineEdit(self.gridLayoutWidget)
        self.line_egitmen_ad.setObjectName(u"line_egitmen_ad")

        self.horizontalLayout_4.addWidget(self.line_egitmen_ad)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.line_calisma_saatleri = QLineEdit(self.gridLayoutWidget)
        self.line_calisma_saatleri.setObjectName(u"line_calisma_saatleri")
        self.line_calisma_saatleri.setEnabled(True)

        self.horizontalLayout_14.addWidget(self.line_calisma_saatleri)


        self.gridLayout_2.addLayout(self.horizontalLayout_14, 3, 1, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.line_dogum = QLineEdit(self.gridLayoutWidget)
        self.line_dogum.setObjectName(u"line_dogum")
        self.line_dogum.setEnabled(True)

        self.horizontalLayout_13.addWidget(self.line_dogum)


        self.gridLayout_2.addLayout(self.horizontalLayout_13, 3, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.line_adres = QLineEdit(self.gridLayoutWidget)
        self.line_adres.setObjectName(u"line_adres")
        self.line_adres.setEnabled(True)

        self.horizontalLayout_11.addWidget(self.line_adres)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.radiosaglikli = QRadioButton(self.gridLayoutWidget)
        self.radiosaglikli.setObjectName(u"radiosaglikli")

        self.horizontalLayout_12.addWidget(self.radiosaglikli)

        self.radioraporlu = QRadioButton(self.gridLayoutWidget)
        self.radioraporlu.setObjectName(u"radioraporlu")

        self.horizontalLayout_12.addWidget(self.radioraporlu)


        self.gridLayout_2.addLayout(self.horizontalLayout_12, 4, 1, 1, 1)

        self.tableWidget = QTableWidget(egitmenler)
        if (self.tableWidget.columnCount() < 10):
            self.tableWidget.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(6, 169, 1021, 251))

        self.retranslateUi(egitmenler)

        QMetaObject.connectSlotsByName(egitmenler)
    # setupUi

    def retranslateUi(self, egitmenler):
        egitmenler.setWindowTitle(QCoreApplication.translate("egitmenler", u"Form", None))
        self.push_yeni.setText(QCoreApplication.translate("egitmenler", u"Yeni", None))
        self.push_guncelle.setText(QCoreApplication.translate("egitmenler", u"G\u00fcncelle", None))
        self.push_kaydet.setText(QCoreApplication.translate("egitmenler", u"Kaydet", None))
        self.push_sil.setText(QCoreApplication.translate("egitmenler", u"Sil", None))
        self.push_ara.setText(QCoreApplication.translate("egitmenler", u"Ara", None))
        self.label_8.setText(QCoreApplication.translate("egitmenler", u"Tecr\u00fcbe (Y\u0131l)       ", None))
        self.label_7.setText(QCoreApplication.translate("egitmenler", u"E\u011fitmen ID       ", None))
        self.label_5.setText(QCoreApplication.translate("egitmenler", u"E\u011fitim Derecesi  ", None))
        self.label.setText(QCoreApplication.translate("egitmenler", u"E\u011fitmen Kimlik", None))
        self.label_6.setText(QCoreApplication.translate("egitmenler", u"Cinsiyet             ", None))
        self.label_4.setText(QCoreApplication.translate("egitmenler", u"E\u011fitmen Ad\u0131     ", None))
        self.label_14.setText(QCoreApplication.translate("egitmenler", u"\u00c7al\u0131\u015fma Saatleri ", None))
        self.label_13.setText(QCoreApplication.translate("egitmenler", u"Do\u011fum Y\u0131l\u0131       ", None))
        self.label_11.setText(QCoreApplication.translate("egitmenler", u"Adres                   ", None))
        self.label_12.setText(QCoreApplication.translate("egitmenler", u"Sa\u011fl\u0131k Durumu", None))
        self.radiosaglikli.setText(QCoreApplication.translate("egitmenler", u"Sa\u011fl\u0131kl\u0131", None))
        self.radioraporlu.setText(QCoreApplication.translate("egitmenler", u"Raporlu", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("egitmenler", u"10", None));
    # retranslateUi

