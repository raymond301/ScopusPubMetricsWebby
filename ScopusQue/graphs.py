__author__ = 'm088378'

import wx
import matplotlib

# matplotlib.use('WXAgg')
# import wx.xrc as xrc
#
#
# class GroupPieChartView(wx.Panel):
#     def __init__(self, parent):
#
#         #self.res = xrc.XmlResource(xrcfile)
#
#         # main frame and panel ---------
#
#         self.frame = self.res.LoadFrame(None, "MainFrame")
#         self.panel = xrc.XRCCTRL(self.frame, "MainPanel")
#
#         # matplotlib panel -------------
#
#         # container for matplotlib panel (I like to make a container
#         # panel for our panel so I know where it'll go when in XRCed.)
#         plot_container = xrc.XRCCTRL(self.frame, "plot_container_panel")
#         sizer = wx.BoxSizer(wx.VERTICAL)
#
#         # matplotlib panel itself
#         self.plotpanel = PlotPanel(plot_container)
#         self.plotpanel.init_plot_data()
#
#         # wx boilerplate
#         sizer.Add(self.plotpanel, 1, wx.EXPAND)
#         plot_container.SetSizer(sizer)
#
#         self.panel = xrc.XRCCTRL(self.frame, "MainPanel")
#         plot_container = xrc.XRCCTRL(self.frame, "plot_container_panel")
#         # wx.Panel.__init__(self, parent, -1)
#
#     def onEraseBackground(self, evt):
#         # this is supposed to prevent redraw flicker on some X servers...
#         pass
#
#


import numpy as np
import wx
from wx.lib.plot import PlotCanvas, PlotGraphics, PolyLine, PolyMarker


def drawSinCosWaves():
    # 100 points sin function, plotted as green circles
    data1 = 2. * np.pi * np.arange(200) / 200.
    data1.shape = (100, 2)
    data1[:, 1] = np.sin(data1[:, 0])
    markers1 = PolyMarker(data1, legend='Green Markers', colour='green', marker='circle', size=1)

    # 50 points cos function, plotted as red line
    data1 = 2. * np.pi * np.arange(100) / 100.
    data1.shape = (50, 2)
    data1[:, 1] = np.cos(data1[:, 0])
    lines = PolyLine(data1, legend='Red Line', colour='red')

    # A few more points...
    pi = np.pi
    markers2 = PolyMarker([(0., 0.), (pi / 4., 1.), (pi / 2, 0.),
                           (3. * pi / 4., -1)], legend='Cross Legend', colour='blue',
                          marker='cross')

    return PlotGraphics([markers1, lines, markers2], "Graph Title", "X Axis", "Y Axis")


########################################################################
class MyGraph(wx.Frame):
    # ----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Sin / Cos Plot')

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        checkSizer = wx.BoxSizer(wx.HORIZONTAL)

        # create the widgets
        self.canvas = PlotCanvas(panel)
        self.canvas.Draw(drawSinCosWaves())
        toggleGrid = wx.CheckBox(panel, label="Show Grid")
        toggleGrid.Bind(wx.EVT_CHECKBOX, self.onToggleGrid)
        toggleLegend = wx.CheckBox(panel, label="Show Legend")
        toggleLegend.Bind(wx.EVT_CHECKBOX, self.onToggleLegend)

        # layout the widgets
        mainSizer.Add(self.canvas, 1, wx.EXPAND)
        checkSizer.Add(toggleGrid, 0, wx.ALL, 5)
        checkSizer.Add(toggleLegend, 0, wx.ALL, 5)
        mainSizer.Add(checkSizer)
        panel.SetSizer(mainSizer)

    # ----------------------------------------------------------------------
    def onToggleGrid(self, event):
        """"""
        self.canvas.SetEnableGrid(event.IsChecked())

    # ----------------------------------------------------------------------
    def onToggleLegend(self, event):
        """"""
        self.canvas.SetEnableLegend(event.IsChecked())

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyGraph()
    frame.Show()
    app.MainLoop()



# if __name__ == '__main__':
#     ### start UI ###
#     ex = wx.App(redirect=False)
#     GroupPieChartView(None)
#     ex.MainLoop()
