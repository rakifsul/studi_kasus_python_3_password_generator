import wx
from BaseDialog import BaseDialog


class PWDGenDialog (BaseDialog):

    def __init__(self):
        BaseDialog.__init__(self, None)
        self.m_button_generate.Bind(wx.EVT_BUTTON, self.on_button_generate)
        self.m_button_copy_to_clipboard.Bind(
            wx.EVT_BUTTON, self.on_button_copy_to_clipboard)

    def __del__(self):
        pass

    def on_button_generate(self, e):
        print("generate")
        pass

    def on_button_copy_to_clipboard(self, e):
        print("copy")
        pass
