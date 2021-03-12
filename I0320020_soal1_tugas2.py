#Menghitung Luas persegi panjang
print("Selamat datang di Cikalku, menghitung luas persegi panjang")
print("Masukkan panjang dan lebarnya ya")
panjang = float(input("panjang (meter)="))
lebar = float(input("lebar (meter) = "))
luas = panjang*lebar
print("Jadi, luas persegi panjang adalah", luas, "m^2")

##Menghitung Luas Lingkaran
print("Menghitung luas lingkarang")
print("Masukkan Jari-jari lingkaran ya")
phy = 3.14
Jari = float(input("jari jari (meter)= "))
LuasLingkaran = phy*(Jari**2)
print("Jadi, luas lingkaran adalah", LuasLingkaran, "m^2")

#Menghitung Luas Kubus
print("Menghitung Luas Permukaan kubus")
print("Masukkank sisi kubus ya")
sisi = float(input("Sisi (meter) = "))
LuasKubus = (sisi**2)*6
print("Jadi, luas permukaan kubus adalah", LuasKubus, "m^2")

#Konversi Suhu Celcius ke Farenheit
print("Selamat datang, Silahkang menggunakan Cikaklku Konversi suhu Celcius ke Frenheit")
print("Silahkan masukkan suhu dalam derajat reamur")
suhuCelsius= float(input("Suhu (Celsius)= "))
KonversiFarenheit = 9*(suhuCelsius/5) + 32
print("Jadi, Konversi suhu Celius", suhuCelsius,"menjadi", KonversiFarenheit, "F")

#Konversi Suhu Reamur ke Kelvin
print("Silahkan menggunakan Cikalku Konversi Suhu Reamur ke Kelvin")
print("Silahkan masukkan suhu dalam derajat Reamur")
suhuReamur = float(input("Suhu (Reamur) = "))
KonversiCelsius = (suhuReamur/4)*5
KonversiKelvin = KonversiCelsius + 273
print("jadi Konversi suhu Reamur", suhuReamur, "menjadi", KonversiCelsius,"C", ",dan", KonversiKelvin, "K")