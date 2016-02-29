#! /usr/bin/python
# -*- coding: utf-8 -*-

import wx, sys
from conf import Static, Author
from webby import *
from wx.lib.mixins.listctrl import ListCtrlAutoWidthMixin
import logging

logging.basicConfig(level=logging.DEBUG, filename='sq_app.log', )
logger = logging.getLogger(__name__)

DUMMYMETRIC = json.loads(
    '{"author-retrieval-response":[{"@_fa":"true","@status":"found","coauthor-count":"46","coredata":{"citation-count":"13","cited-by-count":"13","dc:identifier":"AUTHOR_ID:56007630200","document-count":"5","prism:url":"http://api.elsevier.com/content/author/author_id/56007630200"},"h-index":"2"}]}')
DUMMYPROFILE = json.loads(
    '{"author-retrieval-response":[{"@_fa":"true","@status":"found","affiliation-current":{"@href":"http://api.elsevier.com/content/affiliation/affiliation_id/103323174","@id":"103323174"},"author-profile":{"affiliation-current":{"affiliation":{"@affiliation-id":"103323174","@parent":"60005558","ip-doc":{"@id":"103323174","@relationship":"author","@type":"dept","address":{"@country":"usa","city":"Rochester","country":"UnitedStates","postal-code":"55905","state":"MN"},"afdispname":"MayoClinic,DepartmentofHealthSciencesResearch","org-URL":"http://www.mayoclinic.org/","org-domain":"mayoclinic.org","parent-preferred-name":"MayoClinic","preferred-name":"DepartmentofHealthSciencesResearch","sort-name":"DepartmentofHealthSciencesResearch"}}},"affiliation-history":{"affiliation":[{"@affiliation-id":"103323174","@parent":"60005558","ip-doc":{"@id":"103323174","@relationship":"author","@type":"dept","address":{"@country":"usa","city":"Rochester","country":"UnitedStates","postal-code":"55905","state":"MN"},"afdispname":"MayoClinic,DepartmentofHealthSciencesResearch","org-URL":"http://www.mayoclinic.org/","org-domain":"mayoclinic.org","parent-preferred-name":"MayoClinic","preferred-name":"DepartmentofHealthSciencesResearch","sort-name":"DepartmentofHealthSciencesResearch"}},{"@affiliation-id":"103323932","@parent":"60005558","ip-doc":{"@id":"103323932","@relationship":"author","@type":"dept","address":{"@country":"usa","city":"Rochester","country":"UnitedStates","postal-code":"55905","state":"MN"},"afdispname":"MayoClinic,DivisionofBiomedicalStatisticsandInformatics","org-URL":"http://www.mayoclinic.org/","org-domain":"mayoclinic.org","parent-preferred-name":"MayoClinic","preferred-name":"DivisionofBiomedicalStatisticsandInformatics","sort-name":"DivisionofBiomedicalStatisticsandInformatics"}},{"@affiliation-id":"103246320","@parent":"60003892","ip-doc":{"@id":"103246320","@relationship":"author","@type":"dept","address":{"@country":"usa","address-part":"UniversityDriveandMillAvenue","city":"Tempe","country":"UnitedStates","state":"AZ"},"afdispname":"ArizonaStateUniversity,DepartmentofBiomedicalInformatics","org-URL":"http://www.asu.edu/","org-domain":"asu.edu","parent-preferred-name":"ArizonaStateUniversity","preferred-name":"DepartmentofBiomedicalInformatics","sort-name":"DepartmentofBiomedicalInformatics"}}]},"classificationgroup":{"classifications":{"@type":"ASJC","classification":[{"$":"1303","@frequency":"3"},{"$":"1703","@frequency":"1"},{"$":"2204","@frequency":"1"},{"$":"2713","@frequency":"1"},{"$":"2730","@frequency":"1"},{"$":"2605","@frequency":"1"},{"$":"2700","@frequency":"4"},{"$":"2613","@frequency":"1"},{"$":"1100","@frequency":"3"},{"$":"2800","@frequency":"1"},{"$":"1315","@frequency":"2"},{"$":"2216","@frequency":"1"},{"$":"2718","@frequency":"1"},{"$":"1312","@frequency":"3"},{"$":"1300","@frequency":"3"},{"$":"1706","@frequency":"3"},{"$":"2604","@frequency":"2"}]}},"date-created":{"@day":"07","@month":"02","@year":"2014"},"journal-history":{"@type":"author","journal":[{"@type":"j","issn":"10559965","sourcetitle":"CancerEpidemiologyBiomarkersandPrevention","sourcetitle-abbrev":"CancerEpidemiol.BiomarkersPrev."},{"@type":"j","issn":"14602059","sourcetitle":"Bioinformatics","sourcetitle-abbrev":"Bioinformatics"},{"@type":"j","issn":"19326203","sourcetitle":"PLoSONE","sourcetitle-abbrev":"PLoSONE"},{"@type":"j","issn":"14712105","sourcetitle":"BMCbioinformatics","sourcetitle-abbrev":"BMCBioinformatics"},{"@type":"j","issn":"21678359","sourcetitle":"PeerJ","sourcetitle-abbrev":"PeerJ"},{"@type":"j","issn":"14712105","sourcetitle":"BMCBioinformatics","sourcetitle-abbrev":"BMCBioinform."},{"@type":"p","sourcetitle":"BIOINFORMATICS2015-6thInternationalConferenceonBioinformaticsModels,MethodsandAlgorithms,Proceedings;Partof8thInternationalJointConferenceonBiomedicalEngineeringSystemsandTechnologies,BIOSTEC2015","sourcetitle-abbrev":"BIOINFORMATICS-Int.Conf.Bioinform.Model.,MethodsAlgorithms,Proc.;PartInt.Jt.Conf.Biomed.Eng.Syst.Technol.,BIOSTEC"},{"@type":"j","issn":"13674811","sourcetitle":"Bioinformatics(Oxford,England)","sourcetitle-abbrev":"Bioinformatics"}]},"name-variant":{"given-name":"Raymond","indexed-name":"MooreR.","initials":"R.","surname":"Moore"},"preferred-name":{"given-name":"RaymondM.","indexed-name":"MooreR.","initials":"R.M.","surname":"Moore"},"publication-range":{"@end":"2016","@start":"2013"},"status":"update"},"coredata":{"citation-count":"13","cited-by-count":"13","dc:identifier":"AUTHOR_ID:56007630200","document-count":"5","eid":"9-s2.0-56007630200","link":[{"@_fa":"true","@href":"http://api.elsevier.com/content/search/scopus?query=refauid%2856007630200%29","@rel":"scopus-citedby"},{"@_fa":"true","@href":"http://www.scopus.com/authid/detail.url?partnerID=HzOxMe3b&authorId=56007630200&origin=inward","@rel":"scopus-author"},{"@_fa":"true","@href":"http://api.elsevier.com/content/author/author_id/56007630200","@rel":"self"},{"@_fa":"true","@href":"http://api.elsevier.com/content/search/scopus?query=au-id%2856007630200%29","@rel":"search"}],"prism:url":"http://api.elsevier.com/content/author/author_id/56007630200"},"subject-areas":{"subject-area":[{"$":"Biochemistry","@_fa":"true","@abbrev":"BIOC","@code":"1303"},{"$":"ComputationalTheoryandMathematics","@_fa":"true","@abbrev":"COMP","@code":"1703"},{"$":"BiomedicalEngineering","@_fa":"true","@abbrev":"ENGI","@code":"2204"},{"$":"Epidemiology","@_fa":"true","@abbrev":"MEDI","@code":"2713"},{"$":"Oncology","@_fa":"true","@abbrev":"MEDI","@code":"2730"},{"$":"ComputationalMathematics","@_fa":"true","@abbrev":"MATH","@code":"2605"},{"$":"Medicine(all)","@_fa":"true","@abbrev":"MEDI","@code":"2700"},{"$":"StatisticsandProbability","@_fa":"true","@abbrev":"MATH","@code":"2613"},{"$":"AgriculturalandBiologicalSciences(all)","@_fa":"true","@abbrev":"AGRI","@code":"1100"},{"$":"Neuroscience(all)","@_fa":"true","@abbrev":"NEUR","@code":"2800"},{"$":"StructuralBiology","@_fa":"true","@abbrev":"BIOC","@code":"1315"},{"$":"Architecture","@_fa":"true","@abbrev":"ENGI","@code":"2216"},{"$":"HealthInformatics","@_fa":"true","@abbrev":"MEDI","@code":"2718"},{"$":"MolecularBiology","@_fa":"true","@abbrev":"BIOC","@code":"1312"},{"$":"Biochemistry,GeneticsandMolecularBiology(all)","@_fa":"true","@abbrev":"BIOC","@code":"1300"},{"$":"ComputerScienceApplications","@_fa":"true","@abbrev":"COMP","@code":"1706"},{"$":"AppliedMathematics","@_fa":"true","@abbrev":"MATH","@code":"2604"}]}}]}')

