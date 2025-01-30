# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'konutlar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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

class Ui_egitmenler(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1240, 580)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(1060, 30, 171, 151))
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

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 190, 1221, 381))
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 1041, 156))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.line_mersis = QLineEdit(self.gridLayoutWidget)
        self.line_mersis.setObjectName(u"line_mersis")

        self.horizontalLayout_6.addWidget(self.line_mersis)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.line_konut_id = QLineEdit(self.gridLayoutWidget)
        self.line_konut_id.setObjectName(u"line_konut_id")
        self.line_konut_id.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.line_konut_id)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.line_konut_tur = QLineEdit(self.gridLayoutWidget)
        self.line_konut_tur.setObjectName(u"line_konut_tur")

        self.horizontalLayout_4.addWidget(self.line_konut_tur)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.line_cephe = QLineEdit(self.gridLayoutWidget)
        self.line_cephe.setObjectName(u"line_cephe")

        self.horizontalLayout_5.addWidget(self.line_cephe)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.line_konum = QLineEdit(self.gridLayoutWidget)
        self.line_konum.setObjectName(u"line_konum")
        self.line_konum.setEnabled(True)

        self.horizontalLayout_11.addWidget(self.line_konum)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 3, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.line_havuz = QLineEdit(self.gridLayoutWidget)
        self.line_havuz.setObjectName(u"line_havuz")

        self.horizontalLayout_8.addWidget(self.line_havuz)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.line_konut_alan = QLineEdit(self.gridLayoutWidget)
        self.line_konut_alan.setObjectName(u"line_konut_alan")
        self.line_konut_alan.setEnabled(True)

        self.horizontalLayout_14.addWidget(self.line_konut_alan)


        self.gridLayout_2.addLayout(self.horizontalLayout_14, 0, 2, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.line_uretimyil = QLineEdit(self.gridLayoutWidget)
        self.line_uretimyil.setObjectName(u"line_uretimyil")
        self.line_uretimyil.setEnabled(True)

        self.horizontalLayout_13.addWidget(self.line_uretimyil)


        self.gridLayout_2.addLayout(self.horizontalLayout_13, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.line_renk = QLineEdit(self.gridLayoutWidget)
        self.line_renk.setObjectName(u"line_renk")

        self.horizontalLayout.addWidget(self.line_renk)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.line_odasayi = QLineEdit(self.gridLayoutWidget)
        self.line_odasayi.setObjectName(u"line_odasayi")
        self.line_odasayi.setEnabled(True)

        self.horizontalLayout_15.addWidget(self.line_odasayi)


        self.gridLayout_2.addLayout(self.horizontalLayout_15, 1, 2, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.line_durum = QLineEdit(self.gridLayoutWidget)
        self.line_durum.setObjectName(u"line_durum")
        self.line_durum.setEnabled(True)

        self.horizontalLayout_12.addWidget(self.line_durum)


        self.gridLayout_2.addLayout(self.horizontalLayout_12, 3, 2, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.line_kira = QLineEdit(self.gridLayoutWidget)
        self.line_kira.setObjectName(u"line_kira")

        self.horizontalLayout_10.addWidget(self.line_kira)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.push_yeni.setText(QCoreApplication.translate("Form", u"Yeni", None))
        self.push_guncelle.setText(QCoreApplication.translate("Form", u"G\u00fcncelle", None))
        self.push_kaydet.setText(QCoreApplication.translate("Form", u"Kaydet", None))
        self.push_sil.setText(QCoreApplication.translate("Form", u"Sil", None))
        self.push_ara.setText(QCoreApplication.translate("Form", u"Ara", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"5", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"6", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"7", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"8", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"9", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"10", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"11", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"12", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"1", None));
        self.label_6.setText(QCoreApplication.translate("Form", u"Mersis No", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Konut ID", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Konut T\u00fcr\u00fc", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Cephe", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Konum", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Havuz", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Konut Alan\u0131", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u00dcretim Y\u0131l\u0131", None))
        self.label.setText(QCoreApplication.translate("Form", u"Renk", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Oda Say\u0131s\u0131", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Durum", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Kira Bedeli/G\u00fcn", None))
    # retranslateUi

