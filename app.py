# import module
import wx
from PWDGenFrame import PWDGenFrame

# buat objek aplikasi
app = wx.App()

# buat frame
frm = PWDGenFrame()

# tampilkan
frm.Show()

# mulai event loop
app.MainLoop()
