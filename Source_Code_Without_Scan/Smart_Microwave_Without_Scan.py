#PROGRAM SMART MICROWAVE
#Alur kerja serta logika microwave sederhana

#KAMUS
#class
    #comp: Berisi komponen penting untuk berjalannya Mikrowave (suhu, waktu, kelembapan)
    #mode: berisi pintasan mode otomatis untuk menjalankan microwave
    #vegetable: Berisi mode memasakn otomatis untuk sayuran
    #seafood: Berisi mode memasakn otomatis untuk Seafood
    #incode: Berisi mode memasakn otomatis untuk Seafood
    #Microwave: Berisi logika utama berjalannya program, mulai dari tampilan sampai pemrosesan input dan output
    #notif: Berisi prosedur untuk memutar notifikasi
    #Music: Berisi prosedur untuk memutar musik
    
#Fungsi dan prosedur
    ##Comp
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class
        #moisture1: berfungsi untuk menentukan kelembapan akhir setelah melewati proses memasak, dengan batas kelembapan yang sudah diatur(disesuaikan)
    ##mode
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class
        #quick_heat: mode untuk memasak cepat biasa untuk memanansakn makanan
        #Deforst: mode untuk mencairkan makanan beku
        #Grill: mode untuk melakukan proses pemanggangan dengan suhu tinggi
    ##Vegetable
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class
        #menu: Berisi daftar sayuran yang dapat dimasak otomatis
        #wortel : mode memasak otomatis untuk wortel
        #kembang_kol: mode memasak otomatis untuk kembang kol
        #bayam : mode memasak otomatis untuk bayam
        #jagung_manis : mode memasak otomatis untuk jagung manis
        #paprika : mode memasak otomatis untuk paprika
        #zuicchini : mode memasak otomatis untuk zuicchini
    ##seafood
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class
        #menu: Berisi daftar Seafood yang dapat dimasak otomatis
        #fish: mode memasak otomatis untuk ikan fillet(tuna dan sebagainya)
        #shirmp: mode memasak otomatis untuk udang
        #squid: mode memasak otomatis untuk cumi-cumi
        #shellfish: mode memasak otomatis untuk kerang
        #lobster: mode memasak otomatis untuk lobster
    ##incode
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class
        #detect: berfungsi untuk mencocokan barcode hasil scan dengan database, dan mengimport data yang diperlukan
        #cook: mode memasak otomatis untuk makanan yang berhasil discan
    ##Microwave
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class
        #displayup: berfungsi sebagai batas atas pada display layar microwave
        #displaydown: berfungsi sebagai batas bawah pada display layar microwave
        #display1: berfungsi untuk memberikan tampilan awal saat microwave dijalakan atau direstart(start display)
        #display2: berfungsi untuk memberikan tampilan saat microwave sedang melakuakn proses memasak, menampilkan suhu terkini, sisa waktu, dan temperatur terkini.
        #displayCooling: berfungsi untuk meberikan tampilan saat microwave menjalankan fungsi Cooling
        #displayClean: berfungsi untuk meberikan tampilan saat microwave menjalankan fungsi Cleaning
        #displayCoolingDone: berfungsi untuk meberikan tampilan saat microwave selesai menjalankan fungsi Cooling
        #displayCleanDone: berfungsi untuk meberikan tampilan saat microwave selesai menjalankan fungsi Cleaning
        #displayundercooked: berfungsi untuk memberikan tampilan saat makanan yang dimasak Undercooked (kelembapan lebih dari 75%)
        #displayover: berfungsi untuk memberikan tampilan saat makanan yang dimasak overcooked (kelembapan kurang dari 40%)
        #displaydry: berfungsi untuk memberikan tampilan saat makanan yang dimasak sudah kering (kelembapan 0%)
        #displaydone: berfungsi untuk memberikan tampilan saat makanan yang dimasak sudah matang sempurna
        #menu: menampilkan pilihan menu dari fitur microwave yang dapat dijalankan
        #menulock: menampilkan pilihan menu dari fitur microwave ketika dalam mode Child Lock
        #Start: berisi logika utama dalam menjalankan semua fitur mikrowave serta memproses input dan output user
    ##Notif
        #menu:berfungsi untuk menampilkan menu menyalakan atau mematikan notifikasi
        #notifStart: prosedur yang berfungsi untuk memutar notifikasi saat microwave mulai MEMASAK
        #notifDone: prosedur yang berfungsi untuk memutar notifikasi saat microwave selesai MEMASAK
        #notifAlmostDone: prosedur yang berfungsi untuk memutar notifikasi saat microwave hampir selesai MEMASAK (30 detik sebelum selesai)
        #notifChildLock: prosedur yang berfungsi untuk memutar notifikasi saat mengaktifkan/menonakitfkan mode ChildLock
        #notifWrong: prosedur yang berfungsi untuk memutar notifikasi saat salah memasukan pin ChildLock
    ##Music
        #menu1: berfungsi untuk menampilkan menu memutar atau mematikan musik
        #menu2: berfungsi untuk menampilkan menu memilih musik yang ingin diputar
        #music1: prosedur yang berfungsi untuk memutar musik ke-1
        #music2: prosedur yang berfungsi untuk memutar musik ke-2
        #music3: prosedur yang berfungsi untuk memutar musik ke-3

#variable
    #aturulang(string(char)): menyimpan konfirmasi dari user untuk memasak ulang atau tidak (ganti waktu dan suhu)
    #barcode(int): menyimpan nilai barcode makanan yang sesuai
    #barcode(int): menyimpan barcode yang berhasil di deteksi
    #ChildLock(boolean): parameter mode Child lock(true jika sedang dalam mode child lock)
    #Choice(int): menyimpan pilihan fitur yang akan digunakan user
    #Code(int): menyimpan nomor barcode makanan yang berhasil di scan
    #codefood(list): menyimpan semua data barcode makanan yang ada dalam database
    #confirm(string): menyimpan inputan user terkait konfirmasi nama makanan yang akan dimasak melalui fitur scan barcode
    #csvfile(file csv(list)): berisi file csv yang menyimpan data makanan 
    #filename(file): berisi file suara(notifikasi atau musik) yang akan diputar
    #foodname(string): menyimpan nama makanan yang sesuai barcode
    #foodcode(list): menyimpan data yang berasal dari database csvfile
    #limit(int): nilai batas kelembapan saat menjalankan fungsi masak otomatis
    #min(int): menyimpan nilai menit waktu memasak(hasil pembagian time dengan 60)
    #moisture(int): menyimpan pengaturan kelembapan microwave
    #moisturefood(list): menyimpan semua data batas kelembapan makanan yang ada dalam database
    #musicchoice(int): menyimpan pilihan user pada menu media player
    #namefood(list): menyimpan semua data nama makanan yang ada dalam database
    #notifchoice(int): menyimpan pilihan user pada menu Notif
    #pin(int) = menyimpan PIN yang dimasukan user saat microwave sedang dalam mode Child Lock
    #notification(boolean): parameter notifikasi nyala(True) atau mati(False)
    #pinlock(int): menyimpan PIN yang digunakan pada mode Child Lock
    #play_obj(media player): memutar musik atau notifikasi
    #sayur(int): menyimpan pilihan mode memasak sayuran yang akan digunakan user
    #seaf(int): menyimpan pilihan mode memasak seafood yang akan digunakan user
    #sec(int): menyimpan nilai detik waktu memasak(sisa pembagian time dengan 60)
    #side_h(int): menyimpan nilai batas horizontal dislpay
    #side_v(int): menyimpan nilai batas vertikal dislpay
    #stop(boolean): parameter untuk mendeteksi apakah microwave dihentikan saat sedang berjalan atau tidak
    #temp(int): menyimpan pengaturan suhu microwave
    #tempfood(list): menyimpan semua data tempratur untuk memesak makanan yang ada dalam database
    #time(int): menyimpan pengaturan waktu microwave
    #timefood(list): menyimpan semua data waktu memasak makanan yang ada dalam database
    #vegen(int): menyimpan pilihan mode memasak seafood yang akan digunakan user
    #wait(int): menyimpan countdown untuk mematikan microwave secara otomatis setelah watu memasak selesai
    #wave_obj: mendeteksi(decode) dan menyimpan file kedalam format wav
