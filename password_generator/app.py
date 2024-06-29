# import module.
import wx
from PWDGenDialog import PWDGenDialog

# buat objek aplikasi.
app = wx.App()

# buat dialog.
dialog = PWDGenDialog()

# tampilkan.
dialog.ShowModal()