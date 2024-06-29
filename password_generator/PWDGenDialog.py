import wx
import webbrowser
from BaseDialog import BaseDialog
from PWDGen import PWDGen

# dialog utama, diturunkan dari BaseDialog.
class PWDGenDialog (BaseDialog):

    def __init__(self):
        BaseDialog.__init__(self, None)
        self.pwd_gen = PWDGen()

        # event binding.
        self.m_check_lower_case.Bind(wx.EVT_CHECKBOX, self.on_check_lower_case)
        self.m_check_upper_case.Bind(wx.EVT_CHECKBOX, self.on_check_upper_case)
        self.m_check_numbers.Bind(wx.EVT_CHECKBOX, self.on_check_numbers)
        self.m_check_symbols.Bind(wx.EVT_CHECKBOX, self.on_check_symbols)
        self.m_check_unique_characters.Bind(
            wx.EVT_CHECKBOX, self.on_check_unique_characters)

        self.m_button_generate.Bind(wx.EVT_BUTTON, self.on_button_generate)
        self.m_button_copy_to_clipboard.Bind(
            wx.EVT_BUTTON, self.on_button_copy_to_clipboard)

    def __del__(self):
        pass

    # saat lowercase dicentang/tidak dicentang.
    def on_check_lower_case(self, e):
        print("check " + str(e.IsChecked()))
        self.pwd_gen.is_lower_case = e.IsChecked()

    # saat uppercase dicentang/tidak dicentang.
    def on_check_upper_case(self, e):
        print("check " + str(e.IsChecked()))
        self.pwd_gen.is_upper_case = e.IsChecked()

    # saat numbers dicentang/tidak dicentang.
    def on_check_numbers(self, e):
        print("check " + str(e.IsChecked()))
        self.pwd_gen.is_numbers = e.IsChecked()

    # saat symbols dicentang/tidak dicentang.
    def on_check_symbols(self, e):
        print("check " + str(e.IsChecked()))
        self.pwd_gen.is_symbols = e.IsChecked()

    # saat unique characters dicentang/tidak dicentang.
    def on_check_unique_characters(self, e):
        print("check " + str(e.IsChecked()))
        self.pwd_gen.unique_chars = e.IsChecked()

    # saat tombol generate diklik.
    def on_button_generate(self, e):
        print("generate")
        self.pwd_gen.length = self.m_spin_ctrl_length.GetValue()
        result = self.pwd_gen.generate_password()
        self.m_text_ctrl_results.SetValue(result)

    # saat tombol copy to clipboard diklik.
    def on_button_copy_to_clipboard(self, e):
        print("copy")
        self.set_clipboard_text(self.m_text_ctrl_results.GetValue())
        pass

    # implementasi pengisian clipboard.
    def set_clipboard_text(self, value):
        text_data_object = wx.TextDataObject()
        text_data_object.SetText(value)
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(text_data_object)
            wx.TheClipboard.Close()
