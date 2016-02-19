#! /usr/bin/python
# -*- coding: utf-8 -*-

import wx
from conf import Static
from webby import *
import pprint

pp = pprint.PrettyPrinter(indent=4)

allData = []

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

        cbtn = wx.Button(pnl, label='Add Authors', pos=(640, 10))  # (from Left, from Top)
        cbtn.Bind(wx.EVT_BUTTON, self.on_button)
        # self.button.Bind(wx.EVT_BUTTON, self.on_button)


        #### Set Window Attributes ####
        self.SetSize((750, 600))  ## (w,h)
        self.SetTitle(Static.APP_NAME)
        self.Show(True)

    def OnQuit(self, e):
        self.Close()

    def on_button(self, evt):
        frame = AddAuthorsFrame(self)
        frame.Show(True)
        frame.MakeModal(True)


class AddAuthorsFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.NewId(), "Add Scopus Author")
        # self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Centre()
        # Add a panel so it looks correct on all platforms
        p2 = wx.Panel(self, wx.ID_ANY)

        labelOne = wx.StaticText(p2, wx.ID_ANY, 'Select Workunit:')
        c = wx.Choice(self, -1, choices=Static.WORKUNITS)
        labelTwo = wx.StaticText(p2, wx.ID_ANY, 'Enter Scopus IDs:')
        txt = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE, size=(-1, 80))

        topSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer.Add(labelOne, 0, wx.CENTER, 5)
        topSizer.Add(c, 0, wx.ALL | wx.EXPAND, 5)
        # topSizer.Add(wx.StaticLine(p2, ), 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(labelTwo, 0, wx.CENTER, 5)
        topSizer.Add(txt, 0, wx.ALL | wx.EXPAND, 5)

        okBtn = wx.Button(p2, wx.ID_ANY, 'OK')
        cancelBtn = wx.Button(p2, wx.ID_CANCEL, 'Cancel')
        self.Bind(wx.EVT_BUTTON, self.onOK, okBtn)
        self.Bind(wx.EVT_BUTTON, self.on_close, cancelBtn)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add(okBtn, 0, wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)
        topSizer.Add(btnSizer, 0, wx.ALL | wx.CENTER, 5)

        p2.SetSizerAndFit(topSizer)
        topSizer.Fit(self)

    def on_close(self, evt):
        self.MakeModal(False)
        self.Close()
        # evt.Skip()

    def onOK(self, evt):
        self.MakeModal(False)
        evt.Skip()




def main():
    ex = wx.App(redirect=False)
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
