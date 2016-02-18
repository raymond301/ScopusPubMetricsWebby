#! /usr/bin/python
# -*- coding: utf-8 -*-

import wx
from conf import Static


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
        cbtn.Bind(wx.EVT_BUTTON, self.ShowEnterAuthorUI)


        #### Set Window Attributes ####
        self.SetSize((750, 600))  ## (w,h)
        self.SetTitle(Static.APP_NAME)
        self.Show(True)

    def OnQuit(self, e):
        self.Close()

    def onOK(self, e):
        self.Close()

    def onCancel(self, e):
        self.Close()

    def ShowEnterAuthorUI(self, e):
        f2 = wx.Frame(None, -1)
        f2.Centre()
        # Add a panel so it looks correct on all platforms
        p2 = wx.Panel(f2, wx.ID_ANY)

        labelOne = wx.StaticText(p2, wx.ID_ANY, 'Select Workunit:')
        c = wx.Choice(f2, -1, choices=Static.WORKUNITS)
        labelTwo = wx.StaticText(p2, wx.ID_ANY, 'Enter Scopus IDs:')
        txt = wx.TextCtrl(f2, -1, style=wx.TE_MULTILINE, size=(-1, 80))
        # txt.SetValue('<scopus id>')

        okBtn = wx.Button(p2, wx.ID_ANY, 'OK')
        cancelBtn = wx.Button(p2, wx.ID_ANY, 'Cancel')
        self.Bind(wx.EVT_BUTTON, self.onOK, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)

        topSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer.Add(labelOne, 0, wx.CENTER, 5)
        topSizer.Add(c, 0, wx.ALL | wx.EXPAND, 5)
        # topSizer.Add(wx.StaticLine(p2, ), 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(labelTwo, 0, wx.CENTER, 5)
        topSizer.Add(txt, 0, wx.ALL | wx.EXPAND, 5)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add(okBtn, 0, wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)
        topSizer.Add(btnSizer, 0, wx.ALL | wx.CENTER, 5)

        p2.SetSizerAndFit(topSizer)
        topSizer.Fit(f2)
        f2.Show()


def main():
    ex = wx.App(redirect=False)
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()
