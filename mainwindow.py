#C.Said BERK
#Necati EROL
#CRYPTURK

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import random
import time


class Kir():
    def modCek(hash):  # Modu tespit edip gönderir.
        if (hash != ""):
            if (hash[2] == "."):#Noktanın Konumuna Göre Mod Belirlenir.
                return "oe"
            else:
                return "oa"
        else:
            print("Lütfen bir hash giriniz!")

    def oeSade(hash):  # oe modunu sadeleştirir.
        dosyaoe = open('parcasade.txt', 'w') #Parcasade dosyasına yazmaya hazırlanır.

        parcailk = hash[16:len(hash) - 17]
        parcasade = parcailk[:int(len(parcailk) / 2)]  #Hash'ı Fazlalıklarından Ayırır.

        dosyaoe.write(parcasade)#İlkel Şifreyi Döner.
        dosyaoe.close()
        Kir.decode()#Decode fonksiyonunu tetikler

    def oaSade(hash):  # oa modunu sadeleştirir.
        dosyaoa = open("parcasade.txt", "w")#Parcasade dosyasına yazmaya hazırlanır.
        j = 0#Döngü Değişkeni
        nt = 0  # ilk nokta tespit edici
        for i in hash:  # noktayı bulana dek ara
            if (i == "." and nt == 0):  # ilk noktayı bulursan
                parcason = hash[:j - 2]  # ilk indexten itibaren nokta indeksine kadar hepsini parcason isimli degiskene ata(son iki indeksi alma).#Böylelikle Fazlalıkları Ayıkla,İlkel Şifreyi Elde Et.
                break  # döngüyü durdur

            j = j + 1

        dosyaoa.write(parcason)
        dosyaoa.close()
        Kir.decode()#Decode fonksiyonunu tetikler

    def decode():  # gelen sade hash'in sayisal verilerini ayıklar.
        dosyaYaz = open('decrypt.txt', 'w')
        dosyaOku = open('parcasade.txt', 'r')
        parcasade = dosyaOku.read()#İlkel Sifreyi Elde Eder.

        j = 0  # döngü index degiskeni
        tc = 0  # ilk durak tespit degiskeni

        for i in parcasade:
            if ((i == "T" or i == "C")):  # durak tespti
                if (tc == 0):  # ilk durak tespiti
                    dosyaYaz.write(parcasade[j - 2] + parcasade[j - 1])  # ilk durağın solundaki iki sayıyı yazıyor.
                    tc = 1  # ilk duraktan sonra degiskeni degistirerek ilk duragı isaretliyor.
                try:
                    dosyaYaz.write(parcasade[j + 3] + parcasade[j + 4])  # durakların iki index sağındaki harfleri dosyaya yazıyor.bkz:pdf 5.Sayfa,3.Adım(Tekrar Eden Değerleri Almaz,Sadece Anlamlı Kısımlar Çekilir.)
                except:
                    pass
            j = j + 1

        dosyaOku.close()
        dosyaYaz.close()
        Eslestir.sayidanharf()#İLkel Şifreyi Harflerle Eşleştiren Fonksiyonu Tetikliyor.