#Objek
    #clean(Microwave): object class Microwave, untuk menggunakan metode(fungsi) Cleaning pada class Microwave
    #cooling(Microwave): object class Microwave, untuk menggunakan metode(fungsi) cooling pada class Microwave
    #food(mode): object class mode, untuk menggunakan metode(fungsi) pada class mode
    #food(incode): object class incode, untuk menggunakan metode(fungsi) pada class incode
    #seafd(seafood): object class seafood, untuk menggunakan metode(fungsi) pada class seafood
    #vegen(vegetable): object class vegetable, untuk menggunakan metode(fungsi) pada class vegetable

import time
import os
import csv
import simpleaudio as sa

class comp: #Kelas comp ini menjadi parent class untuk kelas-kelas yang lain
    #Kamus Lokal
    #Fungsi dan prosedur
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class 
        #moisture1: berfungsi untuk menentukan kelembapan akhir setelah melewati proses memasak, dengan batas kelembapan yang sudah diatur(disesuaikan)
        
    def __init__(self, time:int, temp:int, moisture:int): #Kelas ini memiliki tiga atribut atau nilai, yaitu time (waktu), temperature (suhu), dan moisture (kelembaban) yang disimpan dalam variabel self
        #Kamus Lokal
        #Variabel
            #moisture(int): menyimpan pengaturan kelembapan microwave
            #temp(int): menyimpan pengaturan suhu microwave
            #time(int): menyimpan pengaturan waktu microwave
            
        self.time = time*60 #waktu diubah menjadi satuan detik dari inputnya menit
        self.temp = temp #nilai temperature dari self diambil dari nilai temp
        self.moisture = moisture #nilai moisture dari self diambil dari nilai moisture

    #Pada program microwave ini nilai kelembaban berkurang seiring dengan berjalannya pemasakan makanan
    def moisture1(self, limit): #Fungsi ini digunakan untuk mengurangi nilai kelembaban
        #Kamus Lokal
        #Variabel
            #limit(int): nilai batas kelembapan saat menjalankan fungsi masak otomatis
            #time(int): menyimpan pengaturan waktu microwave
            
        if self.moisture >= limit: #Mulai dari sini sampai bawah merupakan fungsi untuk mengurangi persentase kelembaban kondisi di dalam microwave
            time = self.time
            while time > 0: #Selama waktu memasak masih tersisa, kelembaban akan terus berkurang sebesar temperatur/1200 sampai nilai kelembabannya di bawah batas minimum kelembaban microwave (limit)
                self.moisture = self.moisture - (self.temp/1200)
                if self.moisture <= limit:
                    break
                time -= 1     

class mode(comp): #Kelas ini merupakan anakan dari kelas comp yang digunakan untuk melakukan 3 mode pemasakan cepat (tanpa pengaturan manual), yaitu quick heat, defrost, dan gril
    #Kamus Lokal
    #Fungsi dan prosedur
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class 
        #quick_heat: mode untuk memasak cepat biasa untuk memanansakn makanan
        #Deforst: mode untuk mencairkan makanan beku
        #Grill: mode untuk melakukan proses pemanggangan dengan suhu tinggi
        
    def __init__(self, time, temp, moisture): #Seperti kelas comp, kelas mode ini juga memiliki nilai waktu, temperatur, dan kelembaban yang disimpan dalam variabel self
        #Kamus Lokal
        #Variabel
            #moisture(int): menyimpan pengaturan kelembapan microwave
            #temp(int): menyimpan pengaturan suhu microwave
            #time(int): menyimpan pengaturan waktu microwave
        super().__init__(time, temp, moisture)
    def quick_heat(self): #Fungsi untuk menggunakan mode quick heat
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 40) #Mode ini  memiliki batas (limit) kelembaban sebesar 40 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def Deforst(self): #Fungsi untuk menggunakan mode defrost
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 60) #Mode ini  memiliki batas (limit) kelembaban sebesar 60 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def Grill(self): #Fungsi untuk menggunakan mode grill
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 30) #Mode ini  memiliki batas (limit) kelembaban sebesar 30 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
class vegetable(comp): #Kelas ini merupakan anakan dari kelas comp yang digunakan untuk melakukan pemasakan sayuran
    #Kamus Lokal
    #Fungsi dan prosedur
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class 
        #menu: Berisi daftar sayuran yang dapat dimasak otomatis
        #wortel : mode memasak otomatis untuk wortel
        #kembang_kol: mode memasak otomatis untuk kembang kol
        #bayam : mode memasak otomatis untuk bayam
        #jagung_manis : mode memasak otomatis untuk jagung manis
        #paprika : mode memasak otomatis untuk paprika
        #zuicchini : mode memasak otomatis untuk zuicchini
        
    def __init__(self, time, temp, moisture): #Seperti kelas comp, kelas vegetable ini juga memiliki nilai waktu, temperatur, dan kelembaban yang disimpan dalam variabel self
        #Kamus Lokal
        #Variabel
            #moisture(int): menyimpan pengaturan kelembapan microwave
            #temp(int): menyimpan pengaturan suhu microwave
            #time(int): menyimpan pengaturan waktu microwave
            
        super().__init__(time, temp, moisture)
    def menu(): #Fungsi ini adalah fungsi untuk menampilkan menu sayuran yang tersedia
        #Kamus Lokal
        #Variabel
        
        Microwave.display1() #Seiring dengan penampilan menu sayuran, microwave juga menampilkan interfacenya (akan dijelaskan lebih lanjut fdi bawah)
        print(f'======================================')
        print(f'||1. brokoli      ||5. jagung manis ||')
        print(f'||==================================||')
        print(f'||2. wortel       ||6. paprika      ||')
        print(f'||==================================||')
        print(f'||3. kembang kol  ||7. zucchini     ||')
        print(f'||==================================||')
        print(f'||4. bayam        ||0. Kembali      ||')
        print(f'======================================')
    def brokoli(self): #Fungsi ini adalah fungsi untuk memasak brokoli
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 70) #Pemasakan brokoli  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def wortel(self): #Fungsi ini adalah fungsi untuk memasak wortel
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 60) #Pemasakan wortel  memiliki batas (limit) kelembaban sebesar 60 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def kembang_kol(self): #Fungsi ini adalah fungsi untuk memasak kembang kol
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 70) #Pemasakan kembang kol  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def bayam(self): #Fungsi ini adalah fungsi untuk memasak bayam
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 80) #Pemasakan bayam  memiliki batas (limit) kelembaban sebesar 80 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def jagung_manis(self): #Fungsi ini adalah fungsi untuk memasak jagung manis
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 70) #Pemasakan jagung manis  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def paprika(self): #Fungsi ini adalah fungsi untuk memasak paprika
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 60) #Pemasakan paprika  memiliki batas (limit) kelembaban sebesar 60 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def zucchini(self): #Fungsi ini adalah fungsi untuk memasak zuncchini
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 70) #Pemasakan zucchini  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
class seafood(comp): #Kelas ini merupakan anakan dari kelas comp yang digunakan untuk melakukan pemasakan seafood
    #Kamus Lokal
    #Fungsi dan prosedur
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class 
        #menu: Berisi daftar Seafood yang dapat dimasak otomatis
        #fish: mode memasak otomatis untuk ikan fillet(tuna dan sebagainya)
        #shirmp: mode memasak otomatis untuk udang
        #squid: mode memasak otomatis untuk cumi-cumi
        #shellfish: mode memasak otomatis untuk kerang
        #lobster: mode memasak otomatis untuk lobster
        
    def __init__(self, time, temp, moisture): #Seperti kelas comp, kelas seafood ini juga memiliki nilai waktu, temperatur, dan kelembaban yang disimpan dalam variabel self
        #Kamus Lokal
        #Variabel
            #moisture(int): menyimpan pengaturan kelembapan microwave
            #temp(int): menyimpan pengaturan suhu microwave
            #time(int): menyimpan pengaturan waktu microwave
        super().__init__(time, temp, moisture)
    def menu(): #Fungsi ini adalah fungsi untuk menampilkan menu sayuran yang tersedia
        #Kamus Lokal
        #Variabel
        
        Microwave.display1() #Seiring dengan penampilan menu seafood, microwave menampilkan interfacenya
        print(f'======================================')
        print(f'||1. Ikan Fillet  ||4. Kerang       ||')
        print(f'||==================================||')
        print(f'||2. Udang        ||5. Lobster      ||')
        print(f'||==================================||')
        print(f'||3. Cumi-cumi    ||0. Kembali      ||')
        print(f'======================================')
    def fish(self): #Fungsi ini adalah fungsi untuk memasak ikan fillet
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 70) #Pemasakan ikan fillet  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def shrimp(self): #Fungsi ini adalah fungsi untuk memasak udang
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 75) #Pemasakan udang  memiliki batas (limit) kelembaban sebesar 75 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def squid(self): #Fungsi ini adalah fungsi untuk memasak cumi-cumi
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 70) #Pemasakan cumi-cumi  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def shellfish(self): #Fungsi ini adalah fungsi untuk memasak kerang
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 70) #Pemasakan kerang  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
    def lobster(self): #Fungsi ini adalah fungsi untuk memasak lobster
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 70) #Pemasakan lobster  memiliki batas (limit) kelembaban sebesar 70 %
        Microwave.display2(self) #Setelah fungsi dijalankan, microwave akan menampilkan interfacenya (akan dijelaskan lebih lanjut di bawah)
         
