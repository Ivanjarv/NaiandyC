#*

import wx
import diseno_naiandy as dn

class Geometry():
    def __init__(self, parent):
        self.parent = parent
        self.posicion = self.parent.ClientToScreen()
        self.cw, self.ch = self.parent.parent.GetClientSize()
        self.wc, self.hc =self.parent.parent.GetPosition()

    def prueba(self):
        dc = wx.PainDC(self)
        dc.DrawLine(50, 60, 190, 60)

class BaseWidget(dn.BaseNainady):
    def __init__(self, *arg, **kwargs):
        self.parent = arg[0]
        self.senal = True
        super().__init__(*arg, **kwargs)
        self.delta = wx.Point(0, 0)
        self.sise = (85, 42)
        self.panelsup.Bind(wx.EVT_LEFT_DOWN, self.onleftdown)
        self.panelsup.Bind(wx.EVT_LEFT_UP, self.onleftup)
        self.panelsup.Bind(wx.EVT_MOTION, self.onmousemove)

    def onleftdown(self, event):
        self.panelsup.CaptureMouse()
        pos = self.ClientToScreen(event.GetPosition())
        origin = self.GetPosition()
        self.delta = wx.Point(pos.x - origin.x, pos.y - origin.y)
        event.Skip()

    def onleftup(self, event):
        if self.panelsup.HasCapture():
            self.ReleaseMouse()
        event.Skip()

    def onmousemove(self, event):
        if event.Dragging() and event.LeftIsDown():
            pos = self.ClientToScreen(event.GetPosition())
            newPos = (pos.x - self.delta.x, pos.y - self.delta.y)
            self.Move(newPos)
        event.Skip()

    def btnonenter(self, event):
        print("Event handler 'btnonenter' not implemented!")
        event.Skip()

    def btnleavve(self, event):
        print("Event handler 'btnleavve' not implemented!")
        event.Skip()

    def minimizar(self, event):
        wc, hc =self.parent.GetPosition()        
        self.SetSize(self.sise[0],self.sise[1])
        event.Skip()

    def btnonenterright(self, event):
        print("Event handler 'btnonenterright' not implemented!")
        event.Skip()

    def btnleavveright(self, event):
        print("Event handler 'btnleavveright' not implemented!")
        event.Skip()

    def maximizar(self, event):
        cw, ch = self.parent.GetClientSize()
        wc, hc =self.parent.GetPosition()
        if self.senal:
            self.SetDimensions(wc+2, hc+95,cw+12,ch+5)
            self.senal = False
        else:
            self.SetSize((200,200))
            self.senal = True
            self.Center() 
        event.Skip()

    def close(self, event):
        self.Close()
        event.Skip()

class MainWindows(dn.MainWindows):
    def __init__(self, *arg, **kwargs):
        dn.MainWindows.__init__(self, *arg, **kwargs)
        g = Geometry(self)
        g.prueba()

    def onregistro(self, event):
        base = BaseWidget(self, -1, "")
        base.Show()
        event.Skip()
#_____________________________________________________________________________
# las clases aqui declarada son de prueba borrar al terminar de traajar el modulo

class MyApp(wx.App):
    def OnInit(self):
        self.mainwindows = MainWindows(None, wx.ID_ANY, "")
        self.SetTopWindow(self.mainwindows)
        self.mainwindows.Show()
        return True

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