class Eslestir():
    osman_tablo = {"21": "a",  # boslugu karakter olarak goruyor.
                   "Q2": "b",
                   "Q6": "c",
                   "Q7": "ç",
                   "10": "d",
                   "Q1": "e",
                   "23": "f",
                   "26": "g",
                   "22": "ğ",
                   "Q8": "h",
                   "37": "ı",
                   "38": "i",
                   "97": "j",
                   "24": "k",
                   "28": "l",
                   "29": "m",
                   "27": "n",
                   "39": "o",
                   "40": "ö",
                   "Q3": "p",
                   "12": "r",
                   "Q5": "s",
                   "16": "ş",
                   "Q4": "t",
                   "41": "u",
                   "42": "ü",
                   "31": "v",
                   "36": "y",
                   "11": "z",
                   "T": "T",
                   "C": "C",
                   "14": " ",
                   "70": ".",
                   "71": ",",
                   "72": "!",
                   "73": "?",
                   "74": ":",
                   "75": ";",
                   "76": "'",
                   "77":"/",
                   "78":"@",
                   "79":"(",
                   "80":")",
                   "81":"{",
                   "82":"}",
                   "83":"+",
                   "84":"-",
                   "85":"*",
                   "86":"%",
                   "87":"₺",
                   "88":"$",
                   "89":"€",
                   "90":"'",
                   "91":"â",
                   "92":">",
                   "93":"<",
                   "94":'"',
                   "50": "0",
                   "51": "1",
                   "52": "2",
                   "53": "3",
                   "54": "4",
                   "55": "5",
                   "56": "6",
                   "57": "7",
                   "58": "8",
                   "59": "9",
                   "No":" \n "

                   }  # latin - osmanlı alfabe karşılığı

    def sayidanharf():
        sayisalTM = open('decrypt.txt', 'r').read()  # sayisalTM = Sayısal Temiz Metin
        j = 0  # döngü index degiskeni
        sozelTM = list()  # sozelTM = Sözel Temiz Metin
        for i in sayisalTM:
            if (j % 2 == 0):
                sozelTM.append(Eslestir.osman_tablo[sayisalTM[j] + sayisalTM[j + 1]])#sayilari harflerle eslestirip sozelTM listesine sırasıyla ekliyoruz
            j = j + 1  # index değişkenini arttır.

            temiz_metin = ''.join(map(str, sozelTM))  # sozelTM listemizi stringe ceviriyoruz.

        dosyaYaz = open("duz_metin.txt", 'w')
        dosyaYaz.write(temiz_metin)#Kırılmış Şifreyi Dosyaya Yazıyoruz.

#-----------------------------------------Encryption

class ModAyar():

    def modDegis(encryptionMod):  # sifreleme modunu kelime uzunluguna gore belirler
        dosya = open('mod.txt', 'w')
        dosya.write(encryptionMod)

    def modCek():  # sifreleme modunu her cagrildiginda geri dondurur.
        dosya = open('mod.txt', 'r')
        for satir in dosya:
            return satir


class Sezar():
    latin_tablo = {"a": "21",
                   "b": "Q2",
                   "c": "Q6",
                   "ç": "Q7",
                   "d": 10,
                   "e": "Q1",
                   "f": 23,
                   "g": 26,
                   "ğ": 22,
                   "h": "Q8",
                   "ı": 37,
                   "i": 38,
                   "j": 97,
                   "k": 24,
                   "l": 28,
                   "m": 29,
                   "n": 27,
                   "o": 39,
                   "ö": 40,
                   "p": "Q3",
                   "r": 12,
                   "s": "Q5",
                   "ş": 16,
                   "t": "Q4",
                   "u": 41,
                   "ü": 42,
                   "v": 31,
                   "y": 36,
                   "z": 11,
                   "T": "T",
                   "C": "C",
                   " ": 1453,
                   ".": 70,
                   ",": 71,
                   "!": 72,
                   "?": 73,
                   ":": 74,
                   ";": 75,
                   "'": 76,
                   "/":77,
                   "0": 50,
                   "1": 51,
                   "2": 52,
                   "3": 53,
                   "4": 54,
                   "5": 55,
                   "6": 56,
                   "7": 57,
                   "8": 58,
                   "9": 59,
                   "@": 78,
                   "(": 79,
                   ")": 80,
                   "{": 81,
                   "}": 82,
                   "+": 83,
                   "-": 84,
                   "*": 85,
                   "%": 86,
                   "₺": 87,
                   "$": 88,
                   "€": 89,
                   " ' ": 90,
                   "â": 91,
                   ">": 92,
                   "<": 93,
                   '"':94

                   }  # latin - osmanlı alfabe karşılığı

    def latinDeger(harf):  # hata denetleme fonksiyonu.
        if (len(harf) != 1):
            return "lütfen bir harf giriniz!"
        else:
            return Sezar.latin_tablo.get(harf)


