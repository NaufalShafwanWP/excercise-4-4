a = 125
b = 62
c = 256
d = 70
e = a+c

Berangkat_a_ke_b = float(input("Waktu berangkat dari kota a ke b:"))
Jarak_tempuh_a_ke_b = float(input("Jarak tempuh dari kota a ke b:"))
Kecepatan_a_ke_b = float(input("Kecepatan dari kota a ke b:"))
Lama_waktu_a_ke_b = a/b
print(round(Lama_waktu_a_ke_b, 2))

Jarak_tempuh_b_ke_c = float(input("Jarak tempuh dari kota b ke c:"))
Kecepatan_b_ke_c = float(input("Kecepatan dari kota b ke c:"))
Lama_waktu_b_ke_c = c/d + 1/60 * 45
print(float(Lama_waktu_b_ke_c))

Total_waktu = Lama_waktu_a_ke_b + Lama_waktu_b_ke_c
print(round(Total_waktu, 1))

