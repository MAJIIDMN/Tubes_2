>[!IMPORTANT]
># Baca Dulu YA..
File Python pada Directory <Source_Code> merupakan program Utama kami, untuk menjalankan Source Code tersebut diperlukan Library tambahan, seperti OpenCV, pyzbar dan simpleaudio.

Karena besarnya ukuran Library (150mb++) kami tidak dapat menyediakan bersamaan dengan file ini ,anda dapat mengistall Library secara manual melalui platfom yang anda gunakan
## PIP
 
	pip install simpleaudio opencv-python pyzbar 
## CONDA
	conda install -c simpleaudio opencv-python pyzbar
		
Jika anda tidak dapat mengistall Library OpenCV dan pyzbar, anda dapat menjalankan Source Code yang hanya menggunakan Library simpleaudio dan library bawaan saat mengistall Python, Source Code tersebut berada pada Folder <Source_Code_Without_Scan>.
 
### File Library Simpleaudio berada pada folder Library
anda juga bisa menginstall Library simpleaudio secara manual
## PIP
	pip install simpleaudio
## CONDA
	conda install -c simpleaudio
> [!TIP]
>## Tambahan
- untuk menghentikan proses microwave saat sedang berjalan(memasak) ada dapat menggunakan keyboard interrupt (CTRL+C)
- anda dapat mencoba fitur Scan Barcode dengan beberapa barcode yang telah disediakan pada folder (barcode)
> [!NOTE]
>### Fitur lainnya telah dijelaskan dalam file program
