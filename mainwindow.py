# This Python file uses the following encoding: utf-8
import sys
import pypyodbc

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QMessageBox

from PySide6.QtCore import QDate

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_egitmenler import Ui_egitmenler
from ui_uyeler import Ui_uyeler
from ui_bul import Ui_bul
from ui_ara_egitmen import Ui_araegitmen
from ui_planlama import Ui_planlama
from ui_plandakiler import Ui_plandakiler



class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.target_db = "vt_**********"
        self.ui.p_uyeler.clicked.connect(self.open_uyeler)
        self.ui.p_egitmenler.clicked.connect(self.open_egitmenler)
        self.ui.p_antrenmanp.clicked.connect(self.open_planlama)
        self.ui.p_planlistesi.clicked.connect(self.open_plandakiler)
        
        self.dbConn = None
        self.sqlBaglan()


    def sqlBaglan(self):
        self.dbConn = pypyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-*******\\SQLEXPRESS;Database=vt_**********;Trusted_Connection=yes;')
        self.mycursor = self.dbConn.cursor()


    def open_uyeler(self):
        self.m = uyeler(self)
        self.m.show()

    def open_egitmenler(self):
        self.a = egitmenler(self)
        self.a.show()

    def open_planlama(self):
        self.k = planlama(self)
        self.k.show()

    def open_plandakiler(self):
        self.d = plandakiler(self)
        self.d.show()


