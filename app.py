import wx

from PasswordGeneratorFrame import PasswordGeneratorFrame

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = PasswordGeneratorFrame()

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
