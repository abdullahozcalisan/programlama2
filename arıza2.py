# -*- coding: utf-8 -*-

import sqlite3
from tkinter import messagebox
import os.path
i=11
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "blogKayitFormu.db")
print (db_path)

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ArizaKayit(object):
    def setupUi(self, ArizaKayit):
        ArizaKayit.setObjectName(_fromUtf8("ArizaKayit"))
        ArizaKayit.resize(264, 291)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("tel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ArizaKayit.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(ArizaKayit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 46, 13))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 46, 13))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 80, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 130, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 180, 113, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 220, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        ArizaKayit.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ArizaKayit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 264, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        ArizaKayit.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ArizaKayit)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ArizaKayit.setStatusBar(self.statusbar)

        

        self.retranslateUi(ArizaKayit)
        QtCore.QMetaObject.connectSlotsByName(ArizaKayit)

    def retranslateUi(self, ArizaKayit):
        ArizaKayit.setWindowTitle(_translate("ArizaKayit", "Arıza Kayıt", None))
        self.label.setText(_translate("ArizaKayit", "Ad Soyad:", None))
        self.label_2.setText(_translate("ArizaKayit", "Telefon", None))
        self.label_3.setText(_translate("ArizaKayit", "Arıza:", None))
        self.label_4.setText(_translate("ArizaKayit", "İşlem tutarı:", None))
        self.pushButton.setText(_translate("ArizaKayit", "Kaydet", None))
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"),self.kaydet)
        
    def kaydet(self):
        con=sqlite3.connect("vt.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("INSERT INTO ariza_kayit (ad_soyad,telefon,ariza,tutar) VALUES (?,?,?,?)",(self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text()))
        con.commit()
        con.close()
        messagebox.showinfo("kayıt form", "Kaydınız tamamlandı")
    

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ArizaKayit = QtGui.QMainWindow()
    ui = Ui_ArizaKayit()
    ui.setupUi(ArizaKayit)
    ArizaKayit.show()
    sys.exit(app.exec_())