class uyeler(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_uyeler()
        self.ui.setupUi(self)
        self.Qwidget = QWidget
        self.mainWindow = mainWindow
        self.ui.tableWidget.setHorizontalHeaderLabels(["Id","Ad","Soyad","TC","Doğum Tarihi","Adres","Telefon","E-Posta"])
        self.ui.tableWidget.setColumnWidth(0, 65)
        self.ui.tableWidget.setColumnWidth(1, 135)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 95)
        self.ui.tableWidget.setColumnWidth(4, 85)
        self.ui.tableWidget.setColumnWidth(5, 125)
        self.ui.tableWidget.setColumnWidth(6, 90)
        self.ui.tableWidget.setColumnWidth(7, 139)
        self.ui.push_sil.setEnabled(False)
        self.ui.push_guncelle.setEnabled(False)
        self.ui.mycursor = self.mainWindow.mycursor

        query = f"SELECT * FROM {self.mainWindow.target_db}.dbo.uyeler"
        self.mainWindow.mycursor.execute(query)
        self.table_doldur()

        self.ui.push_ara.clicked.connect(self.open_bul)
        self.ui.push_yeni.clicked.connect(self.yeni_fonk)
        self.ui.push_sil.clicked.connect(self.sil_fonk)
        self.ui.push_guncelle.clicked.connect(self.guncelle_fonk)
        self.ui.push_kaydet.clicked.connect(self.kaydet_fonk)
        self.ui.tableWidget.doubleClicked.connect(self.get_info_fonk)



    def open_bul(self):
        self.b = bul(self)
        self.b.show()



    def yeni_fonk(self):
        self.ui.line_ad.setText("")
        self.ui.line_soyad.setText("")
        self.ui.line_TC.setText("")
        self.ui.line_eposta.setText("")
        self.ui.line_dogum.setText("")
        self.ui.line_kullanici_id.setText("")
        self.ui.line_adres.setText("")
        self.ui.line_telefon.setText("")
        self.ui.push_sil.setEnabled(False)
        self.ui.push_guncelle.setEnabled(False)



    def sil_fonk(self):
        result = self.mesaj("Silmek İstediğinize Emin Misiniz?")

        if result == QMessageBox.Yes:
            try:
                id = int(self.ui.line_kullanici_id.text())
                query = f"""
                    DELETE FROM [{self.mainWindow.target_db}].[dbo].[uyeler]
                    WHERE id = ?;
                """
                self.mainWindow.mycursor.execute(query, (id,))
                self.ui.push_sil.setEnabled(False)
                self.mainWindow.dbConn.commit()
                self.ara_fonk()

            except ValueError:
                self.statusBar.showMessage("Geçersiz ID", 4000)
        else:
            pass




    def guncelle_fonk(self):
        id = int(self.ui.line_kullanici_id.text())
        ad = self.ui.line_ad.text()
        soyad = self.ui.line_soyad.text()
        tc = self.ui.line_TC.text()
        dogum_tarihi = self.ui.line_dogum.text()
        adres = self.ui.line_adres.text()
        telefon = self.ui.line_telefon.text()
        e_posta = self.ui.line_eposta.text()

        sorgu = f"""
            UPDATE [{self.mainWindow.target_db}].[dbo].[uyeler] SET
            ad = ?,
            soyad = ?,
            tc = ?,
            dogum_tarihi = ?,
            adres = ?,
            telefon = ?,
            e_posta = ?
            WHERE id = ?;
        """
        degerler = (ad, soyad, tc, dogum_tarihi, adres, telefon, e_posta, id)

        try:
            self.mainWindow.mycursor.execute(sorgu, degerler)
            self.mainWindow.dbConn.commit()
            self.ui.push_guncelle.setEnabled(False)
            self.ara_fonk()
        except Exception as e:
            print(f"Hata: {str(e)}")




    def kaydet_fonk(self):
        if self.ui.line_kullanici_id.text() != "":
            result = self.mesaj("Bu kayıt zaten mevcut. Güncellemek ister misiniz?")
            if result == QMessageBox.Yes:
                self.guncelle_fonk()
            else:
                pass
        else:
            sqlBaglan = """
            INSERT INTO uyeler
            (ad, soyad, tc, dogum_tarihi, adres, telefon, e_posta)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            self.veri = (
                self.ui.line_ad.text(),
                self.ui.line_soyad.text(),
                self.ui.line_TC.text(),
                self.ui.line_dogum.text(),
                self.ui.line_adres.text(),
                self.ui.line_telefon.text(),
                self.ui.line_eposta.text()
            )

            try:
                self.mainWindow.mycursor.execute(sqlBaglan, self.veri)
                self.mainWindow.dbConn.commit()
            except pypyodbc.Error as e:
                print(f"Hata: {str(e)}")


    def get_info_fonk(self):
        self.ui.push_sil.setEnabled(True)
        self.ui.push_guncelle.setEnabled(True)
        self.cell_changed_fonk()



    def cell_changed_fonk(self):
        row_sec=int(self.ui.tableWidget.currentRow())
        if(row_sec>=0):
            self.ui.line_kullanici_id.setText(str(self.ui.tableWidget.item(row_sec,0).text()))
            self.ui.line_ad.setText(str(self.ui.tableWidget.item(row_sec,1).text()))
            self.ui.line_soyad.setText(str(self.ui.tableWidget.item(row_sec,2).text()))
            self.ui.line_TC.setText(str(self.ui.tableWidget.item(row_sec,3).text()))
            self.ui.line_dogum.setText(str(self.ui.tableWidget.item(row_sec,4).text()))
            self.ui.line_adres.setText(str(self.ui.tableWidget.item(row_sec,5).text()))
            self.ui.line_telefon.setText(str(self.ui.tableWidget.item(row_sec,6).text()))
            self.ui.line_eposta.setText(str(self.ui.tableWidget.item(row_sec,7).text()))


    def mesaj(self, metin):
        self.messagebox = QMessageBox()
        self.messagebox.setText(metin)
        self.messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        self.messagebox.setDefaultButton(QMessageBox.Cancel)
        return self.messagebox.exec()

    def ara_fonk(self):
        self.mainWindow.mycursor.execute(f"SELECT * FROM {self.mainWindow.target_db}.dbo.uyeler WHERE 1 = 1")
        self.table_doldur()

    def table_doldur(self):
        araTable = [arama for arama in self.mainWindow.mycursor.fetchall()]
        self.ui.tableWidget.setRowCount(len(araTable))
        if(araTable!=[]):
            for x in range(len(araTable)):
                item_uye_id = QTableWidgetItem(str(araTable[x][0]))
                item_ad_u = QTableWidgetItem(str(araTable[x][1]))
                item_soyad = QTableWidgetItem(str(araTable[x][2]))
                item_tc_u = QTableWidgetItem(str(araTable[x][3]))
                item_dogum = QTableWidgetItem(str(araTable[x][5]))
                item_ad_ures = QTableWidgetItem(str(araTable[x][6]))
                item_telefon = QTableWidgetItem(str(araTable[x][7]))
                item_eposta = QTableWidgetItem(str(araTable[x][4]))
                self.ui.tableWidget.setItem(x,0, item_uye_id)
                self.ui.tableWidget.setItem(x,1, item_ad_u)
                self.ui.tableWidget.setItem(x,2, item_soyad)
                self.ui.tableWidget.setItem(x,3, item_tc_u)
                self.ui.tableWidget.setItem(x,4, item_eposta)
                self.ui.tableWidget.setItem(x,5, item_dogum)
                self.ui.tableWidget.setItem(x,6, item_ad_ures)
                self.ui.tableWidget.setItem(x,7, item_telefon)


class bul(QWidget):
    def __init__(self, uyeler):
        super().__init__()
        self.ui = Ui_bul()
        self.ui.setupUi(self)
        self.uyeler = uyeler
        self.ui.push_bul.clicked.connect(self.arama_fonk)

    def arama_fonk(self):
        self.ad = self.ui.line_ad.text()
        self.soyad = self.ui.line_soyad.text()
        self.tc = self.ui.line_TC.text()
        self.dogum = self.ui.line_dogum.text()
        self.telefon = self.ui.line_telefon.text()
        self.e_posta = self.ui.line_eposta.text()

        query = f"SELECT * FROM {self.uyeler.mainWindow.target_db}.dbo.uyeler WHERE 1 = 1"

        params = []

        if self.ad:
            query += " AND ad LIKE ?"
            params.append(f"%{self.ad}%")
        if self.soyad:
            query += " AND soyad LIKE ?"
            params.append(f"%{self.soyad}%")
        if self.tc:
            query += " AND tc LIKE ?"
            params.append(f"%{self.tc}%")
        if self.dogum:
            query += " AND dogum_tarihi LIKE ?"
            params.append(f"%{self.dogum}%")
        if self.telefon:
            query += " AND telefon LIKE ?"
            params.append(f"%{self.telefon}%")
        if self.e_posta:
            query += " AND e_posta LIKE ?"
            params.append(f"%{self.e_posta}%")

        self.uyeler.mainWindow.mycursor.execute(query, params)

        self.uyeler.table_doldur()


class egitmenler(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_egitmenler()
        self.ui.setupUi(self)
        self.Qwidget = QWidget
        self.mainWindow = mainWindow
        self.ui.tableWidget.setHorizontalHeaderLabels(["Id","Eğitmen Ad","TC No","Doğum Tarihi","Cinsiyet","Adres","Eğitim","Tecrübe","Çalışma Saatleri","Sağlık Durumu"])
        self.ui.tableWidget.setColumnWidth(0, 70)
        self.ui.tableWidget.setColumnWidth(1, 140)
        self.ui.tableWidget.setColumnWidth(2, 105)
        self.ui.tableWidget.setColumnWidth(3, 105)
        self.ui.tableWidget.setColumnWidth(4, 70)
        self.ui.tableWidget.setColumnWidth(5, 140)
        self.ui.tableWidget.setColumnWidth(6, 100)
        self.ui.tableWidget.setColumnWidth(7, 70)
        self.ui.tableWidget.setColumnWidth(8, 95)
        self.ui.tableWidget.setColumnWidth(9, 95)
        self.ui.push_sil.setEnabled(False)
        self.ui.push_guncelle.setEnabled(False)
        self.ui.mycursor = self.mainWindow.mycursor

    


        query = f"SELECT * FROM {self.mainWindow.target_db}..egitmenler"
        self.mainWindow.mycursor.execute(query)
        self.table_doldur()

        self.ui.push_ara.clicked.connect(self.open_ara_egitmen)
        self.ui.push_yeni.clicked.connect(self.yeni_fonk)
        self.ui.push_sil.clicked.connect(self.sil_fonk)
        self.ui.push_guncelle.clicked.connect(self.guncelle_fonk)
        self.ui.push_kaydet.clicked.connect(self.kaydet_fonk)
        self.ui.tableWidget.doubleClicked.connect(self.get_info_fonk)

    


    def open_ara_egitmen(self):
        self.k = ara_egitmen(self)
        self.k.show()


    def yeni_fonk(self):
        self.ui.line_egitmen_id.setText("")
        self.ui.line_egitmen_ad.setText("")
        self.ui.line_egitmen_tc.setText("")
        self.ui.line_dogum.setText("")
        self.ui.line_cinsiyet.setText("")
        self.ui.line_adres.setText("")
        self.ui.line_egitim_derecesi.setText("")
        self.ui.line_tecrube.setText("")
        self.ui.line_calisma_saatleri.setText("")
        self.ui.radioraporlu.setChecked(False)
        self.ui.radiosaglikli.setChecked(False)
        self.ui.push_sil.setEnabled(False)
        self.ui.push_guncelle.setEnabled(False)



    def sil_fonk(self):
        result = self.mesaj("Silmek İstediğinize Emin Misiniz?")
        if result == QMessageBox.Yes:
            id = int(self.ui.line_egitmen_id.text())
            table_name = "egitmenler"  

            
            delete_query = f"DELETE FROM {self.mainWindow.target_db}.dbo.{table_name} WHERE (id = ?);"

            self.mainWindow.mycursor.execute(delete_query, (id,))
            self.ui.push_sil.setEnabled(False)
            self.mainWindow.dbConn.commit()
            self.ara_fonk()
        else:
            pass

    def guncelle_fonk(self):
        egitmen_id = int(self.ui.line_egitmen_id.text())
        egitmen_ad = self.ui.line_egitmen_ad.text()
        egitmen_tc = self.ui.line_egitmen_tc.text()
        dogum = self.ui.line_dogum.text()
        cinsiyet = self.ui.line_cinsiyet.text()
        adres = self.ui.line_adres.text()
        egitim_derecesi = self.ui.line_egitim_derecesi.text()
        tecrube = self.ui.line_tecrube.text()
        calisma_saatleri = self.ui.line_calisma_saatleri.text()
        saglik_durumu = 1 if self.ui.radiosaglikli.isChecked() else 0

        sorgu = f"""
            UPDATE {self.mainWindow.target_db}.dbo.egitmenler SET
            egitmen_ad = ?,
            egitmen_tc = ?,
            dogum = ?,
            cinsiyet = ?,
            adres = ?,
            egitim_derecesi = ?,
            tecrube = ?,
            calisma_saatleri = ?,
            saglik_durumu = ?
            WHERE id = ?;
        """

        degerler = (egitmen_ad, egitmen_tc, dogum, cinsiyet, adres, egitim_derecesi, tecrube, calisma_saatleri, saglik_durumu, egitmen_id)

        self.mainWindow.mycursor.execute(sorgu, degerler)
        self.mainWindow.dbConn.commit()
        self.ara_fonk()


    def kaydet_fonk(self):
        if self.ui.line_egitmen_id.text() != "":
            result = self.mesaj("Bu kayıt zaten mevcut. Güncellemek ister misiniz?")
            if result == QMessageBox.Yes:
                self.guncelle_fonk()
            else:
                pass
        else:
            saglik_durumu = 1 if self.ui.radiosaglikli.isChecked() else 0
            sqlBaglan = """
                INSERT INTO egitmenler
                (egitmen_ad, egitmen_tc, dogum, cinsiyet, adres, egitim_derecesi, tecrube, calisma_saatleri, saglik_durumu)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            self.veri = (
                self.ui.line_egitmen_ad.text(),
                self.ui.line_egitmen_tc.text(),
                self.ui.line_dogum.text(),
                self.ui.line_cinsiyet.text(),
                self.ui.line_adres.text(),
                self.ui.line_egitim_derecesi.text(),
                self.ui.line_tecrube.text(),
                self.ui.line_calisma_saatleri.text(),
                saglik_durumu
            )

            self.mainWindow.mycursor.execute(sqlBaglan, self.veri)
            self.mainWindow.dbConn.commit()


    def get_info_fonk(self):
        self.ui.push_sil.setEnabled(True)
        self.ui.push_guncelle.setEnabled(True)
        self.cell_changed_fonk()





    def cell_changed_fonk(self):
        row_sec=int(self.ui.tableWidget.currentRow())
        if(row_sec>=0):
            self.ui.line_egitmen_id.setText(str(self.ui.tableWidget.item(row_sec,0).text()))
            self.ui.line_egitmen_ad.setText(str(self.ui.tableWidget.item(row_sec,1).text()))
            self.ui.line_egitmen_tc.setText(str(self.ui.tableWidget.item(row_sec,2).text()))
            self.ui.line_dogum.setText(str(self.ui.tableWidget.item(row_sec,3).text()))
            self.ui.line_cinsiyet.setText(str(self.ui.tableWidget.item(row_sec,4).text()))
            self.ui.line_adres.setText(str(self.ui.tableWidget.item(row_sec,5).text()))
            self.ui.line_egitim_derecesi.setText(str(self.ui.tableWidget.item(row_sec,6).text()))
            self.ui.line_tecrube.setText(str(self.ui.tableWidget.item(row_sec,7).text()))
            self.ui.line_calisma_saatleri.setText(str(self.ui.tableWidget.item(row_sec,8).text()))
            self.ui.push_sil.setEnabled(True)
            self.ui.push_guncelle.setEnabled(True)



    def mesaj(self, metin):
        self.messagebox = QMessageBox()
        self.messagebox.setText(metin)
        self.messagebox.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        self.messagebox.setDefaultButton(QMessageBox.Cancel)
        return self.messagebox.exec()

    def ara_fonk(self):
        query = "SELECT * FROM egitmenler;"
        self.mainWindow.mycursor.execute(query)
        self.table_doldur()


    def table_doldur(self):
        araTable = [arama for arama in self.mainWindow.mycursor.fetchall()]
        self.ui.tableWidget.setRowCount(len(araTable))
        
        for x in range(len(araTable)):
            item_egitmen_id = QTableWidgetItem(str(araTable[x][0]))
            item_egitmen_ad = QTableWidgetItem(str(araTable[x][1]))
            item_egitmen_tc = QTableWidgetItem(str(araTable[x][2]))
            item_dogum = QTableWidgetItem(str(araTable[x][3]))
            item_cinsiyet = QTableWidgetItem(str(araTable[x][4]))
            item_ad_ures = QTableWidgetItem(str(araTable[x][5]))
            item_egitim_derecesi = QTableWidgetItem(str(araTable[x][6]))
            item_tecrube = QTableWidgetItem(str(araTable[x][7]))
            item_calisma_saatleri = QTableWidgetItem(str(araTable[x][8]))  
            item_saglik_durumu = QTableWidgetItem(str(araTable[x][9]))                                                  
            self.ui.tableWidget.setItem(x, 0, item_egitmen_id)
            self.ui.tableWidget.setItem(x, 1, item_egitmen_ad)
            self.ui.tableWidget.setItem(x, 2, item_egitmen_tc)
            self.ui.tableWidget.setItem(x, 3, item_dogum)
            self.ui.tableWidget.setItem(x, 4, item_cinsiyet)
            self.ui.tableWidget.setItem(x, 5, item_ad_ures)
            self.ui.tableWidget.setItem(x, 6, item_egitim_derecesi)
            self.ui.tableWidget.setItem(x, 7, item_tecrube)
            self.ui.tableWidget.setItem(x, 8, item_calisma_saatleri)
            self.ui.tableWidget.setItem(x, 9, item_saglik_durumu)



