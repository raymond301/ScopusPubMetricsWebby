#! /usr/bin/python
# -*- coding: utf-8 -*-

import wx, sys
from conf import *
from webby import *
import pprint
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


pp = pprint.PrettyPrinter(indent=4)
allData = []


###########  Create Table Func #############
class AutoWidthListCtrl(wx.ListCtrl, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        ListCtrlAutoWidthMixin.__init__(self)


############################################
###       Main Window - has Table        ###
############################################
class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        logger.info('Create Main Window')

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

        sk = wx.MenuItem(fileMenu, wx.ID_ANY, '&Scopus API Key')
        fileMenu.AppendItem(sk)
        self.Bind(wx.EVT_MENU, self.on_update_api_key, sk)
        qmi = wx.MenuItem(fileMenu, 1, '&Quit')
        fileMenu.AppendItem(qmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        #### Create Panel ####
        pnl = wx.Panel(self)
        topSizer = wx.BoxSizer(wx.VERTICAL)

        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        cbtn = wx.Button(pnl, label='Add Authors')  # (from Left, from Top) , pos=(640, 10)
        cbtn.Bind(wx.EVT_BUTTON, self.on_button)
        btnSizer.Add(cbtn, 0, wx.ALL, 5)
        topSizer.Add(btnSizer, 0, wx.ALL | wx.ALIGN_RIGHT, 10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.list = AutoWidthListCtrl(pnl)
        self.list.InsertColumn(0, 'Scopus ID', width=100)
        self.list.InsertColumn(1, 'Name', wx.LIST_FORMAT_CENTER, width=130)
        self.list.InsertColumn(2, 'year', wx.LIST_FORMAT_RIGHT, 90)

        #########  Main Table ##########
        for i in allData:
            pp.pprint(i)
            index = self.list.InsertStringItem(sys.maxint, i.scopusId())
            self.list.SetStringItem(index, 1, i.fullName())
            self.list.SetStringItem(index, 2, i.group())

        hbox.Add(self.list, 1, wx.EXPAND)
        topSizer.Add(hbox, 0, wx.ALL | wx.EXPAND, 10)
        pnl.SetSizerAndFit(topSizer)

        # self.button.Bind(wx.EVT_BUTTON, self.on_button)

        #### Set Window Attributes ####
        self.SetSize((750, 600))  ## (w,h)
        self.SetTitle(Static.APP_NAME)
        self.Show(True)

    def OnQuit(self, e):
        f = open("myfile.txt", "wb")
        f.write("\n".join(allData))
        self.Close()

    def on_button(self, evt):
        frame = AddAuthorsFrame(self)
        frame.Show(True)
        frame.MakeModal(True)

    def on_update_api_key(self, evt):
        dlg = wx.TextEntryDialog(None, 'Change/Update this Scpous API KEY:', 'Configure API Key', Static.API_KEY)
        ret = dlg.ShowModal()
        if ret == wx.ID_OK:
            # print('You entered: %s\n' % dlg.GetValue())
            Static.API_KEY = dlg.GetValue()
        dlg.Destroy()


############################################
###     Add Author: just enter Ids       ###
############################################
class AddAuthorsFrame(wx.Frame):
    def __init__(self, parent):
        logger.info('Open Add Author Window')
        wx.Frame.__init__(self, parent, wx.NewId(), "Add Scopus Author")
        self.Centre()
        # Add a panel so it looks correct on all platforms
        p2 = wx.Panel(self, wx.ID_ANY)

        labelOne = wx.StaticText(p2, wx.ID_ANY, 'Select Workunit:')
        self.c = wx.Choice(self, -1, choices=Static.WORKUNITS)
        labelTwo = wx.StaticText(p2, wx.ID_ANY, 'Enter Scopus IDs:')
        self.txt = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE, size=(-1, 80))

        topSizer = wx.BoxSizer(wx.VERTICAL)
        topSizer.Add(labelOne, 0, wx.CENTER, 5)
        topSizer.Add(self.c, 0, wx.ALL | wx.EXPAND, 5)
        # topSizer.Add(wx.StaticLine(p2, ), 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(labelTwo, 0, wx.CENTER, 5)
        topSizer.Add(self.txt, 0, wx.ALL | wx.EXPAND, 5)

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
        #### Add error checks ####
        scopusIds = [s.strip() for s in self.txt.GetValue().splitlines()]
        for i, val in enumerate(scopusIds):
            ### add check for numbers only - error back
            newAU = Author(val, self.c.GetString(self.c.GetSelection()), getAuthorMetrics(val), getAuthorProfile(val))
            allData.append(newAU)
            print(newAU.fullName())
            logger.info('Author: %s', newAU)

        self.GetParent().Refresh()
        # self.parent.Refresh()
        self.MakeModal(False)
        self.Close()




def main():
    ### Check for existing data ###

    ### start UI ###
    ex = wx.App(redirect=False)
    Example(None)
    ex.MainLoop()

if __name__ == '__main__':
    main()
