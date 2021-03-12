#Proses Membuat Biodata
nama = "Cita Tri Cahaya Sakti"
Biodata = "Halo perkenalkan, saya" + " " + nama

#Perhitungan Umur
tanggal_lahir = 28
bulan_lahir = 2
tahun_lahir = 2002
tanggal_skrg = 11
bulan_skrg = 3
tahun_skrg = 2021
umur = ((tanggal_skrg - tanggal_lahir)/365 + (bulan_skrg - bulan_lahir)/12 + (tahun_skrg - tahun_lahir))

#Perhitung Tinggi Badan dan Berat Badan
TBcenti = 172
BBgram= 98000
tinggi_badan = float(TBcenti/100)
berat_badan = float(BBgram/1000)
ukuran_sepatu = "ukuran sepatu saya adalah 44"

Alamat_jalan= "Jln. Stonen Timur"
Nomer_alamat = "17"
Alamat_rumah = Alamat_jalan + " " + Nomer_alamat + " " +"Gajahmungkur, Semarang"
#Data Diri
NIM = " NIM I0320020"
Kelas = "A"
Prodi = "Teknik Industri"
PTN = "Universitas Sebelas Maret"
Motivasi_Masuk_Universitas = "Universitas Sebelas Maret merupakan universitas favorit dan memiliki lingkungan aman, nyaman dan rindang"
Motivasi_Masuk_TeknikIndustri = "Teknik industri salah satu prodi yang memiliki peminat yang tinggi serta jurusan ini mempelajari macam-macam ilmu"
Cita_cita = "Saya bercita-cita menjadi seorang direktur, bisa membanggakan orang tua dan membbantu orang sekitar"
Moto_hidup = "Moto hidup saya : Sederhana itu indah"
Deskripsi = "Saya merupakan anak ketiga dari empat bersuadara. Saya cukup pemalu bila bertemu dengan orang yang malu, sedangkan jika sudah akrab saya orangg yang cukup ramah dan suka bergaul. Saya gemar bermain game dan berenang"

print("Deskripsi Biodata\n", Biodata, "\n", int(umur),"tahun", "\n", Alamat_rumah, "\n", tinggi_badan, "meter", "\n", berat_badan, "kg", "\n", ukuran_sepatu, "\n", NIM, "\n", Prodi,"\n", PTN, "\n", Motivasi_Masuk_Universitas, "\n", Motivasi_Masuk_TeknikIndustri, "\n", Cita_cita, "\n", Moto_hidup, "\n", Deskripsi)
print("------------------TERIMAKASIH------------------")