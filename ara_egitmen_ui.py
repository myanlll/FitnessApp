# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ara_konut.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_araegitmen(object):
    def setupUi(self, araegitmen):
        if not araegitmen.objectName():
            araegitmen.setObjectName(u"araegitmen")
        araegitmen.resize(730, 225)
        self.horizontalLayoutWidget = QWidget(araegitmen)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 20, 691, 121))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayoutWidget_3 = QWidget(araegitmen)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(120, 20, 211, 121))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.line_konut_turu = QLineEdit(self.verticalLayoutWidget_3)
        self.line_konut_turu.setObjectName(u"line_konut_turu")

        self.verticalLayout_3.addWidget(self.line_konut_turu)

        self.line_mersis = QLineEdit(self.verticalLayoutWidget_3)
        self.line_mersis.setObjectName(u"line_mersis")

        self.verticalLayout_3.addWidget(self.line_mersis)

        self.line_uretim_yili = QLineEdit(self.verticalLayoutWidget_3)
        self.line_uretim_yili.setObjectName(u"line_uretim_yili")

        self.verticalLayout_3.addWidget(self.line_uretim_yili)

        self.verticalLayoutWidget_4 = QWidget(araegitmen)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(480, 20, 181, 121))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line_cephe = QLineEdit(self.verticalLayoutWidget_4)
        self.line_cephe.setObjectName(u"line_cephe")

        self.verticalLayout_4.addWidget(self.line_cephe)

        self.line_havuz = QLineEdit(self.verticalLayoutWidget_4)
        self.line_havuz.setObjectName(u"line_havuz")

        self.verticalLayout_4.addWidget(self.line_havuz)

        self.line_durum = QLineEdit(self.verticalLayoutWidget_4)
        self.line_durum.setObjectName(u"line_durum")

        self.verticalLayout_4.addWidget(self.line_durum)

        self.push_bul = QPushButton(araegitmen)
        self.push_bul.setObjectName(u"push_bul")
        self.push_bul.setGeometry(QRect(250, 150, 231, 51))

        self.retranslateUi(araegitmen)

        QMetaObject.connectSlotsByName(araegitmen)
    # setupUi

    def retranslateUi(self, araegitmen):
        araegitmen.setWindowTitle(QCoreApplication.translate("araegitmen", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("araegitmen", u"Konut T\u00fcr\u00fc", None))
        self.label_3.setText(QCoreApplication.translate("araegitmen", u"Mersis No", None))
        self.label_6.setText(QCoreApplication.translate("araegitmen", u"\u00dcretim Y\u0131l\u0131", None))
        self.label_7.setText(QCoreApplication.translate("araegitmen", u"Cephe", None))
        self.label_5.setText(QCoreApplication.translate("araegitmen", u"Havuz", None))
        self.label_8.setText(QCoreApplication.translate("araegitmen", u"Durum", None))
        self.push_bul.setText(QCoreApplication.translate("araegitmen", u"Bul", None))
    # retranslateUi