class incode(comp): #Kelas ini merupakan anakan dari kelas comp yang digunakan untuk membaca kode barcode paket makanan yang tersedia
    #Kamus Lokal
    #Fungsi dan prosedur
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class 
        #detect: berfungsi untuk mencocokan barcode hasil scan dengan database, dan mengimport data yang diperlukan
        #cook: mode memasak otomatis untuk makanan yang berhasil discan
    def __init__(self, time:int, temp:int, moisture:int, barcode:int, foodname):
        #Kamus Lokal
        #Variabel
            #barcode(int): menyimpan nilai barcode makanan yang sesuai
            #foodname(string): menyimpan nama makanan yang sesuai barcode
            #moisture(int): menyimpan pengaturan kelembapan microwave
            #temp(int): menyimpan pengaturan suhu microwave
            #time(int): menyimpan pengaturan waktu microwave
        super().__init__(time, temp, moisture)
        self.barcode = barcode
        self.foodname = foodname
        
    def detect(self, Code):
        #Kamus Lokal
        #Variabel
            #Code(int): menyimpan nomor barcode makanan yang berhasil di scan
            #codefood(list): menyimpan semua data barcode makanan yang ada dalam database
            #csvfile(file csv(list)): berisi file csv yang menyimpan data makanan 
            #foodcode(list): menyimpan data yang berasal dari database csvfile
            #moisturefood(list): menyimpan semua data batas kelembapan makanan yang ada dalam database
            #namefood(list): menyimpan semua data nama makanan yang ada dalam database
            #tempfood(list): menyimpan semua data tempratur untuk memesak makanan yang ada dalam database
            #timefood(list): menyimpan semua data waktu memasak makanan yang ada dalam database
        #membuka dan menyimpan nilai file database(csv)
        csvfile = open('Source_Code_Without_Scan\\barcodes.csv', newline='')
        foodcode = csv.reader(csvfile)
        #skip baris pertama pada file csv(header)
        next(foodcode)
        codefood = []
        namefood = []
        timefood = []
        tempfood = []
        moisturefood = []
        #perulangan untuk mengambil dan memisakan antara value yang dibutuhkan pada database
        for row in foodcode:
            codefood.append(int(row[1]))
            namefood.append(row[2])
            timefood.append(int(row[3])*60)
            tempfood.append(int(row[4]))
            moisturefood.append(int(row[5]))
        #menutuk kembali file database(csv)
        csvfile.close()
        #mencocokan barcode yang sesuai dengan hasil scan atau input dengan data pada database 
        for i in range(len(codefood)):
            #jika data sudah ditemukan maka perulangan akan dihentikan
            if Code == codefood[i]:
                self.foodname = namefood[i]
                self.barcode = codefood[i]
                self.time = timefood[i]
                self.temp = tempfood[i]
                self.moisture = moisturefood[i]
                break               
    def cook(self):
        #Kamus Lokal
        #Variabel
        
        comp.moisture1(self, 0)
        Microwave.display2(self)

notification = True
class notif(): #Kelas ini digunakan untuk memutar notifikasi
    #Kamus Lokal
    #Fungsi dan prosedur
        #menu:berfungsi untuk menampilkan menu menyalakan atau mematikan notifikasi
        #notifStart: prosedur yang berfungsi untuk memutar notifikasi saat microwave mulai MEMASAK
        #notifDone: prosedur yang berfungsi untuk memutar notifikasi saat microwave selesai MEMASAK
        #notifAlmostDone: prosedur yang berfungsi untuk memutar notifikasi saat microwave hampir selesai MEMASAK (30 detik sebelum selesai)
        #notifChildLock: prosedur yang berfungsi untuk memutar notifikasi saat mengaktifkan/menonakitfkan mode ChildLock
        #notifWrong: prosedur yang berfungsi untuk memutar notifikasi saat salah memasukan pin ChildLock
    def menu():
        #Kamus Lokal
        #Variabel
        
        print(f'======================================')
        print(f'||0. OFF          ||1. ON           ||')
        print(f'======================================')
    def notifStart():
        #Kamus Lokal
        #Variabel
            #filename(file): berisi file suara(notifikasi atau musik) yang akan diputar
            #play_obj(media player): memutar musik atau notifikasi
            #wave_obj: mendeteksi(decode) dan menyimpan file kedalam format wav
        filename = 'Sound\\Start.wav' #panggil(load) file notifikasi yang digunakan
        wave_obj = sa.WaveObject.from_wave_file(filename) #detect file sebagai obejek wave file
        play_obj = wave_obj.play() #jalankan fungsi play (mainkan)
        play_obj #mainkan file
    def notifDone():
        #Kamus Lokal
        #Variabel
            #filename(file): berisi file suara(notifikasi atau musik) yang akan diputar
            #play_obj(media player): memutar musik atau notifikasi
            #wave_obj: mendeteksi(decode) dan menyimpan file kedalam format wav
        filename = 'Sound\\Done.wav'#panggil(load) file notifikasi yang digunakan
        wave_obj = sa.WaveObject.from_wave_file(filename) #detect file sebagai obejek wave file
        play_obj = wave_obj.play() #jalankan fungsi play (mainkan)
        play_obj.wait_done() #mainkan file(sampai selesai)
    def notifAlmostDone():
        #Kamus Lokal
        #Variabel
            #filename(file): berisi file suara(notifikasi atau musik) yang akan diputar
            #play_obj(media player): memutar musik atau notifikasi
            #wave_obj: mendeteksi(decode) dan menyimpan file kedalam format wav
        filename = 'Sound\\AlmostDone.wav' #panggil(load) file notifikasi yang digunakan
        wave_obj = sa.WaveObject.from_wave_file(filename) #detect file sebagai obejek wave file
        play_obj = wave_obj.play() #jalankan fungsi play (mainkan)
        play_obj.wait_done() #mainkan file(sampai selesai)
    def notifChildLock():
        #Kamus Lokal
        #Variabel
            #filename(file): berisi file suara(notifikasi atau musik) yang akan diputar
            #play_obj(media player): memutar musik atau notifikasi
            #wave_obj: mendeteksi(decode) dan menyimpan file kedalam format wav
        filename = 'Sound\\ChildLock.wav' #panggil(load) file notifikasi yang digunakan
        wave_obj = sa.WaveObject.from_wave_file(filename) #detect file sebagai obejek wave file
        play_obj = wave_obj.play() #jalankan fungsi play (mainkan)
        play_obj #mainkan file
    def notifWrong():
        #Kamus Lokal
        #Variabel
            #filename(file): berisi file suara(notifikasi atau musik) yang akan diputar
            #play_obj(media player): memutar musik atau notifikasi
            #wave_obj: mendeteksi(decode) dan menyimpan file kedalam format wav
        filename = 'Sound\\Wrong.wav'#panggil(load) file notifikasi yang digunakan
        wave_obj = sa.WaveObject.from_wave_file(filename) #detect file sebagai obejek wave file
        play_obj = wave_obj.play() #jalankan fungsi play (mainkan)
        play_obj #mainkan file
        
