# shb_py_gui_password_generator - Aplikasi desktop GUI Python untuk membuat password

Ini adalah aplikasi desktop GUI untuk membuat password yang dibuat dengan Python3.

Aplikasi ini bisa menggunakan berbagai jenis karakter:

- Lower case
- Upper case
- Numbers
- Symbols

Juga bisa menghasilkan password yang karakternya unik jika memungkinkan.

## Screenshot

![ScreenShot](.readme-assets/shb_py_gui_password_generator-1.png?raw=true)

## Cara Mencoba Kode Ini

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

Untuk membuild exe:

```
pyinstaller --onefile app.py
```
