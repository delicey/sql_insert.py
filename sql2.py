import sqlite3 as sql


adi = input("Öğrenci adı: ")
soyadi = input("Öğrenci soyadı: ")
nosu = input("Öğrenci numarası: ")
notu = input("Öğrenci notu: ")

con = sql.connect("sqlim.db")

cursor = con.cursor()

#def tabloOlustur():
#    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad, soyad, no, notlar)")
#    con.commit()



def ogrenciEkle():
    ogrenci_yeni = "INSERT INTO ogrenciler VALUES (?, ?, ?, ?);"
    data_tuple = (adi, soyadi, nosu, notu)
    cursor.execute(ogrenci_yeni,data_tuple)
    con.commit()


#tabloOlustur()
ogrenciEkle()

con.close()