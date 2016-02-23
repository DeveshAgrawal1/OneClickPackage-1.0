import wx,os

wildcard =  "All files (*.py)|*.py"


keylist=[]
reqlist=[]

class Example(wx.Frame):
  
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
            size=(500, 700))
            
        self.InitUI()
        self.Centre()
        self.Show()   
        self.attpath=''  
        
    def InitUI(self):
    
        panel = wx.Panel(self)

        self.currentDirectory = os.getcwd()
        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Name of the Package')
        st1.SetFont(font)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.tc = wx.TextCtrl(panel)
        hbox1.Add(self.tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)
        vbox.Add((-1, 10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(panel, label='Version No.')
        st3.SetFont(font)
        hbox3.Add(st3, flag=wx.RIGHT, border=70)
        self.tc3 = wx.TextCtrl(panel)
        hbox3.Add(self.tc3, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)
        vbox.Add((-1, 10))

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        st4 = wx.StaticText(panel, label='GitHub URL')
        st4.SetFont(font)
        hbox4.Add(st4, flag=wx.RIGHT, border=68)
        self.tc4 = wx.TextCtrl(panel)
        hbox4.Add(self.tc4, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)
        vbox.Add((-1, 10))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        st5 = wx.StaticText(panel, label='Author Name')
        st5.SetFont(font)
        hbox5.Add(st5, flag=wx.RIGHT, border=61)
        self.tc5 = wx.TextCtrl(panel,style=wx.TE_CAPITALIZE)
        hbox5.Add(self.tc5, proportion=1)
        vbox.Add(hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)
        vbox.Add((-1, 10))

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        st6 = wx.StaticText(panel, label='Author Email')
        st6.SetFont(font)
        hbox6.Add(st6, flag=wx.RIGHT, border=61)
        self.tc6 = wx.TextCtrl(panel)
        hbox6.Add(self.tc6, proportion=1)
        vbox.Add(hbox6, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)
        vbox.Add((-1, 10))

        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        st7 = wx.StaticText(panel, label='Description')
        st7.SetFont(font)
        hbox7.Add(st7, flag=wx.RIGHT, border=8)
        vbox.Add(hbox7, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)
        vbox.Add((-1, 10))

        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc8 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox8.Add(self.tc8, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox8, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=5)
        vbox.Add((-1, 25))

        

        hbox11 = wx.BoxSizer(wx.HORIZONTAL)
        st11 = wx.StaticText(panel, label='Keywords you want to specify')
        st11.SetFont(font)
        hbox11.Add(st11, flag=wx.RIGHT, border=8)
        self.tc11 = wx.TextCtrl(panel)
        hbox11.Add(self.tc11, proportion=1)
        vbox.Add(hbox11, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)
        vbox.Add((-1, 10))

        hbox12 = wx.BoxSizer(wx.HORIZONTAL)
        st12 = wx.StaticText(panel, label='Other Python Packages needed to be installed')
        st12.SetFont(font)
        hbox12.Add(st12, flag=wx.RIGHT, border=8)
        vbox.Add(hbox12, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=5)
        vbox.Add((-1, 10))

        hbox13 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc13 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        hbox13.Add(self.tc13, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox13, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=5)
        vbox.Add((-1, 25))

        hbox14 = wx.BoxSizer(wx.HORIZONTAL)
        self.btn1 = wx.Button(panel, label='Path', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.onAttach, self.btn1)
        hbox14.Add(self.btn1)
        self.st14 = wx.StaticText(panel,wx.ID_ANY ,label='Path to the Python Script')
        self.st14.SetFont(font)
        hbox14.Add(self.st14, flag=wx.RIGHT, border=50)
        vbox.Add(hbox14, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=5)

        hbox15=wx.BoxSizer(wx.HORIZONTAL)
        btn=wx.Button(panel,label='Pack It!',size=(70,30))
        btn.Bind(wx.EVT_BUTTON, self.onPack)
        hbox15.Add(btn, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox15, flag=wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT, border=5)
        panel.SetSizer(vbox)

    def onAttach(self,event):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory, 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            str(self.st14.SetLabel(str(path).encode('utf-8').encode('ascii')))
            self.attpath=str(path).encode('utf-8').encode('ascii')
            print self.attpath
        dlg.Destroy()

    def onPack(self,event):
        if str(self.tc.GetValue()).strip()==''or str(self.tc3.GetValue()).strip()=='' or str(self.tc4.GetValue()).strip()==''or str(self.st14.GetLabelText).strip()=='' or str(self.tc5.GetValue()).strip()=='' or str(self.tc6.GetValue()).strip()=='' or str(self.tc8.GetValue()).strip()=='':
            dial = wx.MessageDialog(None, 'Please enter valid details', 'Error', wx.OK | wx.ICON_EXCLAMATION)
            dial.ShowModal()
            return
        name= str(self.tc.GetValue())
        version=str(self.tc3.GetValue())
        github=str(self.tc4.GetValue())
        author=str(self.tc5.GetValue())
        authemail=str(self.tc6.GetValue())
        desc=str(self.tc8.GetValue())
        keyword=str(self.tc11.GetValue())
        requires=str(self.tc13.GetValue())

        reqlist=requires.splitlines()
        keylist=keyword.split(',')
        i1=makedirectories(name) 
        if i1=='not done':
            dial1 = wx.MessageDialog(None, 'Error making directories', 'Error',wx.OK | wx.ICON_ERROR)
            dial1.ShowModal()
            return
        i2=createfiles(name,version,github,author,authemail,desc,keylist,reqlist,self.attpath)
        if i2=='not done':
            dial1 = wx.MessageDialog(None, 'Error making files', 'Error',wx.OK | wx.ICON_ERROR)
            dial1.ShowModal()
            return
        os.system('python setup.py sdist register upload')
        dial2 = wx.MessageDialog(None, 'Package created successfully!', 'Success!', wx.OK)
        dial2.ShowModal()
        self.tc.Clear()
        self.tc3.Clear()
        self.tc4.Clear()
        self.tc5.Clear()
        self.tc6.Clear()
        self.tc8.Clear()
        self.tc11.Clear()
        self.tc13.Clear()
        

def makedirectories(name):
    try:
        os.system('mkdir ' + name)
        os.system('mkdir ' + name + '\\' + name)
        os.system('type NUL > ' + name + '\\' + name + '\\' + '__init__.py')
        return 'done'
    except Exception,e:
        info='not done'
        return info

def createfiles(name,version,github,author,authemail,desc,keylist,reqlist,ath):
    try:
        lth=len(keylist)
        pop=[]
        for i in range(0,lth):
            if(str(keylist[i]).strip!=''):
                pop.append(str(keylist[i]))
        if len(keylist)<5:
            for j in range(0,5-lth):
                pop.append(' ')

        rth=len(reqlist)
        top=[]
        for i in range(0,rth):
            if(str(reqlist[i]).strip!=''):
                top.append(str(reqlist[i]))
        if len(reqlist)<5:
            for j in range(0,5-rth):
                top.append(' ')
                
        print pop,top,keylist,reqlist
        with open(name+'\\setup.py',"w+")as file:
            file.write('''
from setuptools import setup

setup(
    name="''' + name + '''",
    version="''' + version + '''",
    description="'''+desc+'''",
    url="''' + github + '''",
    author="''' + author + '''",
    author_email="''' + authemail + '''",
    license='MIT',
    packages=["''' + name + '''"],
    keywords=["'''+pop[0]+'''","'''+pop[1]+'''","'''+pop[2]+'''","'''+pop[3]+'''","'''+pop[4]+'''"],
    install_requires=["'''+top[0] +'''","'''+top[1] +'''","'''+top[2] +'''","'''+top[3] +'''","'''+top[4] +'''"],
    scripts=["src/''' + name + '''"],
    zip_safe=True
    )
    ''')
        os.system('mkdir ' + name + '\src')
        with open(name+'\src\\'+name,'w')as file2,open(ath,'r')as file1:
            for line in file1:
                file2.write(line)
        os.chdir(name)
        info='done'
        return info
    except Exception,e:
        info='not done'
        return info

if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='One Click Package')
    app.MainLoop()