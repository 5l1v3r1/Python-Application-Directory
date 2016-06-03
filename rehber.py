#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3
 
baglanti = sqlite3.connect("sqlite_database/sqlite_data")
isaretci = baglanti.cursor()

def adres_defterine_ekleme():
	kisi_isim = raw_input("Kişi isim : ")
	kisi_adres = raw_input("Kişi ev adresi : ")
	kisi_kurumsalmail= raw_input("Kişi kurumsal mail adresi : ")
	kisi_mail = raw_input("Kişi mail adresi : ")
	kisi_tel = raw_input("Kişi telefon numarası : ")
	kisi_twitter = raw_input("Kişi twitter adresi : ")
	kisi_linkedin = raw_input("Kişi linkedin adresi : ")
	kisi_instagram = raw_input("Kişi insatgram adresi : ")
	kisi_snapchat = raw_input("Kişi snapchat adresi : ")
	kisi_aciklama = raw_input("Kişi açıklama : ")
	isaretci.execute("""INSERT INTO Adres_Defteri (kisi_isim,kisi_adres,kisi_kurumsalmail,kisi_mail,kisi_tel,kisi_twitter,kisi_linkedin,kisi_instagram,kisi_snapchat,kisi_aciklama) VALUES (?,?,?,?,?,?,?,?,?,?)""",(kisi_isim, kisi_adres, kisi_kurumsalmail, kisi_mail,kisi_tel, kisi_twitter, kisi_linkedin, kisi_instagram, kisi_snapchat,  	kisi_aciklama))
	baglanti.commit()

def adres_defteri_kisi_silme():
	silinecek = raw_input("Silinecek Numarayı gir : ")
        isaretci.execute("DELETE from Adres_Defteri Where kisi_id =" + " " + silinecek + ";")
        baglanti.commit()

def adres_defeteri_listele():
	db = isaretci.execute("SELECT * FROM Adres_Defteri")
	print db.fetchall()
	baglanti.close()

adres_rehber_ico = """
#########################################################
#         PYTHON - ADRES DEFTERİ - GH0ST S0FTWARE       #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

star = "#########################################################"

islemler_ico = """
(1) Deftere Kişi Ekle
(2) Defterdeki Kişiyi Sil
(3) Defterdeki Kişileri Göster
"""

ekleme_yapildi_ico = """
#########################################################
#           Yeni Kişi Adres Defterine Eklendi           # 
#########################################################
"""

silme_yapildi_ico = """
#########################################################
#            Kişi Adres Defterinden Silindi             # 
#########################################################
"""

print adres_rehber_ico

print star

print islemler_ico

print star

islem = input("Yapılcak işlem numrasını giriniz : ")

print star

if islem == 1:
	adres_defterine_ekleme()
	print ekleme_yapildi_ico

elif islem == 2:
	adres_defteri_kisi_silme()
	print silme_yapildi_ico

elif islem == 3:
	adres_defeteri_listele()