class Incele():
    basla = 0
    bitir = 1
    harfler = list()

    def durak():
        durak = ["T", "C"] #T,C DURAKLARI KELİME SETLERİ ARASINA YERLEŞİR.DAHA FAZLA DURAK EKLEYEREK KAOSU ARTTIRMAK MÜMKÜNDÜR.BKZ:PDF SAYFA4,KELİME SETLERİ
        durakEkle = random.sample(durak, 1)  # durak aralarına rastgele t ya da c harflerinden birini seçip ekler.
        return durakEkle

    def parcala():  # STRİNGİ PARÇALAR,LİSTEYE ELEMAN OLARAK VEREREK ITERE EDİLEBİLİR VAZİYETE SOKAR.
        Incele.harfler = list()  # GRAFİKSEL ARAYÜZDE OUTPUTUN ÜST ÜSTE BİNMEMESİ AMACIYLA LİSTEYİ SIFIRLIYORUZ.
        for i in range(0, len(csb)):
            Incele.harfler.append(csb[Incele.basla + i:Incele.bitir + i])  # harfi al
            Incele.harfler = Incele.harfler + Incele.durak()  # durak ekle

        return Incele.harfler#Sayısal Karşılık + Durak Listesini Döner.


class Sifre():
    sifre_liste = list()

    asal_liste = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]#İşlevsizdir.Karışıklık Amaçlı Eklenmiştir.

    sayı_liste = [10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39,
                  40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72,
                  74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99]#İşlevsizdir.Karışıklık Amaçlı Eklenmiştir.

    def sayisal():
        Sifre.sifre_liste = list()
        for i in Incele.parcala():
            Sifre.sifre_liste.append(Sezar.latinDeger(i))  # harfleri sayısal değerlerine çeviren fonksiyonu tetikler.
        return Sifre.sifre_liste  # sayısal değerli liste döner.

    def ikilikimlik():  # asil sayılarla ikili kimlik oluşturuyoruz.
        kimlik_sifre = list()  # GRAFİKSEL ARAYÜZDE OUTPUTUN ÜST ÜSTE BİNMEMESİ AMACIYLA LİSTEYİ SIFIRLIYORUZ.
        j = -1
        for i in Sifre.sayisal():
            kimlik_sifre.append(i) #Sifre.sayisal listesini kimlik_sifre ismi altında tekrar kopyalıyoruz.
        try:
            for i in range(1, (len(kimlik_sifre) + 1) + len(csb)):  # girilen kelimenin harf sayısı kadar iki asal sayı ekleneceğinden harf sayısının 2 katı kadar döngüyü  döndürüyoruz.
                if ((i - 2) % 3 == 0 or i - 2 == 0):  # ikinci beşinci yedinci dokuzuncu ... indexlere asal sayi ekleniyor.Bkz:Kelime Setleri.
                    kimlik_sifre.insert(i, Sifre.asal_liste[random.randint(0, 20)])
        except:
            print("Hata!")
        return kimlik_sifre  # asal sayi eklenmiş degisken donuyor.

    def output():#Oluştuurlmuş Kelime Setleri Birleştirilip İlkel Şifre Haline Getiriliyor.İlkel Şifre Kendi İçinde Karıştırılıp Output Hazırlanıyor.
        dosya = open('hash.txt', 'w')#Hash.txt'ye yazılmaya hazırlanıyor.

        cikti1 = ''.join(map(str, Sifre.ikilikimlik()))#Sifre Listesini Stringe Çeviriyor.
        cikti2 = ''.join(reversed(cikti1))#Sifre Listesinin Stringinin Tersini Alıyor.Karıştırma Unsuru.
        cikti3 = random.uniform(10.000, 50.000)#10.000 - 50.000 arası Random Sayı Üretiyor.Karıştırma Unsuru.
        cikti4 = random.uniform(50.000, 90.000)#50.000 - 90.000 arası Random Sayı Üretiyor.Karıştırma Unsuru.

        if (ModAyar.modCek() == "oe"):
            dosya.write(str(cikti4) + cikti1 + cikti2 + str(cikti3))#Mod OE ise OE dizilimini Yapıyor.Karıştırma Unsuru.
            return str(cikti4) + cikti1 + cikti2 + str(cikti3)
            dosya.close()

        elif (ModAyar.modCek() == "oa"):
            dosya.write(cikti1 + str(cikti4) + str(cikti3) + cikti2)#Mod OA ise OA dizilimini Yapıyor.Karıştırma Unsuru.
            return cikti1 + str(cikti4) + str(cikti3) + cikti2
            dosya.close()


