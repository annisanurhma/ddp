import bangunRuang as br
import bangundatar as bd

print("----bangun ruang----")
print(f"Volume kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"Volume balok dengan adalah {br.balok(4 ,5, 6)}")
print(f"Volume prisma segitiga adalah adalah {br.prisma(4, 5, 6)}")
print(f"Volume tabung adalah {br.tabung(2, 10)}")
print(f"volume kerucut adalah{br.kerucut(7, 10)}")

print(" BANGUN DATAR ~~")
print(f"Luas Persegi adalah {bd.persegi(4)}")
print(f"Luas Persegi Panjang adalah {bd.persegi_panjang(10 ,5)}")
print(f"Luas Segitiga adalah {bd.segitiga(4, 3)}")
print(f"Luas Lingkaran adalah {bd.lingkaran(7)}")
print(f"Luas JajarGanjar adalah {bd.jajarGanjar(4,7)}")
