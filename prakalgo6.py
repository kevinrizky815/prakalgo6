# -*- coding: utf-8 -*-
"""PrakAlgo6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17zrtnZze0EunDQG26rbQyHN_J_nhAy47
"""

print("@@    @@  @@@@@@   @@             @@  @@  @@@@       @@")
print("@@   @@   @@        @@           @@   @@  @@  @@     @@")
print("@@ @@     @@         @@         @@    @@  @@   @@    @@")
print("@@@       @@@@@@      @@       @@     @@  @@    @@   @@")
print("@@ @@     @@           @@     @@      @@  @@     @@  @@")
print("@@   @@   @@            @@   @@       @@  @@      @@ @@")
print("@@    @@  @@@@@@         @@@@@        @@  @@       @@@@")
# Meminta input dari pengguna
V0 = float(input("Masukkan kecepatan awal (m/s): "))  # Input kecepatan awal
s = float(input("Masukkan jarak yang ditempuh (meter): "))  # Input jarak yang ditempuh
a = float(input("Masukkan percepatan (m/s^2): "))  # Input percepatan

# Menghitung kecepatan akhir (Vt)
Vt = (V0 ** 2 + 2 * a * s) ** 0.5

# Menampilkan hasil perhitungan beserta penjelasan
print(f"Kecepatan akhir (Vt) = {Vt} m/s")
print(f"Kecepatan akhir (Vt) adalah kecepatan yang akan dicapai setelah perjalanan sejauh {s} meter,")
print(f"dengan kecepatan awal {V0} m/s, dan percepatan {a} m/s^2.")

print("@@    @@  @@@@@@   @@             @@  @@  @@@@       @@")
print("@@   @@   @@        @@           @@   @@  @@  @@     @@")
print("@@ @@     @@         @@         @@    @@  @@   @@    @@")
print("@@@       @@@@@@      @@       @@     @@  @@    @@   @@")
print("@@ @@     @@           @@     @@      @@  @@     @@  @@")
print("@@   @@   @@            @@   @@       @@  @@      @@ @@")
print("@@    @@  @@@@@@         @@@@@        @@  @@       @@@@")
import math
def luas_permukaan_kubus(sisi):
    return 6 * sisi**2
def luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
def luas_permukaan_tabung(jari_jari, tinggi):
    tutup_atas = math.pi * jari_jari**2
    selimut = 2 * math.pi * jari_jari * tinggi
    return 2 * tutup_atas + selimut
def luas_permukaan_kerucut(jari_jari, tinggi):
    selimut = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari**2 + tinggi**2))
    return math.pi * jari_jari**2 + selimut
def luas_permukaan_bola(jari_jari):
    return 4 * math.pi * jari_jari**2
while True:
    print("Pilih dah tu bangunan yang pengen lu itung luas permukaannya:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Bola")
    print("0. Keluar")
    pilihan = int(input("lu mau cari yg mana bro?: "))
    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi kubus: "))
        luas = luas_permukaan_kubus(sisi)
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        luas = luas_permukaan_balok(panjang, lebar, tinggi)
    elif pilihan == 3:
        jari_jari = float(input("Masukkan jari-jari tabung: "))
        tinggi = float(input("Masukkan tinggi tabung: "))
        luas = luas_permukaan_tabung(jari_jari, tinggi)
    elif pilihan == 4:
        jari_jari = float(input("Masukkan jari-jari kerucut: "))
        tinggi = float(input("Masukkan tinggi kerucut: "))
        luas = luas_permukaan_kerucut(jari_jari, tinggi)
    elif pilihan == 5:
        jari_jari = float(input("Masukkan jari-jari bola: "))
        luas = luas_permukaan_bola(jari_jari)
    elif pilihan == 0:
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")

    print(f"Luas permukaan: {luas} satuan luas")
    print("======================================")

