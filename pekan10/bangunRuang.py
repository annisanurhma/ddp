import math
def kubus(sisi):
    hasil = math.pow(sisi, 3)
    return hasil
#print (kubus (3))

def balok(p, l, t):
    hasil = p * l * t
    return hasil
#print (balok (4, 5, 6))

def prisma(alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    return hasil
#print (prisma (4, 5, 6))

def tabung(jari_jari, tinggi):
    hasil = math.pi * math.pow(jari_jari, 2) * tinggi
    return hasil
#print (tabung (2, 10))

def kerucut(jari_jari, tinggi):
    hasil = (1/3) * math.pi * math.pow(jari_jari, 2) * tinggi
    return hasil
#print (kerucut(7,10))
