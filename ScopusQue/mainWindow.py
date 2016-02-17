#! /usr/bin/python
# -*- coding: utf-8 -*-

import wx


##### GLOBAL VARIABLES #####
# APP_EXIT = 1

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        #### Create Menu ####
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        op = wx.MenuItem(fileMenu, wx.ID_OPEN, '&Open Session')
        op.SetBitmap(wx.Bitmap('Import.png'))
        fileMenu.AppendItem(op)
        sv = wx.MenuItem(fileMenu, wx.ID_SAVE, '&Save Session')
        sv.SetBitmap(wx.Bitmap('Export.png'))
        fileMenu.AppendItem(sv)
        fileMenu.AppendSeparator()
        qmi = wx.MenuItem(fileMenu, 1, '&Quit')
        fileMenu.AppendItem(qmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        #### Create Panel ####
        pnl = wx.Panel(self)
        cbtn = wx.Button(pnl, label='Close', pos=(20, 30))
        cbtn.Bind(wx.EVT_BUTTON, self.OnQuit)


        #### Set Window Attributes ####
        self.SetSize((450, 400))
        self.SetTitle('Scopus Que Assistant')
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