tmp = Author('44444444444', 'No-Where', DUMMYMETRIC, DUMMYPROFILE)
allData = [tmp]


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
        #### Set Window Attributes ####
        self.SetSize((950, 600))  ## (w,h)
        self.SetTitle(Static.APP_NAME)
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
        self.pnlTableList = wx.Panel(self)
        topSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        cbtn = wx.Button(self.pnlTableList, label='Add Authors')  # (from Left, from Top) , pos=(640, 10)
        cbtn.Bind(wx.EVT_BUTTON, self.on_button)
        btnSizer.Add(cbtn, 0, wx.ALL, 5)
        topSizer.Add(btnSizer, 0, wx.ALL | wx.ALIGN_RIGHT, 10)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.list = AutoWidthListCtrl(self.pnlTableList)
        self.list.InsertColumn(0, 'Scopus ID', width=100)
        self.list.InsertColumn(1, 'Name', wx.LIST_FORMAT_CENTER, width=130)
        self.list.InsertColumn(2, 'H-Index', wx.LIST_FORMAT_CENTER, 90)
        self.list.InsertColumn(3, 'Total Articles', wx.LIST_FORMAT_CENTER, 90)
        self.list.InsertColumn(4, '# Co-authors', wx.LIST_FORMAT_CENTER, 90)
        self.list.InsertColumn(5, '# Citations', wx.LIST_FORMAT_CENTER, 90)
        self.list.InsertColumn(6, '# Cited By', wx.LIST_FORMAT_CENTER, 90)
        self.list.InsertColumn(7, '# Affiliations', wx.LIST_FORMAT_CENTER, 90)
        self.list.InsertColumn(8, 'Work Unit', wx.LIST_FORMAT_RIGHT, 90)

        ## Use this function to dymanically keep adding to Table from Global Array
        self.updateTable()
        hbox.Add(self.list, 1, wx.EXPAND | wx.GROW)
        topSizer.Add(hbox, 0, wx.ALL | wx.EXPAND | wx.GROW, 10)

        btnSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        okBtn = wx.Button(self.pnlTableList, wx.ID_ANY, 'OK')
        cancelBtn = wx.Button(self.pnlTableList, wx.ID_CANCEL, 'Cancel')
        self.Bind(wx.EVT_BUTTON, self.OnQuit, okBtn)
        self.Bind(wx.EVT_BUTTON, self.OnQuit, cancelBtn)
        btnSizer2.Add(okBtn, 0, wx.ALL, 20)
        btnSizer2.Add(cancelBtn, 0, wx.ALL, 20)
        topSizer.Add(btnSizer2, 0, wx.ALL | wx.CENTER, 5)

        self.pnlTableList.SetSizerAndFit(topSizer)
        self.Show(True)

    def updateTable(self):
        #########  Main Table ##########
        ## Scopus ID | Name | Work Unit
        self.list.DeleteAllItems()
        for i in allData:
            index = self.list.InsertStringItem(sys.maxint, i.scopusId())
            self.list.SetStringItem(index, 1, i.fullName())
            self.list.SetStringItem(index, 2, i.hIdx())
            self.list.SetStringItem(index, 3, i.totalPubNx())
            self.list.SetStringItem(index, 4, i.coauthorNx())
            self.list.SetStringItem(index, 5, i.citationNx())
            self.list.SetStringItem(index, 6, i.citedByNx())
            self.list.SetStringItem(index, 7, i.affiliationNx())
            self.list.SetStringItem(index, 8, i.group())

    def OnQuit(self, e):
        logger.info(','.join(allData))
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

    def onOK(self, evt):
        #### Add error checks ####
        scopusIds = [s.strip() for s in self.txt.GetValue().splitlines()]
        for i, val in enumerate(scopusIds):
            ### add check for numbers only - error back
            # newAU = Author(val, self.c.GetString(self.c.GetSelection()), getAuthorMetrics(val), getAuthorProfile(val))
            newAU = Author('76676544333', 'Here 2', DUMMYMETRIC, DUMMYPROFILE)
            allData.append(newAU)
            #logger.info('Author: %s', newAU)

        #        logger.debug(self.GetParent().GetTitle())
        self.GetParent().updateTable()
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
