>[!TIP]
>## Penting
- jika bermasalah pada path program untuk fitur notifikasi dan musik, pindah Folder (Sound) yang ada di directory Utama kedalam folder yang berisi file program
- jika path yang bermasalah adalah path pada fitur scan barcode, maka ganti path directory pada line 433,
### dari
  	'Source_Code\\barcodes.csv'
### menjadi
	'barcodes.csv'
- untuk mengatur jeda countdown microwave saat berjalan, anda bisa Menganti code pada baris ke 798.
### untuk jeda countdown 10 ms (0.01 detik)
     time.sleep(0.01)
### untuk jeda countdown 1s (1 detik)
     time.sleep(1)
>[!note]
>### Catatan
- sesuaikan path dengan workplace anda saat menjalankan program