class ara_egitmen(QWidget):
    def __init__(self, egitmenler):
        super().__init__()
        self.ui = Ui_araegitmen()
        self.ui.setupUi(self)
        self.egitmenler = egitmenler
        self.ui.push_bul.clicked.connect(self.arama_fonk)

    def arama_fonk(self):
        self.egitmen_ad = self.ui.line_egitmen_ad.text()
        self.egitmen_tc = self.ui.line_egitmen_tc.text()
        self.dogum = self.ui.line_dogum.text()
        self.cinsiyet = self.ui.line_cinsiyet.text()
        self.tecrube = self.ui.line_tecrube.text()
        self.durum = self.ui.line_saglik.text()


        query = f"SELECT * FROM {self.egitmenler.mainWindow.target_db}.dbo.egitmenler WHERE 1=1"
        params = []

        if self.egitmen_ad:
            query += " AND egitmen_ad LIKE ?"
            params.append(f"%{self.egitmen_ad}%")
        if self.egitmen_tc:
            query += " AND egitmen_tc LIKE ?"
            params.append(f"%{self.egitmen_tc}%")
        if self.dogum:
            query += " AND dogum LIKE ?"
            params.append(f"%{self.dogum}%")
        if self.cinsiyet:
            query += " AND cinsiyet LIKE ?"
            params.append(f"%{self.cinsiyet}%")
        if self.tecrube:
            query += " AND tecrube LIKE ?"
            params.append(f"%{self.tecrube}%")
        if self.durum:
            query += " AND saglik_durumu LIKE ?"
            params.append(f"%{self.durum}%")

        self.egitmenler.mainWindow.mycursor.execute(query, params)
        self.egitmenler.table_doldur()