class Ui_MainWindow(object):
    # MENÜ VE ARAYÜZ GRAFİKLERİ -GELİŞTİRİLME AŞAMASINDA.-
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 706)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 849))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../.designer/Documents/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 700))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 700))
        self.centralwidget.setObjectName("centralwidget")
        self.banner = QtWidgets.QLabel(self.centralwidget)
        self.banner.setGeometry(QtCore.QRect(200, 0, 400, 200))
        self.banner.setMinimumSize(QtCore.QSize(400, 200))
        self.banner.setMaximumSize(QtCore.QSize(400, 200))
        self.banner.setAlignment(QtCore.Qt.AlignCenter)
        self.banner.setObjectName("banner")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 190, 790, 620))
        self.tabWidget.setMinimumSize(QtCore.QSize(790, 620))
        self.tabWidget.setMaximumSize(QtCore.QSize(790, 620))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setObjectName("tabWidget")
        self.encryption_tab = QtWidgets.QWidget()
        self.encryption_tab.setMinimumSize(QtCore.QSize(0, 620))
        self.encryption_tab.setMaximumSize(QtCore.QSize(16777215, 620))
        self.encryption_tab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.encryption_tab.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.encryption_tab.setStyleSheet("")
        self.encryption_tab.setObjectName("encryption_tab")
        self.Baslik2 = QtWidgets.QLabel(self.encryption_tab)
        self.Baslik2.setGeometry(QtCore.QRect(350, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Baslik2.setFont(font)
        self.Baslik2.setAlignment(QtCore.Qt.AlignCenter)
        self.Baslik2.setObjectName("Baslik2")
        self.Encryption_browser = QtWidgets.QTextBrowser(self.encryption_tab)
        self.Encryption_browser.setGeometry(QtCore.QRect(50, 240, 711, 200))
        self.Encryption_browser.setMinimumSize(QtCore.QSize(0, 200))
        self.Encryption_browser.setMaximumSize(QtCore.QSize(16777215, 200))
        self.Encryption_browser.setReadOnly(True)
        self.Encryption_browser.setObjectName("Encryption_browser")
        self.Encryption_button = QtWidgets.QPushButton(self.encryption_tab)
        self.Encryption_button.setGeometry(QtCore.QRect(370, 190, 121, 41))
        self.Encryption_button.setObjectName("Encryption_button")
        self.encrypt_input = QtWidgets.QLineEdit(self.encryption_tab)
        self.encrypt_input.setGeometry(QtCore.QRect(50, 70, 711, 101))
        self.encrypt_input.setObjectName("encrypt_input")
        self.tabWidget.addTab(self.encryption_tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.baslik_3 = QtWidgets.QLabel(self.tab_2)
        self.baslik_3.setGeometry(QtCore.QRect(350, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.baslik_3.setFont(font)
        self.baslik_3.setAlignment(QtCore.Qt.AlignCenter)
        self.baslik_3.setObjectName("baslik_3")
        self.decrypt_input = QtWidgets.QLineEdit(self.tab_2)
        self.decrypt_input.setGeometry(QtCore.QRect(50, 70, 711, 101))
        self.decrypt_input.setObjectName("decrypt_input")
        self.Decryption_button = QtWidgets.QPushButton(self.tab_2)
        self.Decryption_button.setGeometry(QtCore.QRect(370, 190, 121, 41))
        self.Decryption_button.setObjectName("Decryption_button")
        self.decryption_browser = QtWidgets.QTextBrowser(self.tab_2)
        self.decryption_browser.setGeometry(QtCore.QRect(50, 240, 711, 200))
        self.decryption_browser.setMinimumSize(QtCore.QSize(0, 200))
        self.decryption_browser.setMaximumSize(QtCore.QSize(16777215, 200))
        self.decryption_browser.setReadOnly(True)
        self.decryption_browser.setObjectName("decryption_browser")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuDosya = QtWidgets.QMenu(self.menubar)
        self.menuDosya.setObjectName("menuDosya")
        self.menuYardim = QtWidgets.QMenu(self.menubar)
        self.menuYardim.setObjectName("menuYardim")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionYeni = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/page_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionYeni.setIcon(icon1)
        self.actionYeni.setObjectName("actionYeni")
        self.actionAc = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/folder_page_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAc.setIcon(icon2)
        self.actionAc.setObjectName("actionAc")
        self.actionKaydet = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionKaydet.setIcon(icon3)
        self.actionKaydet.setObjectName("actionKaydet")
        self.actionFarkli_Kaydet = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/disk_multiple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFarkli_Kaydet.setIcon(icon4)
        self.actionFarkli_Kaydet.setObjectName("actionFarkli_Kaydet")
        self.actionFile_Properties = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/page_white_gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFile_Properties.setIcon(icon5)
        self.actionFile_Properties.setObjectName("actionFile_Properties")
        self.actionClose_and_Reset = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose_and_Reset.setIcon(icon6)
        self.actionClose_and_Reset.setObjectName("actionClose_and_Reset")
        self.actionDosya_Sifreleme = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/arrow_switch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDosya_Sifreleme.setIcon(icon7)
        self.actionDosya_Sifreleme.setObjectName("actionDosya_Sifreleme")
        self.actionCikis = QtWidgets.QAction(MainWindow)
        self.actionCikis.setObjectName("actionCikis")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/arrow_undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon8)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/arrow_redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon9)
        self.actionRedo.setObjectName("actionRedo")
        self.actionK = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionK.setIcon(icon10)
        self.actionK.setVisible(True)
        self.actionK.setObjectName("actionK")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/page_copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon11)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/page_paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon12)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSelect_All = QtWidgets.QAction(MainWindow)
        self.actionSelect_All.setObjectName("actionSelect_All")
        self.actionFind = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon13)
        self.actionFind.setObjectName("actionFind")
        self.actionReplace = QtWidgets.QAction(MainWindow)
        self.actionReplace.setObjectName("actionReplace")
        self.actionGo_to = QtWidgets.QAction(MainWindow)
        self.actionGo_to.setObjectName("actionGo_to")
        self.actionGenerate_Pass = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/user_suit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGenerate_Pass.setIcon(icon14)
        self.actionGenerate_Pass.setObjectName("actionGenerate_Pass")
        self.actionZoom = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/magnifier_zoom_in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom.setIcon(icon15)
        self.actionZoom.setObjectName("actionZoom")
        self.actionZoom_out = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/magnifier_zoom_out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_out.setIcon(icon16)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionReset_Zoom = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/magnifier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset_Zoom.setIcon(icon17)
        self.actionReset_Zoom.setObjectName("actionReset_Zoom")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionNasil = QtWidgets.QAction(MainWindow)
        self.actionNasil.setObjectName("actionNasil")
        self.actionGenerate_Key = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("../.designer/Desktop/ottocrypto/key_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGenerate_Key.setIcon(icon18)
        self.actionGenerate_Key.setObjectName("actionGenerate_Key")
        self.actionSet_Encrption_Key = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("black")
        self.actionSet_Encrption_Key.setIcon(icon)
        self.actionSet_Encrption_Key.setObjectName("actionSet_Encrption_Key")
        self.actionClear_Encrytion_Key = QtWidgets.QAction(MainWindow)
        self.actionClear_Encrytion_Key.setObjectName("actionClear_Encrytion_Key")
        self.actionGelistiriciler = QtWidgets.QAction(MainWindow)
        self.actionGelistiriciler.setObjectName("actionGelistiriciler")
        self.menuDosya.addAction(self.actionYeni)
        self.menuDosya.addAction(self.actionAc)
        self.menuDosya.addAction(self.actionKaydet)
        self.menuDosya.addAction(self.actionFarkli_Kaydet)
        self.menuDosya.addSeparator()
        self.menuDosya.addAction(self.actionDosya_Sifreleme)
        self.menuDosya.addSeparator()
        self.menuDosya.addAction(self.actionCikis)
        self.menuYardim.addAction(self.actionNasil)
        self.menuYardim.addAction(self.actionGelistiriciler)
        self.menubar.addAction(self.menuDosya.menuAction())
        self.menubar.addAction(self.menuYardim.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # MENÜ VE ARAYÜZ GRAFİKLERİ -GELİŞTİRİLME AŞAMASINDA.-
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRYPTURK"))
        self.banner.setText(_translate("MainWindow", "BANNER"))
        self.Baslik2.setText(_translate("MainWindow", "ŞİFRELEME"))
        self.Encryption_browser.setPlaceholderText(_translate("MainWindow", "Şifrenize Hash.txt\'den Ulaşabilirsiniz."))
        self.Encryption_button.setText(_translate("MainWindow", "Şifrele"))
        self.encrypt_input.setPlaceholderText(_translate("MainWindow", "Lütfen Şifrelemek İstediğiniz Metni Giriniz."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encryption_tab), _translate("MainWindow", "Encryption"))
        self.baslik_3.setText(_translate("MainWindow", "ŞİFRE ÇÖZME"))
        self.decrypt_input.setPlaceholderText(_translate("MainWindow", "Lütfen Düz Metine Çevirmek İstediğiniz Metni Giriniz."))
        self.Decryption_button.setText(_translate("MainWindow", "Şifreyi Çöz"))
        self.decryption_browser.setPlaceholderText(_translate("MainWindow", "Şifrenize Hash.txt\'den Ulaşabilirsiniz."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Decryption"))
        self.menuDosya.setTitle(_translate("MainWindow", "Dosya"))
        self.menuYardim.setTitle(_translate("MainWindow", "Yardım"))
        self.actionYeni.setText(_translate("MainWindow", "Yeni Dosya"))
        self.actionAc.setText(_translate("MainWindow", "Aç"))
        self.actionKaydet.setText(_translate("MainWindow", "Kaydet"))
        self.actionFarkli_Kaydet.setText(_translate("MainWindow", "Farklı Kaydet"))
        self.actionFile_Properties.setText(_translate("MainWindow", "File Properties"))
        self.actionClose_and_Reset.setText(_translate("MainWindow", "Close and Reset"))
        self.actionDosya_Sifreleme.setText(_translate("MainWindow", "Dosya Şifreleme"))
        self.actionCikis.setText(_translate("MainWindow", "Çıkış"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionK.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionSelect_All.setText(_translate("MainWindow", "Select All"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionReplace.setText(_translate("MainWindow", "Replace"))
        self.actionGo_to.setText(_translate("MainWindow", "Go to"))
        self.actionGenerate_Pass.setText(_translate("MainWindow", "Generate Pass"))
        self.actionZoom.setText(_translate("MainWindow", "Zoom İn"))
        self.actionZoom_out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionReset_Zoom.setText(_translate("MainWindow", "Reset Zoom"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionNasil.setText(_translate("MainWindow", "Nasıl Kullanılır?"))
        self.actionGenerate_Key.setText(_translate("MainWindow", "Generate Key"))
        self.actionSet_Encrption_Key.setText(_translate("MainWindow", "Set Encrption Key"))
        self.actionClear_Encrytion_Key.setText(_translate("MainWindow", "Clear Encrytion Key"))
        self.actionGelistiriciler.setText(_translate("MainWindow", "Geliştiriciler"))

        self.pixmap = QPixmap('crypturk.png')#resim konuşlandırma
        self.banner.setPixmap(self.pixmap)

        self.Encryption_button.clicked.connect(self.encrypt)#encrypt fonksiyonunu encrypt butonuna atar.
        self.Decryption_button.clicked.connect(self.decrypt)#decrypt fonkisyonunu decrypt butonuna atar.


    def sifirla(self):#hash.txt dosyasında önceki işlemlerden kalma şifreler varsa temizler.
        dosya = open("hash.txt", "w")
        self.Encryption_browser.setText(" ")
        dosya.write(" ")

    def encrypt(self):
        global csb
        self.sifirla()#hash.txt dosyasında önceki işlemlerden kalma şifreler varsa temizler.

        metin = self.encrypt_input.text() #arayüze input olarak verilen şifrelenmek istenen metni çeker.
        csb = metin.lower()  # inputu alıp küçük harflere döker.

        if (len(csb) % 2 == 0):  # kelime uzunluguna gore mod verisi gonderir
            ModAyar.modDegis("oe")
        else:
            ModAyar.modDegis("oa")

        self.Encryption_browser.setText(Sifre.output()) #Oluşturulan Şifreyi Arayüze Basar.

    def decrypt(self):
        global csb #Arayüze Verilen İnputun Referansı
        csb = self.decrypt_input.text().strip() # sağdaki,soldaki boşlukları temizleme.
        #if (time.strftime("%H" + "%M") == "0415"):  # saat 4.15 ise kırılım işlemini başlat
        if (True): #DİKKAT! GÜVENLİ MOD KAPALI.GÜVENLİ MOD DECRYPTION TOOL'UN İSTENMEYEN KİŞİLERCE ELE GEÇİRİLMESİ DURUMUNA ÖNLEM OLARAK GELİŞTİRİLMİŞ,YALNIZCA SAAT 4.15'TE KIRILMA İŞLEMİNE İZİN VEREN VE 4.15 DIŞINDA KIRILMAYA ÇALIŞILDIĞINDA UYARI VERMEYEN EMNİYET MODUDUR.BÖYLECE DECRYPTION TOOL ÇALINSA DAHİ DECRYPTION İŞLEMİ YAPILAMAZ.
            if (Kir.modCek(csb) == "oe"):  #Mod OE ise yani şifrelemek istenen metinin harf sayısı çift sayı ise OE kırılım modu başlar.
                Kir.oeSade(csb)  # oe sadeleştirmeyi başlat

            elif (Kir.modCek(csb) == "oa"):  # #Mod OA ise yani şifrelemek istenen metinin harf sayısı tek sayı ise OA kırılım modu başlar.
                Kir.oaSade(csb)  # oa sadeleştirmeyi başlat.

            dosyaOku = open('duz_metin.txt', 'r').read() #Kırılım İşlemi Bittikten Sonra kırılmış Şifre duz_meitn.txt dosyasına basılır.duz_metin.txt verisini arayüze çekmek için yazılmıştır.
            self.decryption_browser.setText(dosyaOku)#Şifreyi arayüze basar.
        else:
            self.decryption_browser.setText("56.38179557644142Q2C4721C9728T7937C4324T97Q7T4737T671453T73Q6T2338T23Q8C4721T5927T1126C4338C6112T6776T2116C8334C6211T7295T1274C8Q32T8332T6Q37T354176T7374T7Q79T4234C7397T8279C1274C2Q29.003378456544905")
            #Decryption Güvenli Moddaysa ve Kişi 4.15 dışında bir saatte şifreyi kırmaya çalışıyorsa yanıltma amaçlı varsayılan şifre ekranda gösterilir.Böylece decryption tool'u çalan kişi program hatalı zanneder.

if __name__ == "__main__": #main fonksiyon yapısı.
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()#arayüz entegrasyon işlemleri
    ui.setupUi(MainWindow) # arayüzü programa entegre etme.
    MainWindow.show() #arayüzü gösterme.
    sys.exit(app.exec_())#arayüz gösterimini döngüde tutma,böylece çarpıya basılmadıkça kapanmasını engelleme.
