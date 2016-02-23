__author__ = 'm088378'

import wx
import matplotlib

matplotlib.use('WXAgg')
import wx.xrc as xrc


class GroupPieChartView(wx.Panel):
    def __init__(self, parent):
        self.res = xrc.XmlResource(xrcfile)

        # main frame and panel ---------

        self.frame = self.res.LoadFrame(None, "MainFrame")
        self.panel = xrc.XRCCTRL(self.frame, "MainPanel")

        # matplotlib panel -------------

        # container for matplotlib panel (I like to make a container
        # panel for our panel so I know where it'll go when in XRCed.)
        plot_container = xrc.XRCCTRL(self.frame, "plot_container_panel")
        sizer = wx.BoxSizer(wx.VERTICAL)

        # matplotlib panel itself
        self.plotpanel = PlotPanel(plot_container)
        self.plotpanel.init_plot_data()

        # wx boilerplate
        sizer.Add(self.plotpanel, 1, wx.EXPAND)
        plot_container.SetSizer(sizer)

        self.panel = xrc.XRCCTRL(self.frame, "MainPanel")
        plot_container = xrc.XRCCTRL(self.frame, "plot_container_panel")
        # wx.Panel.__init__(self, parent, -1)

    def onEraseBackground(self, evt):
        # this is supposed to prevent redraw flicker on some X servers...
        pass


if __name__ == '__main__':
    ### start UI ###
    ex = wx.App(redirect=False)
    GroupPieChartView(None)
    ex.MainLoop()