class planlama(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_planlama()
        self.ui.setupUi(self)
        self.Qwidget = QWidget
        self.mainWindow = mainWindow
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID","Ad","Soyad","TC","Doğum Yılı"])
        self.ui.tableWidget.setColumnWidth(0, 40)
        self.ui.tableWidget.setColumnWidth(1, 160)
        self.ui.tableWidget.setColumnWidth(2, 105)
        self.ui.tableWidget.setColumnWidth(3, 90)
        self.ui.tableWidget.setColumnWidth(4, 70)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["ID", "Ad","Tecrübe","TC Kimlik","Doğum Yılı"])
        self.ui.tableWidget_2.setColumnWidth(0, 40)
        self.ui.tableWidget_2.setColumnWidth(1, 125)
        self.ui.tableWidget_2.setColumnWidth(2, 125)
        self.ui.tableWidget_2.setColumnWidth(3, 100)
        self.ui.tableWidget_2.setColumnWidth(4, 80)
        self.data_cek()
        self.ui.tableWidget.doubleClicked.connect(self.label_doldur)
        self.ui.tableWidget_2.doubleClicked.connect(self.label_doldur)
        self.ui.push_planla.clicked.connect(self.rent)
        self.ui.date_baslangic.setDisplayFormat("yyyy-MM-dd")
        self.ui.date_bitis.setDisplayFormat("yyyy-MM-dd")

        today = QDate.currentDate()
        
        self.ui.date_baslangic.setDate(today)
        self.ui.date_bitis.setDate(today)

    def check_if_car_is_rented(self):
        query = """
            SELECT COUNT(*)
            FROM {db}.planlama
            WHERE konut_id = ? AND 
                ((baslangic_tarihi BETWEEN ? AND ? OR bitis_tarihi BETWEEN ? AND ?) OR
                (baslangic_tarihi <= ? AND bitis_tarihi >= ?))
        """

        params = (
            self.ui.line_konut_id.text(),
            self.ui.date_baslangic.date().toString("yyyy-MM-dd"),
            self.ui.date_bitis.date().toString("yyyy-MM-dd"),
            self.ui.date_baslangic.date().toString("yyyy-MM-dd"),
            self.ui.date_bitis.date().toString("yyyy-MM-dd"),
            self.ui.date_baslangic.date().toString("yyyy-MM-dd"),
            self.ui.date_bitis.date().toString("yyyy-MM-dd")
        )

        self.mainWindow.mycursor.execute(query.format(db=self.mainWindow.target_db), params)
        result = self.mainWindow.mycursor.fetchone()

        if result and result[0] > 0:
            return True 
        else:
            return False  

            
    def data_cek(self):

        musteri_query = f"SELECT * FROM [{self.mainWindow.target_db}].[dbo].[uyeler];"
        self.mainWindow.mycursor.execute(musteri_query)
        self.uye_data = [arama for arama in self.mainWindow.mycursor.fetchall()]
        self.table_doldur()

        
        konut_query = f"SELECT * FROM [{self.mainWindow.target_db}].[dbo].[egitmenler];"
        self.mainWindow.mycursor.execute(konut_query)
        self.egitmen_data = [arama for arama in self.mainWindow.mycursor.fetchall()]
        self.table_doldur2()


    def table_doldur(self):
        self.ui.tableWidget.setRowCount(len(self.uye_data))
        if self.uye_data != []:
            for x in range(len(self.uye_data)):
                item_uye_id = QTableWidgetItem(str(self.uye_data[x][0]))
                item_ad_u = QTableWidgetItem(str(self.uye_data[x][1]))
                item_soyad = QTableWidgetItem(str(self.uye_data[x][2]))
                item_tc_u = QTableWidgetItem(str(self.uye_data[x][3]))
                item_dogum_u = QTableWidgetItem(str(self.uye_data[x][4]))
                self.ui.tableWidget.setItem(x, 0, item_uye_id)
                self.ui.tableWidget.setItem(x, 1, item_ad_u)
                self.ui.tableWidget.setItem(x, 2, item_soyad)
                self.ui.tableWidget.setItem(x, 3, item_tc_u)
                self.ui.tableWidget.setItem(x, 4, item_dogum_u)

    def table_doldur2(self):
        
        egitmen_saglikli = [egitmen for egitmen in self.egitmen_data if egitmen[9] == 1]
        self.ui.tableWidget_2.setRowCount(len(egitmen_saglikli))
        
       
        if egitmen_saglikli:
            for x in range(len(egitmen_saglikli)):
                item_egitmen_id = QTableWidgetItem(str(egitmen_saglikli[x][0]))  
                item_ad = QTableWidgetItem(str(egitmen_saglikli[x][1]))          
                item_tecrube = QTableWidgetItem(str(egitmen_saglikli[x][7]))     
                item_tc = QTableWidgetItem(str(egitmen_saglikli[x][2]))          
                item_dogum = QTableWidgetItem(str(egitmen_saglikli[x][3]))       

                self.ui.tableWidget_2.setItem(x, 0, item_egitmen_id)
                self.ui.tableWidget_2.setItem(x, 1, item_ad)
                self.ui.tableWidget_2.setItem(x, 2, item_tecrube)
                self.ui.tableWidget_2.setItem(x, 3, item_tc)
                self.ui.tableWidget_2.setItem(x, 4, item_dogum)


    def fill_user_fields(self,row):
        self.ui.line_uye_id.setText(self.get_cell_value(self.ui.tableWidget, row, 0))
        self.ui.line_ad_u.setText(self.get_cell_value(self.ui.tableWidget, row, 1))
        self.ui.line_soyad.setText(self.get_cell_value(self.ui.tableWidget, row, 2))
        self.ui.line_tc_u.setText(self.get_cell_value(self.ui.tableWidget, row, 3))
        self.ui.line_dogum_u.setText(self.get_cell_value(self.ui.tableWidget, row, 4))

    def fill_car_fields(self,row):

        self.ui.line_egitmen_id.setText(self.get_cell_value(self.ui.tableWidget_2, row, 0))
        self.ui.line_ad.setText(self.get_cell_value(self.ui.tableWidget_2, row, 1))
        self.ui.line_tecrube.setText(self.get_cell_value(self.ui.tableWidget_2, row, 2))
        self.ui.line_tc.setText(self.get_cell_value(self.ui.tableWidget_2, row, 3))
        self.ui.line_dogum.setText(self.get_cell_value(self.ui.tableWidget_2, row, 4))


    def get_cell_value(self,table, row, column):
        item = table.item(row, column)
        return item.text() if item is not None else ""


    def label_doldur(self):
        current_user_row = self.ui.tableWidget.currentRow()
        current_car_row = self.ui.tableWidget_2.currentRow()

        self.fill_user_fields(current_user_row)
        self.fill_car_fields(current_car_row)

    def clear_user_fields(self):
        self.ui.line_uye_id.setText("")
        self.ui.line_ad_u.setText("")
        self.ui.line_soyad.setText("")
        self.ui.line_tc_u.setText("")
        self.ui.line_dogum_u.setText("")


    def clear_egitmen_fields(self):
        self.ui.line_egitmen_id.setText("")
        self.ui.line_ad.setText("")
        self.ui.line_tecrube.setText("")
        self.ui.line_tc.setText("")
        self.ui.line_dogum.setText("")



    def rent(self):
        sqlEklemeKomut = f"""
            INSERT INTO {self.mainWindow.target_db}.dbo.planlama
            (egitmen_id, uye_id, ad_u, ad_e, tecrube, baslangic_tarihi, bitis_tarihi)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """

        veri = (
            self.ui.line_egitmen_id.text(),
            self.ui.line_uye_id.text(),
            self.ui.line_ad_u.text(),
            self.ui.line_ad.text(),
            self.ui.line_tecrube.text(),
            self.ui.date_baslangic.date().toString("yyyy-MM-dd"),
            self.ui.date_bitis.date().toString("yyyy-MM-dd")
            )

        try:
            self.mainWindow.mycursor.execute(sqlEklemeKomut, veri)
            self.mainWindow.dbConn.commit()
            QMessageBox.information(None, "Bilgi", "planlama işlemi başarılı.")
            self.data_cek()
            self.clear_user_fields()
            self.clear_egitmen_fields()
        except Exception as e:
            print("Hata:", e)
            QMessageBox.critical(None, "Hata", "planlama işlemi başarısız oldu. Hata ayrıntıları için konsolu kontrol edin.")


