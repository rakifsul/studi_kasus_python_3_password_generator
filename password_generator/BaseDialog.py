# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class BaseDialog
###########################################################################

class BaseDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Password Generator", pos = wx.DefaultPosition, size = wx.Size( 640,363 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		m_b_sizer = wx.BoxSizer( wx.VERTICAL )

		self.m_check_lower_case = wx.CheckBox( self, wx.ID_ANY, u"Lower Case (asdfghjk...)", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_b_sizer.Add( self.m_check_lower_case, 0, wx.ALL, 5 )

		self.m_check_upper_case = wx.CheckBox( self, wx.ID_ANY, u"Upper Case (ASDFGHJK...)", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_b_sizer.Add( self.m_check_upper_case, 0, wx.ALL, 5 )

		self.m_check_numbers = wx.CheckBox( self, wx.ID_ANY, u"Numbers (1234567...)", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_b_sizer.Add( self.m_check_numbers, 0, wx.ALL, 5 )

		self.m_check_symbols = wx.CheckBox( self, wx.ID_ANY, u"Symbols (!@#$%^&...)", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_b_sizer.Add( self.m_check_symbols, 0, wx.ALL, 5 )

		self.m_check_unique_characters = wx.CheckBox( self, wx.ID_ANY, u"Unique Characters (If Possible)", wx.DefaultPosition, wx.DefaultSize, 0 )
		m_b_sizer.Add( self.m_check_unique_characters, 0, wx.ALL, 5 )

		self.m_static_text_length = wx.StaticText( self, wx.ID_ANY, u"Length:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static_text_length.Wrap( -1 )

		m_b_sizer.Add( self.m_static_text_length, 0, wx.ALL, 5 )

		self.m_spin_ctrl_length = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT|wx.SP_ARROW_KEYS, 1, 100000, 5 )
		self.m_spin_ctrl_length.SetMinSize( wx.Size( 9999,-1 ) )

		m_b_sizer.Add( self.m_spin_ctrl_length, 0, wx.ALL, 5 )

		self.m_static_text_results = wx.StaticText( self, wx.ID_ANY, u"Results:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static_text_results.Wrap( -1 )

		m_b_sizer.Add( self.m_static_text_results, 0, wx.ALL, 5 )

		self.m_text_ctrl_results = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_ctrl_results.SetMinSize( wx.Size( 9999,-1 ) )

		m_b_sizer.Add( self.m_text_ctrl_results, 0, wx.ALL, 5 )

		self.m_button_generate = wx.Button( self, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_generate.SetMinSize( wx.Size( 9999,-1 ) )

		m_b_sizer.Add( self.m_button_generate, 0, wx.ALL, 5 )

		self.m_button_copy_to_clipboard = wx.Button( self, wx.ID_ANY, u"Copy to Clipboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_copy_to_clipboard.SetMinSize( wx.Size( 9999,-1 ) )

		m_b_sizer.Add( self.m_button_copy_to_clipboard, 0, wx.ALL, 5 )


		self.SetSizer( m_b_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


