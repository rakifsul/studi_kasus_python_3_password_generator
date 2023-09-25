# shb_py_gui_password_generator - Aplikasi desktop GUI Python untuk membuat password

## Link ke Halaman Web

https://sfrfrlnc.com/shb_py_gui_password_generator/

## Software Apakah Ini?

Ini adalah aplikasi desktop GUI untuk membuat password yang dibuat dengan Python3...

Aplikasi ini bisa menggunakan berbagai jenis karakter:

-   Lower case
-   Upper case
-   Numbers
-   Symbols

Juga bisa menghasilkan password yang karakternya unik jika memungkinkan.

## Cara Kerja

User memasukkan konfigurasi dari password yang akan digenerate.

Setelah prosedur generate password dijalankan, maka hasil password nya akan ditampilkan.

## Cara Mencoba Kode Ini

Harus menggunakan Python 3.10.0.

Untuk menjalankan aplikasi ini, install Python3, masuk ke dalam foldernya via command line, lalu:

Buat virtual environment:

```
python -m venv venv
```

Untuk di windows agar venv bisa diaktifkan:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Aktifkan venv:

```
venv/Scripts/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Untuk menjalankannya dalam mode development:

```
python app.py
```

Untuk membuild exe DENGAN menyertakan console saat aplikasi dijalankan:

```
pyinstaller --onefile app.py
```

Untuk membuild exe TANPA menyertakan console saat aplikasi dijalankan:

```
pyinstaller --onefile --noconsole app.py
```

## Apa Itu GUI.fbp?

File GUI.fbp adalah template dari wxPython GUI yang dibuat dengan wxFormBuilder.

wxFormBuilder bisa di-download di:

https://github.com/wxFormBuilder/wxFormBuilder/releases

## Screenshot

![ScreenShot](https://github.com/shbfrlnc/shbfrlnc-images/blob/main/gratisan/shb_py_gui_password_generator/screenshot-1.png?raw=true)
