import wx
from BaseDialog import BaseDialog
from PWDGen import PWDGen


class PWDGenDialog (BaseDialog):

    def __init__(self):
        BaseDialog.__init__(self, None)
        self.pwd_gen = PWDGen()

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

    def on_check_lower_case(self, e):
        print("chck " + str(e.IsChecked()))
        self.pwd_gen.is_lower_case = e.IsChecked()

    def on_check_upper_case(self, e):
        print("chck " + str(e.IsChecked()))
        self.pwd_gen.is_upper_case = e.IsChecked()

    def on_check_numbers(self, e):
        print("chck " + str(e.IsChecked()))
        self.pwd_gen.is_numbers = e.IsChecked()

    def on_check_symbols(self, e):
        print("chck " + str(e.IsChecked()))
        self.pwd_gen.is_symbols = e.IsChecked()

    def on_check_unique_characters(self, e):
        print("chck " + str(e.IsChecked()))
        self.pwd_gen.unique_chars = e.IsChecked()

    def on_button_generate(self, e):
        print("generate")
        self.pwd_gen.length = self.m_spin_ctrl_length.GetValue()
        result = self.pwd_gen.generate_password()
        self.m_text_ctrl_results.SetValue(result)

    def on_button_copy_to_clipboard(self, e):
        print("copy")
        pass