class music(): #Kelas ini digunakan untuk memutar musik
    #Kamus Lokal
    #Fungsi dan prosedur
        #menu1: berfungsi untuk menampilkan menu memutar atau mematikan musik
        #menu2: berfungsi untuk menampilkan menu memilih musik yang ingin diputar
        #music1: prosedur yang berfungsi untuk memutar musik ke-1
        #music2: prosedur yang berfungsi untuk memutar musik ke-2
        #music3: prosedur yang berfungsi untuk memutar musik ke-3
    def menu1():
        #Kamus Lokal
        #Variabel
        
        print(f'======================================')
        print(f'||1. Play Music   ||0. Stop Music   ||')
        print(f'======================================')
    def menu2():
        #Kamus Lokal
        #Variabel

        print(f'======================================')
        print(f'||1. Music 1      ||2. Music 2      ||')
        print(f'||==================================||')
        print(f'||3. Music 3      ||0. Kembali      ||')
        print(f'======================================')
    def music1():
        #Kamus Lokal
        #Variabel
            #filename(file): berisi file suara(notifikasi atau musik) yang akan diputar
            #play_obj(media player): memutar musik atau notifikasi
            #wave_obj: mendeteksi(decode) dan menyimpan file kedalam format wav
        filename = 'Sound\\Music1.wav' #panggil(load) file notifikasi yang digunakan
        wave_obj = sa.WaveObject.from_wave_file(filename) #detect file sebagai obejek wave file
        play_obj = wave_obj.play() #jalankan fungsi play (mainkan)
        play_obj #mainkan file
    def music2():
        #Kamus Lokal
        #Variabel
            #filename(file): berisi file suara(notifikasi atau musik) yang akan diputar
            #play_obj(media player): memutar musik atau notifikasi
            #wave_obj: mendeteksi(decode) dan menyimpan file kedalam format wav
        filename = 'Sound\\Music2.wav' #panggil(load) file notifikasi yang digunakan
        wave_obj = sa.WaveObject.from_wave_file(filename) #detect file sebagai obejek wave file
        play_obj = wave_obj.play() #jalankan fungsi play (mainkan)
        play_obj #mainkan file
    def music3():
        #Kamus Lokal
        #Variabel
            #filename(file): berisi file suara(notifikasi atau musik) yang akan diputar
            #play_obj(media player): memutar musik atau notifikasi
            #wave_obj: mendeteksi(decode) dan menyimpan file kedalam format wav
        filename = 'Sound\\Music3.wav' #panggil(load) file notifikasi yang digunakan
        wave_obj = sa.WaveObject.from_wave_file(filename) #detect file sebagai obejek wave file
        play_obj = wave_obj.play() #jalankan fungsi play (mainkan)
        play_obj #mainkan file