class plandakiler(QWidget):

    def __init__(self, mainWindow):
        super().__init__()
        self.ui = Ui_plandakiler()
        self.ui.setupUi(self)
        self.Qwidget = QWidget
        self.mainWindow = mainWindow
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID","Eğitmen Adı","Üye Adı","Bitiş Tarihi","Çalışma Saatleri"])
        self.ui.tableWidget.setColumnWidth(0, 100)
        self.ui.tableWidget.setColumnWidth(1, 220)
        self.ui.tableWidget.setColumnWidth(2, 220)
        self.ui.tableWidget.setColumnWidth(3, 200)
        self.ui.tableWidget.setColumnWidth(4, 200)
        self.data_cek()
        self.ui.push_bitir.clicked.connect(self.kirayi_bitir)
        self.ui.tableWidget.doubleClicked.connect(self.fill_cell_field)



    def label_doldur(self):
        current_user_row = self.ui.tableWidget.currentRow()

        self.fill_cell_field(current_user_row)


    def data_cek(self):
        query = """
            SELECT k.id, a.egitmen_ad, m.ad, k.bitis_tarihi, a.calisma_saatleri
            FROM [{}].dbo.planlama as k
            INNER JOIN [{}].dbo.uyeler as m ON m.id = k.uye_id
            INNER JOIN [{}].dbo.egitmenler as a ON k.egitmen_id = a.id
        """

        formatted_query = query.format(self.mainWindow.target_db, self.mainWindow.target_db, self.mainWindow.target_db)

        try:
            self.mainWindow.mycursor.execute(formatted_query)
            self.planlama_data = [arama for arama in self.mainWindow.mycursor.fetchall()]
            self.table_doldur()
        except pypyodbc.Error as e:
            print(f"Hata: {e}")
            


    def get_cell_value(self,table, row, column):
        item = table.item(row, column)
        return item.text() if item is not None else ""

    def table_doldur(self):
        self.ui.tableWidget.setRowCount(len(self.planlama_data))
        if self.planlama_data != []:
            for x in range(len(self.planlama_data)):
                item_uye_id = QTableWidgetItem(str(self.planlama_data[x][0]))
                item_marka = QTableWidgetItem(str(self.planlama_data[x][1]))
                item_musteri = QTableWidgetItem(str(self.planlama_data[x][2]))
                item_bitis = QTableWidgetItem(str(self.planlama_data[x][3]))
                item_kira_gunluk = QTableWidgetItem(str(self.planlama_data[x][4]))
                self.ui.tableWidget.setItem(x, 0, item_uye_id)
                self.ui.tableWidget.setItem(x, 1, item_marka)
                self.ui.tableWidget.setItem(x, 2, item_musteri)
                self.ui.tableWidget.setItem(x, 3, item_bitis)
                self.ui.tableWidget.setItem(x, 4, item_kira_gunluk)

    def kirayı_oto_bitir(self):
        today = QDate.currentDate().toString("yyyy-MM-dd")
        try:
            query = f"SELECT id FROM {self.mainWindow.target_db}.planlama WHERE bitis_tarihi = ?"
            self.mainWindow.mycursor.execute(query, (today,))
            id = self.mainWindow.mycursor.fetchone()

            if id is not None:
                
                self.mainWindow.mycursor.execute(f"DELETE FROM {self.mainWindow.target_db}.planlama WHERE id = ?;", (id[0],))
                self.mainWindow.dbConn.commit()
                self.data_cek()
                self.clear_cell_field()
                QMessageBox.information(None, "Bilgi", "planlama işlemi başarıyla sonlandırıldı.")
            else:
                QMessageBox.critical(None, "Hata", "Bugün için planlama bitirilecek araç bulunamadı.")
        except Exception as e:
            print("Hata:", e)
            QMessageBox.critical(None, "Hata", "planlama sonlandırma işlemi başarısız oldu. Hata ayrıntıları için konsolu kontrol edin.")


    def kirayi_bitir(self):
        id = self.ui.line_plan_id.text()

        query = f"DELETE FROM {self.mainWindow.target_db}.dbo.planlama WHERE (id = ?)"

        try:
            self.mainWindow.mycursor.execute(query, (id,))
            self.mainWindow.dbConn.commit()
            self.data_cek()
            self.clear_cell_field()
            print("Kira başarıyla sonlandırıldı.")
        except Exception as e:
            print(f"Hata: {e}")


    def fill_cell_field(self):
        current_row = self.ui.tableWidget.currentRow()
        self.ui.line_plan_id.setText(self.get_cell_value(self.ui.tableWidget, current_row, 0))
        self.ui.line_egitmen_ad.setText(self.get_cell_value(self.ui.tableWidget, current_row, 1))
        self.ui.line_uye_ad.setText(self.get_cell_value(self.ui.tableWidget, current_row, 2))
        self.ui.line_bitis_tarihi.setText(self.get_cell_value(self.ui.tableWidget, current_row, 3))
        self.ui.line_calisma_saatleri.setText(self.get_cell_value(self.ui.tableWidget, current_row, 4))

    def clear_cell_field(self):
        self.ui.line_plan_id.setText("")
        self.ui.line_egitmen_ad.setText("")
        self.ui.line_uye_ad.setText("")
        self.ui.line_bitis_tarihi.setText("")
        self.ui.line_calisma_saatleri.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = mainWindow()
    widget.show()
    sys.exit(app.exec())
