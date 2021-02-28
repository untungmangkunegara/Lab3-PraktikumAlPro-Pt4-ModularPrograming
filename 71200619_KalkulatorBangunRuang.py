#Buatlah kalkulator bangun ruang. Untuk membantu teman-teman dari SMP yang akan mempelajari mengenai materi bagun ruang. 
# Di dalam kalkulator, pengguna akan diminta memasukkan angka pilihan untuk memenuhi kriteria pemilihan bangun ruang. 
# Berikut fitur-fitur yang disediakan Kalkulator Bangun ruang:
#1.	Menghitung kubus.
#2.	Menghitung balok.
#3.	Menghitung bola.
#Dengan menggunakan template fungsi berikut ini buatlah kalkulator konversi suhu.
#def kubus(sisi):
#...
#def balok(panjang,lebar,tinggi):
#...
#def bola(jari2):
#========================================================================================================================
print("=== Kalkulator Volume Bangun Ruang ===")
print("Pilih Menu Kalkulator Volume Bangun Ruang")
print("1. Kubus")
print("2. Balok")
print("3. Bola")
#=====================
def kubus(sisi):
    volumeK=sisi*sisi*sisi
    volumeK=round(volumeK, 1)
    return volumeK

def balok(panjang,lebar,tinggi):
    volumeB=panjang*lebar*tinggi
    volumeB=round(volumeB, 1)
    return volumeB

def bola(jari2):
    pi=3.14
    volumeBO=(4/3)*pi*jari2*jari2*jari2
    volumeBO=round(volumeBO, 1)
    return volumeBO
#=====================
a=int(input("Masukkan pilihan anda: "))
#=====================
if a==1:
    a1=float(input("Masukkan sisi kubus: "))
    print("Volume kubus adalah", kubus(a1))
elif a==2:
    a1=float(input("Masukkan panjang balok: "))
    a2=float(input("Masukkan lebar balok: "))
    a3=float(input("Masukkan tinggi balok: "))
    print("Volume balok adalah", balok(a1,a2,a3))
elif a==3:
    a1=float(input("Masukkan jari-jari bola: "))
    print("Volume bola adalah", bola(a1))
else:
    print("Maaf pilihan anda tidak tersedia, silahkan coba lagi.")