stop = False 
class Microwave(comp): #Kelas ini merupakan anakan kelas comp yang digunakan untuk melakukan display interface dan pemasakan pada microwave, serta untuk memulai penggunaan microwave
    #Kamus Lokal
    #Fungsi dan prosedur
        #__init__: berfungsi untuk mendefinisikan parameter yang akan digunakan dalam class 
        #displayup: berfungsi sebagai batas atas pada display layar microwave
        #displaydown: berfungsi sebagai batas bawah pada display layar microwave
        #display1: berfungsi untuk memberikan tampilan awal saat microwave dijalakan atau direstart(start display)
        #display2: berfungsi untuk memberikan tampilan saat microwave sedang melakuakn proses memasak, menampilkan suhu terkini, sisa waktu, dan temperatur terkini.
        #displayCooling: berfungsi untuk meberikan tampilan saat microwave menjalankan fungsi Cooling
        #displayClean: berfungsi untuk meberikan tampilan saat microwave menjalankan fungsi Cleaning
        #displayCoolingDone: berfungsi untuk meberikan tampilan saat microwave selesai menjalankan fungsi Cooling
        #displayCleanDone: berfungsi untuk meberikan tampilan saat microwave selesai menjalankan fungsi Cleaning
        #displayundercooked: berfungsi untuk memberikan tampilan saat makanan yang dimasak Undercooked (kelembapan lebih dari 75%)
        #displayover: berfungsi untuk memberikan tampilan saat makanan yang dimasak overcooked (kelembapan kurang dari 40%)
        #displaydry: berfungsi untuk memberikan tampilan saat makanan yang dimasak sudah kering (kelembapan 0%)
        #displaydone: berfungsi untuk memberikan tampilan saat makanan yang dimasak sudah matang sempurna
        #menu: menampilkan pilihan menu dari fitur microwave yang dapat dijalankan
        #menulock: menampilkan pilihan menu dari fitur microwave ketika dalam mode Child Lock
        #Start: berisi logika utama dalam menjalankan semua fitur mikrowave serta memproses input dan output user
        
    def __init__(self, time, temp, moisture): #Seperti kelas comp, kelas seafood ini juga memiliki nilai waktu, temperatur, dan kelembaban yang disimpan dalam variabel self
        #Kamus Lokal
        #Variabel
            #moisture(int): menyimpan pengaturan kelembapan microwave
            #temp(int): menyimpan pengaturan suhu microwave
            #time(int): menyimpan pengaturan waktu microwave
        super().__init__(time, temp, moisture)
    def displayup(): #Fungsi ini merupakan fungsi untuk menampilakn display bagian atas microwave
        #Kamus Lokal
        #Variabel
        
        print('='*38)
        print('||',end='')
        print('='*18,end='')
        print('||',end='')
        print('='*14,end='')
        print('||')
    def displaydown(): #Fungsi ini merupakan fungsi untuk menampilakn display bagian bawah microwave
        #Kamus Lokal
        #Variabel
        
        print('||',end='')
        print('='*18,end='')
        print('||',end='')
        print('='*14,end='')
        print('||')
        print('='*38)
    def display1(): #Fungsi ini adalah fungsi untuk menampilkan interface / menu utama dari microwave
        #Kamus Lokal
        #Variabel
            #notification(boolean)[Global Variabel]: parameter notifikasi nyala(True) atau mati(False)
            #side_h(int): menyimpan nilai batas horizontal dislpay
            #side_v(int): menyimpan nilai batas vertikal dislpay
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        print(f'Temp || --- ||',end='')
                    elif side_v == 5:
                        print(f'Time ||--:--||',end='')
                    elif side_v == 4:
                        print(f'Mois || --- ||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        if notification == True:
                            print("|1|3|4|5|6|ON ",end='')
                        else:
                            print("|1|3|4|5|6|OFF",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                    #Display ini menunjukkan fungsi-fungsi atau fitur-fitur yang dapat dipilih oleh user untuk digunakan
                side_h-=1
            side_v-=1
        Microwave.displaydown()

        #Saat Notifikasi dinyalkan Tamplian menu utama microwave akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || --- ||||
        # ||                  ||Time ||--:--||||
        # ||                  ||Mois || --- ||||
        # ||                  || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|ON ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu :
        
        #Saat Notifikasi dimatikan Tamplian menu utama microwave akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || --- ||||
        # ||                  ||Time ||--:--||||
        # ||                  ||Mois || --- ||||
        # ||                  || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|OFF||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu :

    def display2(self): #Fungsi ini adalah fungsi untuk menampilkan keadaan microwave saat sedang melakukan pemasakan
        #Kamus Lokal
        #Variabel
            #min(int): menyimpan nilai menit waktu memasak(hasil pembagian time dengan 60)
            #moisture(int): menyimpan pengaturan kelembapan microwave
            #notification(boolean)[Global Variabel]: parameter notifikasi nyala(True) atau mati(False)
            #sec(int): menyimpan nilai detik waktu memasak(sisa pembagian time dengan 60)
            #side_h(int): menyimpan nilai batas horizontal dislpay
            #side_v(int): menyimpan nilai batas vertikal dislpay
            #stop(boolean)[Global Variabel]: parameter untuk mendeteksi apakah microwave dihentikan saat sedang berjalan atau tidak
            #wait(int): menyimpan countdown untuk mematikan microwave secara otomatis setelah watu memasak selesai
        try: #jalankan fungsi
            global notification #code untuk merubah parameter dari variabel global
            while self.time >= 0:
                moisture = self.moisture + (self.temp/1500)*self.time
                if (notification == True): 
                    if ( 0 < self.time < 30 or moisture < 20):
                        notif.notifAlmostDone()
                os.system('cls')
                Microwave.displayup()
                side_v = 6
                while side_v>0:
                    side_h = 38
                    while side_h>0:
                        if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                            print('|', end='')
                        elif (side_h == 1):
                            print('|')
                        elif side_h<37 and side_h>18:
                            print(' ',end='')
                        elif side_h == 16:
                            if side_v == 6:
                                if self.temp < 10:
                                    print(f'Temp || {self.temp}°C ||',end='')
                                elif self.temp < 100:
                                    print(f'Temp || {self.temp}°C||',end='')
                                else:
                                    print(f'Temp ||{self.temp}°C||',end='')
                            elif side_v == 5:
                                min, sec = divmod(self.time, 60)
                                print(f'Time ||{min:02d}:{sec:02d}||',end='')
                                #Fungsi ini menampilkan display secara dinamis dengan menunjukkan countdown waktu pemasakan dan pengurangan nilai kelembaban
                            elif side_v == 4:
                                if moisture <10:
                                    print(f'Mois ||   {int(round(moisture, 0))}%||',end='')
                                elif moisture<100:
                                    print(f'Mois ||  {int(round(moisture, 0))}%||',end='')
                                else:
                                    moisture = 100
                                    print(f'Mois || {int(round(moisture, 0))}%||',end='')
                            elif side_v == 3:
                                print(" _ _ _ _ _ ___",end='')
                            elif side_v == 2:
                                if notification == True:
                                    print("|1|3|4|5|6|ON ",end='')
                                else:
                                    print("|1|3|4|5|6|OFF",end='')
                            else:
                                print("|7|8|0| 99|___",end='')
                        side_h-=1
                    side_v-=1
                Microwave.displaydown()
                if (notification == True) and (self.time == 0):
                    try: 
                        wait = 5 # tunggu 5 kali notif (5 detik)
                        while wait > 0:
                            notif.notifDone()
                            wait -= 1
                    except KeyboardInterrupt:
                        pass
                if (notification == True) and (self.time < 30 or moisture < 20):
                    time.sleep(0.01)
                else:
                    time.sleep(0.01)
                self.time -= 1
        except KeyboardInterrupt: #dijalankan jika program diInterrupt(CTRL + C) saat masih berjalan
            if self.time > 0:
                global stop #code untuk merubah parameter dari variabel global
                stop = True

                os.system('cls')
                Microwave.displayup()
                side_v = 6
                while side_v>0:
                    side_h = 38
                    while side_h>0:
                        if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                            print('|', end='')
                        elif (side_h == 1):
                            print('|')
                        elif side_h<37 and side_h>18:
                            print(' ',end='')
                        elif side_h == 16:
                            if side_v == 6:
                                if self.temp < 10:
                                    print(f'Temp || {self.temp}°C ||',end='')
                                elif self.temp < 100:
                                    print(f'Temp || {self.temp}°C||',end='')
                                else:
                                    print(f'Temp ||{self.temp}°C||',end='')
                            elif side_v == 5:
                                min, sec = divmod(self.time, 60)
                                print(f'Time ||{min:02d}:{sec:02d}||',end='')
                                #Fungsi ini menampilkan display secara dinamis dengan menunjukkan countdown waktu pemasakan dan pengurangan nilai kelembaban
                            elif side_v == 4:
                                moisture = self.moisture + (self.temp/1500)*self.time
                                if moisture <10:
                                    print(f'Mois ||   {int(round(moisture, 0))}%||',end='')
                                elif moisture<100:
                                    print(f'Mois ||  {int(round(moisture, 0))}%||',end='')
                                else:
                                    moisture = 100
                                    print(f'Mois || {int(round(moisture, 0))}%||',end='')
                            elif side_v == 3:
                                print(" _ _ _ _ _ ___",end='')
                            elif side_v == 2:
                                if notification == True:
                                    print("|1|3|4|5|6|ON ",end='')
                                else:
                                    print("|1|3|4|5|6|OFF",end='')
                            else:
                                print("|7|8|0| 99|___",end='')
                        side_h-=1
                    side_v-=1
                Microwave.displaydown()
            else:
                notif.notifDone().stop()
        
        #Tampilan microwave saat ditengah-tengah pemasakan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp ||500°C||||
        # ||                  ||Time ||01:03||||
        # ||                  ||Mois ||  46%||||
        # ||                  || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|ON ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
    def displayCooling(self):
        #Kamus Lokal
        #Variabel
            #min(int): menyimpan nilai menit waktu memasak(hasil pembagian time dengan 60)
            #notification(boolean)[Global Variabel]: parameter notifikasi nyala(True) atau mati(False)
            #sec(int): menyimpan nilai detik waktu memasak(sisa pembagian time dengan 60)
            #side_h(int): menyimpan nilai batas horizontal dislpay
            #side_v(int): menyimpan nilai batas vertikal dislpay
         while self.time >= 0:
            os.system('cls')
            Microwave.displayup()
            side_v = 6
            while side_v>0:
                side_h = 38
                while side_h>0:
                    if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                        print('|', end='')
                    elif (side_h == 1):
                        print('|')
                    elif side_h<37 and side_h>18:
                        print(' ',end='')
                    elif side_h == 16:
                        if side_v == 6:
                            print(f'Temp || --- ||',end='')
                        elif side_v == 5:
                            min, sec = divmod(self.time, 60)
                            print(f'Time ||{min:02d}:{sec:02d}||',end='')
                        elif side_v == 4:
                            print(f'Mois || --- ||',end='')
                        elif side_v == 3:
                            print(" _ _ _ _ _ ___",end='')
                        elif side_v == 2:
                            if notification == True:
                                print("|1|3|4|5|6|ON ",end='')
                            else:
                                print("|1|3|4|5|6|OFF",end='')
                        else:
                            print("|7|8|0| 99|___",end='')
                    side_h-=1
                side_v-=1
            Microwave.displaydown()
            time.sleep(0.001) 
            self.time -= 1
     # Tamplian menu Saat Pembersihan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || --- ||||
        # ||                  ||Time ||02:00||||
        # ||                  ||Mois || --- ||||
        # ||                  || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|ON ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        
    def displayClean(self):
        #Kamus Lokal
        #Variabel
            #min(int): menyimpan nilai menit waktu memasak(hasil pembagian time dengan 60)
            #notification(boolean)[Global Variabel]: parameter notifikasi nyala(True) atau mati(False)
            #sec(int): menyimpan nilai detik waktu memasak(sisa pembagian time dengan 60)
            #side_h(int): menyimpan nilai batas horizontal dislpay
            #side_v(int): menyimpan nilai batas vertikal dislpay
         while self.time >= 0:
            os.system('cls')
            Microwave.displayup()
            side_v = 6
            while side_v>0:
                side_h = 38
                while side_h>0:
                    if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                        print('|', end='')
                    elif (side_h == 1):
                        print('|')
                    elif side_h<37 and side_h>18:
                        print(' ',end='')
                    elif side_h == 16:
                        if side_v == 6:
                            print(f'Temp || --- ||',end='')
                        elif side_v == 5:
                            min, sec = divmod(self.time, 60)
                            print(f'Time ||{min:02d}:{sec:02d}||',end='')
                        elif side_v == 4:
                            print(f'Mois || --- ||',end='')
                        elif side_v == 3:
                            print(" _ _ _ _ _ ___",end='')
                        elif side_v == 2:
                            if notification == True:
                                print("|1|3|4|5|6|ON ",end='')
                            else:
                                print("|1|3|4|5|6|OFF",end='')
                        else:
                            print("|7|8|0| 99|___",end='')
                    side_h-=1
                side_v-=1
            Microwave.displaydown()
            time.sleep(0.001) 
            self.time -= 1
            
        # Tamplian menu Saat Pembersihan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || --- ||||
        # ||                  ||Time ||02:00||||
        # ||                  ||Mois || --- ||||
        # ||                  || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|ON ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
      
    def displayCleanDone():
        #Kamus Lokal
        #Variabel
            #notification(boolean)[Global Variabel]: parameter notifikasi nyala(True) atau mati(False)
            #side_h(int): menyimpan nilai batas horizontal dislpay
            #side_v(int): menyimpan nilai batas vertikal dislpay
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>31 or side_h<23:
                            print(' ',end='')
                        elif side_h == 31:
                            print("Microwave", end='')
                    elif side_v == 3:
                        if side_h>35 or side_h<20:
                            print(' ',end='')
                        elif side_h == 35:
                            print("telah dibersikan", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        print(f'Temp || --- ||',end='')
                    elif side_v == 5:
                        print(f'Time ||00:00||',end='')
                    elif side_v == 4:
                        print(f'Mois || --- ||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        if notification == True:
                            print("|1|3|4|5|6|ON ",end='')
                        else:
                            print("|1|3|4|5|6|OFF",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()
        
        # Tamplian menu setelah Pembersihan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || --- ||||
        # ||                  ||Time ||00:00||||
        # ||    Microwave     ||Mois || --- ||||
        # || telah dibersikan || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|ON ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu :
    
    def displayCoolingDone():
        #Kamus Lokal
        #Variabel
            #notification(boolean)[Global Variabel]: parameter notifikasi nyala(True) atau mati(False)
            #side_h(int): menyimpan nilai batas horizontal dislpay
            #side_v(int): menyimpan nilai batas vertikal dislpay
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>31 or side_h<23:
                            print(' ',end='')
                        elif side_h == 31:
                            print("Microwave", end='')
                    elif side_v == 3:
                        if side_h>35 or side_h<19:
                            print(' ',end='')
                        elif side_h == 35:
                            print("telah didinginkan", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        print(f'Temp || --- ||',end='')
                    elif side_v == 5:
                        print(f'Time ||00:00||',end='')
                    elif side_v == 4:
                        print(f'Mois || --- ||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        if notification == True:
                            print("|1|3|4|5|6|ON ",end='')
                        else:
                            print("|1|3|4|5|6|OFF",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()
        
        # Tamplian menu setelah Pembersihan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || --- ||||
        # ||                  ||Time ||00:00||||
        # ||    Microwave     ||Mois || --- ||||
        # || telah didinginkan|| _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|ON ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu :
       
    def displayundercooked(self): #Fungsi ini adalah fungsi untuk menampilkan hasil pemasakan yang "overcooked" dan juga menampilkan kembali menu utama microwave
        #Kamus Lokal
        #Variabel
            #min(int): menyimpan nilai menit waktu memasak(hasil pembagian time dengan 60)
            #notification(boolean)[Global Variabel]: parameter notifikasi nyala(True) atau mati(False)
            #sec(int): menyimpan nilai detik waktu memasak(sisa pembagian time dengan 60)
            #side_h(int): menyimpan nilai batas horizontal dislpay
            #side_v(int): menyimpan nilai batas vertikal dislpay
            #stop(boolean)[Global Variabel]: parameter untuk mendeteksi apakah microwave dihentikan saat sedang berjalan atau tidak
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>29 or side_h<25:
                            print(' ',end='')
                        elif side_h == 29:
                            print("UNDER", end='')
                    elif side_v == 3:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("COOK", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        if self.temp < 10:
                            print(f'Temp || {self.temp}°C ||',end='')
                        elif self.temp < 100:
                            print(f'Temp || {self.temp}°C||',end='')
                        else:
                            print(f'Temp ||{self.temp}°C||',end='')
                    elif side_v == 5:
                        if stop == False:
                            print(f'Time ||00:00||',end='')
                        else:
                            min, sec = divmod(self.time, 60)
                            print(f'Time ||{min:02d}:{sec:02d}||',end='')
                    elif side_v == 4:
                        if self.moisture<10:
                            print(f'Mois ||   {int(round(self.moisture, 0))}%||',end='')
                        else:
                            print(f'Mois ||  {int(round(self.moisture, 0))}%||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        if notification == True:
                            print("|1|3|4|5|6|ON ",end='')
                        else:
                            print("|1|3|4|5|6|OFF",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()

        # Tamplian menu setelah pemasakan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || 300°C|||
        # ||                  ||Time ||00:00||||
        # ||       UNDER      ||Mois ||  1 %||||
        # ||       COOK       || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|ON ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu : 
   
    def displayover(self): #Fungsi ini adalah fungsi untuk menampilkan hasil pemasakan yang "overcooked" dan juga menampilkan kembali menu utama microwave
        #Kamus Lokal
        #Variabel
            #min(int): menyimpan nilai menit waktu memasak(hasil pembagian time dengan 60)
            #notification(boolean)[Global Variabel]: parameter notifikasi nyala(True) atau mati(False)
            #sec(int): menyimpan nilai detik waktu memasak(sisa pembagian time dengan 60)
            #side_h(int): menyimpan nilai batas horizontal dislpay
            #side_v(int): menyimpan nilai batas vertikal dislpay
            #stop(boolean)[Global Variabel]: parameter untuk mendeteksi apakah microwave dihentikan saat sedang berjalan atau tidak
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("OVER", end='')
                    elif side_v == 3:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("COOK", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        if self.temp < 10:
                            print(f'Temp || {self.temp}°C ||',end='')
                        elif self.temp < 100:
                            print(f'Temp || {self.temp}°C||',end='')
                        else:
                            print(f'Temp ||{self.temp}°C||',end='')
                    elif side_v == 5:
                        if stop == False:
                            print(f'Time ||00:00||',end='')
                        else:
                            min, sec = divmod(self.time, 60)
                            print(f'Time ||{min:02d}:{sec:02d}||',end='')
                    elif side_v == 4:
                        if self.moisture<10:
                            print(f'Mois ||   {int(round(self.moisture, 0))}%||',end='')
                        else:
                            print(f'Mois ||  {int(round(self.moisture, 0))}%||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        if notification == True:
                            print("|1|3|4|5|6|ON ",end='')
                        else:
                            print("|1|3|4|5|6|OFF",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()

        # Tamplian menu setelah pemasakan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || 300°C|||
        # ||                  ||Time ||00:00||||
        # ||       OVER       ||Mois ||  1 %||||
        # ||       COOK       || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|ON ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu : 

    def displaydry(self): #Fungsi ini adalah fungsi untuk menampilkan hasil pemasakan yang "dry cook" dan juga menampilkan kembali menu utama microwave
        #Kamus Lokal
        #Variabel
            #min(int): menyimpan nilai menit waktu memasak(hasil pembagian time dengan 60)
            #notification(boolean)[Global Variabel]: parameter notifikasi nyala(True) atau mati(False)
            #sec(int): menyimpan nilai detik waktu memasak(sisa pembagian time dengan 60)
            #side_h(int): menyimpan nilai batas horizontal dislpay
            #side_v(int): menyimpan nilai batas vertikal dislpay
            #stop(boolean)[Global Variabel]: parameter untuk mendeteksi apakah microwave dihentikan saat sedang berjalan atau tidak
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>29 or side_h<27:
                            print(' ',end='')
                        elif side_h == 29:
                            print("DRY", end='')
                    elif side_v == 3:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("COOK", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        if self.temp < 10:
                            print(f'Temp || {self.temp}°C ||',end='')
                        elif self.temp < 100:
                            print(f'Temp || {self.temp}°C||',end='')
                        else:
                            print(f'Temp ||{self.temp}°C||',end='')
                    elif side_v == 5:
                        if stop == False:
                            print(f'Time ||00:00||',end='')
                        else:
                            min, sec = divmod(self.time, 60)
                            print(f'Time ||{min:02d}:{sec:02d}||',end='')
                    elif side_v == 4:
                        if self.moisture<10:
                            print(f'Mois ||   {int(round(self.moisture, 0))}%||',end='')
                        else:
                            print(f'Mois ||  {int(round(self.moisture, 0))}%||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        if notification == True:
                            print("|1|3|4|5|6|ON ",end='')
                        else:
                            print("|1|3|4|5|6|OFF",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()

        # Tamplian menu setelah pemasakan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || 200°C|||
        # ||                  ||Time ||00:00||||
        # ||       DRY        ||Mois ||  25%||||
        # ||       COOK       || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|ON ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu : 

    def displaydone(self): #Fungsi ini adalah fungsi untuk menampilkan hasil pemasakan yang baik (well done) dan juga menampilkan kembali menu utama microwave
        #Kamus Lokal
        #Variabel
            #min(int): menyimpan nilai menit waktu memasak(hasil pembagian time dengan 60)
            #notification(boolean)[Global Variabel]: parameter notifikasi nyala(True) atau mati(False)
            #sec(int): menyimpan nilai detik waktu memasak(sisa pembagian time dengan 60)
            #side_h(int): menyimpan nilai batas horizontal dislpay
            #side_v(int): menyimpan nilai batas vertikal dislpay
            #stop(boolean)[Global Variabel]: parameter untuk mendeteksi apakah microwave dihentikan saat sedang berjalan atau tidak
        Microwave.displayup()
        side_v = 6
        while side_v>0:
            side_h = 38
            while side_h>0:
                if (side_h == 38) or (side_h == 37) or (side_h == 18) or (side_h == 17) or (side_h == 2):
                    print('|', end='')
                elif (side_h == 1):
                    print('|')
                elif side_h<37 and side_h>18:
                    if side_v == 4:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("WELL", end='')
                    elif side_v == 3:
                        if side_h>29 or side_h<26:
                            print(' ',end='')
                        elif side_h == 29:
                            print("DONE", end='')
                    else:
                        print(' ',end='')
                elif side_h == 16:
                    if side_v == 6:
                        if self.temp < 10:
                            print(f'Temp || {self.temp}°C ||',end='')
                        elif self.temp < 100:
                            print(f'Temp || {self.temp}°C||',end='')
                        else:
                            print(f'Temp ||{self.temp}°C||',end='')
                    elif side_v == 5:
                        if stop == False:
                            print(f'Time ||00:00||',end='')
                        else:
                            min, sec = divmod(self.time, 60)
                            print(f'Time ||{min:02d}:{sec:02d}||',end='')
                    elif side_v == 4:
                        if self.moisture<10:
                            print(f'Mois ||   {int(round(self.moisture, 0))}%||',end='')
                        else:
                            print(f'Mois ||  {int(round(self.moisture, 0))}%||',end='')
                    elif side_v == 3:
                        print(" _ _ _ _ _ ___",end='')
                    elif side_v == 2:
                        if notification == True:
                            print("|1|3|4|5|6|ON ",end='')
                        else:
                            print("|1|3|4|5|6|OFF",end='')
                    else:
                        print("|7|8|0| 99|___",end='')
                side_h-=1
            side_v-=1
        Microwave.displaydown()

        # Tamplian menu setelah pemasakan akan terlihat seperti ini
        # ======================================
        # ||==================||==============||
        # ||                  ||Temp || 70°C||||
        # ||                  ||Time ||00:00||||
        # ||       WELL       ||Mois ||  80%||||
        # ||       DONE       || _ _ _ _ _ ___||
        # ||                  |||1|3|4|5|6|ON ||
        # ||                  |||7|8|0| 99|___||
        # ||==================||==============||
        # ======================================
        # ======================================
        # ||1. Manual mode  ||6. Seafood      ||
        # ||==================================||
        # ||2. Quick Heat   ||7. input kode   ||
        # ||==================================||
        # ||3. Defrost      ||8. Cleaning     ||
        # ||==================================||
        # ||4. Grill        ||0. Stop         ||
        # ||==================================||
        # ||5. Vegetable    ||99. Child Lock  ||
        # ||==================================||
        # Pilih menu : 

    def menu(): #Fungsi ini digunakan untuk menampilkan menu utama microwave dalam keadaan normal
        #Kamus Lokal
        #Variabel
           
        print(f'======================================')
        print(f'||1. Manual mode  ||8. Media Player ||')
        print(f'||==================================||')
        print(f'||2. Quick Heat   ||9. Cleaning     ||')
        print(f'||==================================||')
        print(f'||3. Defrost      ||10. Cooling     ||')
        print(f'||==================================||')
        print(f'||4. Grill        ||11. Notif       ||')
        print(f'||==================================||')
        print(f'||5. Vegetable    ||0. Stop         ||')
        print(f'||==================================||')
        print(f'||6. Seafood      ||99. Child Lock  ||')
        print(f'||==================================||')
        print(f'||7. input kode   ||                ||')
        print(f'======================================')
    def menulock(): #Fungsi ini digunakan untuk menampilkan menu utama microwave dalam keadaan child lock
        #Kamus Lokal
        #Variabel
         
        print(f'======================================')
        print(f'||1. Manual mode🔒||8.Media Player🔒||')
        print(f'||==================================||')
        print(f'||2. Quick Heat🔒 ||9. Cleaning🔒   ||')
        print(f'||==================================||')
        print(f'||3. Defrost🔒    ||10. Cooling🔒   ||')
        print(f'||==================================||')
        print(f'||4. Grill🔒      ||11. Notif🔒     ||')
        print(f'||==================================||')
        print(f'||5. Vegetable🔒  ||0. Stop🔒       ||')
        print(f'||==================================||')
        print(f'||6. Seafood🔒    ||99.Child Lock🔒 ||')
        print(f'||==================================||')
        print(f'||7. input kode🔒 ||                ||')
        print(f'======================================')

    def Start(): #Fungsi start ini adalah fungsi utama dalam program microwave ini, fungsi ini mengintegrasikan semua fungsi-fungsi yang ada untuk user menggunakan microwave
        #Kamus Lokal
        #Variabel
            #aturulang(string(char)): menyimpan konfirmasi dari user untuk memasak ulang atau tidak (ganti waktu dan suhu)
            #ChildLock(boolean): parameter mode Child lock(true jika sedang dalam mode child lock)
            #choice(int): menyimpan pilihan fitur yang akan digunakan user
            #confirm(string): menyimpan inputan user terkait konfirmasi nama makanan yang akan dimasak melalui fitur scan barcode
            #moisture(int): menyimpan pengaturan kelembapan microwave
            #musicchoice(int): menyimpan pilihan user pada menu media player
            #notification(boolean)[Global Variabel]: parameter notifikasi nyala(True) atau mati(False)
            #notifchoice(int): menyimpan pilihan user pada menu Notif
            #pin(int) = menyimpan PIN yang dimasukan user saat microwave sedang dalam mode Child Lock
            #pinlock(int): menyimpan PIN yang digunakan pada mode Child Lock
            #sayur(int): menyimpan pilihan mode memasak sayuran yang akan digunakan user
            #seaf(int): menyimpan pilihan mode memasak seafood yang akan digunakan user
            #stop(boolean)[Global Variabel]: parameter untuk mendeteksi apakah microwave dihentikan saat sedang berjalan atau tidak
            #temp(int): menyimpan pengaturan suhu microwave
            #time(int): menyimpan pengaturan waktu microwave
        #Objek
            #clean(Microwave): object class Microwave, untuk menggunakan metode(fungsi) Cleaning pada class Microwave
            #cooling(Microwave): object class Microwave, untuk menggunakan metode(fungsi) cooling pada class Microwave
            #food(mode): object class mode, untuk menggunakan metode(fungsi) pada class mode
            #food(incode): object class incode, untuk menggunakan metode(fungsi) pada class incode
            #seafd(seafood): object class seafood, untuk menggunakan metode(fungsi) pada class seafood
            #vegen(vegetable): object class vegetable, untuk menggunakan metode(fungsi) pada class vegetable
        ChildLock = False #Awalnya mode childlock dalam keadaan tidak aktif
        Microwave.display1() #Menampilkan menu utama microwave
        global stop #code untuk merubah parameter dari variabel global
        global notification #code untuk merubah parameter dari variabel global
        while True: #Selama user masih mau menggunakan microwave
            if ChildLock == False:
                if stop == False: #dijalankan ketika microwave berjalan seperti biasa
                    Microwave.menu() #Microwave menampilan menu-menu yang dapat dipilih oleh user
                    choice = int(input("Pilih menu : ")) #User menginput menu yang ingin digunakan
                else: #dijalankan ketika microwave di hentikan saat masih memasak
                    if choice == 1: #jika dalam mode manual cook, maka akan ada fitur atur ulang suhu dan waktu memasak
                        stop = False
                        aturulang = input("Apakah anda ingin mengatur ulang Suhu dan Waktu?(Y/N): ").lower()
                        if aturulang == 'y': #menjalankan kembali fungsi manual cook jika user ingin mengatur ulang waktu dan suhu
                            choice = 1
                        else:
                            os.system('cls')
                            Microwave.display1()
                            Microwave.menu()
                            choice = int(input("Pilih menu : ")) #User menginput menu yang ingin digunakan
                    else:
                        Microwave.menu()
                        stop = False
                        choice = int(input("Pilih menu : ")) #User menginput menu yang ingin digunakan
                os.system('cls')
                if choice == 1: #User memilih untuk menggunakan mode manual
                    Microwave.display1()
                    #User memasukkan nilai waktu dan temperatur pemasakan sesuai kehendaknya
                    time = int(input("Masukan waktu Memasak(menit) : "))
                    temp = int(input("Masukan Temperatur(°C) : "))
                    if notification == True:
                        notif.notifStart()
                    moisture = 100
                    food = Microwave(time, temp, moisture)
                    food.moisture1(0.8)
                    food.display2()
                    if food.moisture < 1: #Apabila pada akhir pemasakan kelembabannya kurang dari 1% maka hasil pemasakan menjadi kering
                        os.system('cls')
                        food.displaydry()
                    elif food.moisture < 40: #Apabila pada akhir pemasakan kelembabannya kurang dari 40% maka hasil pemasakan menjadi overcooked
                        os.system('cls')
                        food.displayover()
                    elif food.moisture < 76: #Apabila pada akhir pemasakan kelembabannya kurang dari 76% maka hasil pemasakan baik (well-done)
                        os.system('cls')
                        food.displaydone()
                    else:    #Apabila pada akhir pemasakan kelembabannya lebih dari 76% maka hasil pemasakan UnderCooked
                        os.system('cls')
                        food.displayundercooked()
                elif choice == 2: #User memilih untuk menggunakan mode quick heat untuk memanaskan makanan
                    food = mode(2, 150, 90) #Mode ini berjalan selama 2 menit dengan temperatur 150 derajat celsius dan kelembaban awal 90%
                    if notification == True:
                        notif.notifStart()
                    food.quick_heat()
                elif choice == 3: #User memilih untuk menggunakan mode defrost untuk mencairkan makanan (terutama daging)
                    food = mode(8, 40, 90) #Mode ini berjalan selama 8 menit dengan temperatur 40 derajat celsius dan kelembaban awal 90%
                    if notification == True:
                        notif.notifStart()
                    food.Deforst() 
                elif choice == 4: #User memilih untuk menggunakan mode grill untuk memanggang makanan
                    food = mode(7, 230, 100) #Mode ini berjalan selama 7 menit dengan temperatur 230 derajat celsius dan kelembaban awal 100%
                    if notification == True:
                        notif.notifStart()
                    food.Grill()
                elif choice == 5: #User memilih untuk menggunakan mode memasak sayur
                    while True:
                        vegetable.menu() #Microwave menampilkan menu sayur yang tersedia
                        sayur = int(input("Pilih Sayur : ")) #User memasukkan pilihan sayur untuk dimasak
                        if notification == True:
                            notif.notifStart()
                        os.system('cls')
                        if sayur == 1: #Pilihan sayur pertama: brokoli, dengan lama pemasakan 2 menit, temperatur 200 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(2, 200, 100)
                            vegen.brokoli()
                            break
                        elif sayur == 2: #Pilihan sayur kedua: wortel, dengan lama pemasakan 4 menit, temperatur 200 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(4, 200, 100)
                            vegen.wortel()
                            break
                        elif sayur == 3: #Pilihan sayur ketiga: kembang kol, dengan lama pemasakan 4 menit, temperatur 180 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(4, 180, 100)
                            vegen.kembang_kol()
                            break
                        elif sayur == 4: #Pilihan sayur keempat: bayam, dengan lama pemasakan 3 menit, temperatur 160 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(3, 160, 100)
                            vegen.bayam()
                            break
                        elif sayur == 5: #Pilihan sayur kelima: jagung manis, dengan lama pemasakan 4 menit, temperatur 180 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(4, 180, 100)
                            vegen.jagung_manis()
                            break
                        elif sayur == 6: #Pilihan sayur keenam: paprika, dengan lama pemasakan 4 menit, temperatur 200 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(4, 200, 100)
                            vegen.paprika()
                            break
                        elif sayur == 7: #Pilihan sayur ketujuh: zucchini, dengan lama pemasakan 4 menit, temperatur 180 derajat celsius dan kelembaban awal 100%
                            vegen = vegetable(4, 180, 100)
                            vegen.zucchini()
                            break
                        elif sayur == 0:
                            Microwave.display1()
                            break
                elif choice == 6: #User memilih untuk menggunakan mode memasak seafood
                    while True:
                        seafood.menu() #Microwave menampilkan menu seafood yang tersedia
                        seaf = int(input("Pilih Seafood : ")) #User memasukkan pilihan seafood untuk dimasak
                        if notification == True:
                            notif.notifStart()
                        os.system('cls')
                        if seaf == 1: #Pilihan seafood pertama: ikan fillet, dengan lama pemasakan 5 menit, temperatur 90 derajat celsius dan kelembaban awal 100%
                            seafd = seafood(5, 90, 100)
                            seafd.fish()
                            break
                        elif seaf == 2: #Pilihan seafood kedua: udang, dengan lama pemasakan 3 menit, temperatur 80 derajat celsius dan kelembaban awal 100%
                            seafd = seafood(3, 80, 100)
                            seafd.shrimp()
                            break
                        elif seaf == 3: #Pilihan seafood ketiga: cumi-cumi, dengan lama pemasakan 3 menit, temperatur 80 derajat celsius dan kelembaban awal 100%
                            seafd = seafood(3, 80, 100)
                            seafd.squid()
                            break
                        elif seaf == 4: #Pilihan seafood keempat: kerang, dengan lama pemasakan 4 menit, temperatur 80 derajat celsius dan kelembaban awal 100%
                            seafd = seafood(4, 80, 100)
                            seafd.shellfish()
                            break
                        elif seaf == 5: #Pilihan seafood kelima: lobster, dengan lama pemasakan 7 menit, temperatur 90 derajat celsius dan kelembaban awal 100%
                            seafd = seafood(7, 90, 100)
                            seafd.lobster()
                            break
                        elif seaf == 0:
                            Microwave.display1()
                            break
                elif choice == 7: #User memilih untuk memasak paket makanan yang telah tersedia dari barcode
                    while True:
                        food = incode(0,0,0,0,0)
                        food.barcode = int(input("Masukan Code barcode: "))
                        food.detect(food.barcode)
                        if food.temp == 0:
                            os.system('cls')
                            Microwave.display1()
                            break
                        confirm = input(f'{food.foodname}? (y/n): ').lower()
                        if confirm == 'y':
                            if notification == True:
                                notif.notifStart()
                            food.cook()
                            break
                elif choice == 8: #User memilih untuk Memainkan Musik pada microwave
                    Microwave.display1()
                    music.menu1()
                    musicchoice = int(input("Masukan Pilihan : "))
                    os.system('cls')
                    if musicchoice == 1:
                        Microwave.display1()
                        music.menu2()
                        musicchoice = int(input("Masukan Pilihan : "))
                        if musicchoice == 1:
                            sa.stop_all()
                            music.music1()
                        elif musicchoice == 2:
                            sa.stop_all()
                            music.music2()
                        elif musicchoice == 3:
                            sa.stop_all()
                            music.music3()
                        else:
                            os.system('cls')
                            Microwave.display1()
                    elif musicchoice == 0:
                        sa.stop_all()
                    os.system('cls')
                    Microwave.display1()
                elif choice == 9:   #User memilih untuk melakukan pembersihan otomatis pada microwave
                    clean = Microwave(2,0,0)
                    clean.displayClean()
                    if notification == True:
                        notif.notifDone()
                    os.system('cls')
                    Microwave.displayCleanDone() #Microwave selesai dibersihkan
                elif choice == 10:   #User memilih untuk melakukan pendinginan otomatis pada microwave
                    cooling = Microwave(10,0,0)
                    cooling.displayCooling()
                    if notification == True:
                        notif.notifDone()
                    os.system('cls')
                    Microwave.displayCoolingDone() #Microwave selesai didinginkan
                elif choice == 11:   #User memilih untuk meyalakan atau mematikan notifikasi pada microwave
                    Microwave.display1()
                    notif.menu()
                    notifchoice = int(input("Masukan Pilihan : "))
                    os.system('cls')
                    if notifchoice == 1:
                        notification = True
                    elif notifchoice == 0:
                        notification = False
                    os.system('cls')
                    Microwave.display1()
                elif choice == 99: #User memilih untuk mengaktifkan mode child-lock
                    Pinlock = int(input("Atur PIN :")) #Set pin untuk digunakan pada penggunaan microwave selanjutnya
                    ChildLock = True #nyalakan parameter ChildLock
                    if notification == True:
                        notif.notifChildLock()
                    os.system('cls')
                elif choice == 0: #User memilih untuk selesai menggunakan microwave
                    print("Terima Kasih telah menggunakan produk kami hehehe")
                    break
            else: #Child lock = True
                Microwave.display1()
                Microwave.menulock() #Karena mode child-lock nya aktif, maka display microwave menjadi berubah (ada lambang gemboknya)
                pin = int(input("Masukan PIN :")) #Masukkan pin yang telah dibuat sebelumnya untuk dapat menggunakan microwave
                if pin == Pinlock: #Apabila pin yang dimasukkan benar, maka mode child-lock akan dinonaktifkan kembali
                    ChildLock = False #matikan parameter ChildLock
                    if notification == True:
                        notif.notifChildLock()
                    os.system('cls')
                    Microwave.display1()
                elif pin == 0: #Apabila user memberi masukan 0 maka user memilih untuk selesai menggunakan microwave
                    print("Terima Kasih telah menggunakan produk kami hehehe")
                    break
                else: #Jika masukan pin salah, maka user tidak bisa menggunakan microwave hingga masukan pin benar
                    if notification == True:
                        notif.notifWrong()
                    os.system('cls')
                                
Microwave.Start() #Inisiasi memulai penggunaan microwave