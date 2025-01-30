# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plandakiler.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_plandakiler(object):
    def setupUi(self, plandakiler):
        if not plandakiler.objectName():
            plandakiler.setObjectName(u"plandakiler")
        plandakiler.resize(1180, 369)
        self.verticalLayoutWidget_2 = QWidget(plandakiler)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 0, 991, 156))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_26 = QLabel(self.verticalLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_26.addWidget(self.label_26)

        self.line_plan_id = QLineEdit(self.verticalLayoutWidget_2)
        self.line_plan_id.setObjectName(u"line_plan_id")
        self.line_plan_id.setEnabled(False)

        self.horizontalLayout_26.addWidget(self.line_plan_id)


        self.verticalLayout_4.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_27 = QLabel(self.verticalLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_27.addWidget(self.label_27)

        self.line_egitmen_ad = QLineEdit(self.verticalLayoutWidget_2)
        self.line_egitmen_ad.setObjectName(u"line_egitmen_ad")
        self.line_egitmen_ad.setEnabled(False)

        self.horizontalLayout_27.addWidget(self.line_egitmen_ad)


        self.verticalLayout_4.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_28 = QLabel(self.verticalLayoutWidget_2)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_28.addWidget(self.label_28)

        self.line_uye_ad = QLineEdit(self.verticalLayoutWidget_2)
        self.line_uye_ad.setObjectName(u"line_uye_ad")
        self.line_uye_ad.setEnabled(False)

        self.horizontalLayout_28.addWidget(self.line_uye_ad)


        self.verticalLayout_4.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_29 = QLabel(self.verticalLayoutWidget_2)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_29.addWidget(self.label_29)

        self.line_bitis_tarihi = QLineEdit(self.verticalLayoutWidget_2)
        self.line_bitis_tarihi.setObjectName(u"line_bitis_tarihi")
        self.line_bitis_tarihi.setEnabled(False)

        self.horizontalLayout_29.addWidget(self.line_bitis_tarihi)


        self.verticalLayout_4.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_30 = QLabel(self.verticalLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_30.addWidget(self.label_30)

        self.line_calisma_saatleri = QLineEdit(self.verticalLayoutWidget_2)
        self.line_calisma_saatleri.setObjectName(u"line_calisma_saatleri")
        self.line_calisma_saatleri.setEnabled(False)

        self.horizontalLayout_30.addWidget(self.line_calisma_saatleri)


        self.verticalLayout_4.addLayout(self.horizontalLayout_30)

        self.tableWidget = QTableWidget(plandakiler)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 170, 991, 191))
        self.push_bitir = QPushButton(plandakiler)
        self.push_bitir.setObjectName(u"push_bitir")
        self.push_bitir.setGeometry(QRect(1010, 10, 161, 351))

        self.retranslateUi(plandakiler)

        QMetaObject.connectSlotsByName(plandakiler)
    # setupUi

    def retranslateUi(self, plandakiler):
        plandakiler.setWindowTitle(QCoreApplication.translate("plandakiler", u"Form", None))
        self.label_26.setText(QCoreApplication.translate("plandakiler", u"Plan ID                ", None))
        self.label_27.setText(QCoreApplication.translate("plandakiler", u"E\u011fitmen Ad        ", None))
        self.label_28.setText(QCoreApplication.translate("plandakiler", u"\u00dcye Ad\u0131               ", None))
        self.label_29.setText(QCoreApplication.translate("plandakiler", u"Plan Biti\u015f Tarihi  ", None))
        self.label_30.setText(QCoreApplication.translate("plandakiler", u"\u00c7al\u0131\u015fma Saatleri ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("plandakiler", u"1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("plandakiler", u"2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("plandakiler", u"3", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("plandakiler", u"4", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("plandakiler", u"5", None));
        self.push_bitir.setText(QCoreApplication.translate("plandakiler", u"Plan \u0130ptal", None))
    # retranslateUi

