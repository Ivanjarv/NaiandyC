
import wx
import wx.lib.agw.aui as aui

def createmenu(data):
    menubar = wx.MenuBar()
    return menubar

class MyFrame(wx.Frame):

    def __init__(self, parent, id=-1, title="Nainady", pos=wx.DefaultPosition,
                 size=(800, 600), style=wx.DEFAULT_FRAME_STYLE):

        wx.Frame.__init__(self, parent, id, title, pos, size, style)

        self._mgr = aui.AuiManager(agwFlags=aui.AUI_MGR_ALLOW_FLOATING | 
        aui.AUI_MGR_TRANSPARENT_HINT | aui.AUI_MGR_VENETIAN_BLINDS_HINT |
         aui.AUI_MGR_NO_VENETIAN_BLINDS_FADE | aui.AUI_MGR_TRANSPARENT_DRAG)

        # notify AUI which frame to use
        self._mgr.SetManagedWindow(self)

        # menubar = wx.MenuBar()
        # file = wx.Menu()
        # fiten = file.Append(-1,"abril", 'Abril la aplicaciones') 
        # menubar.Append(file, '&File')  
        # self.SetMenuBar(menubar) 
        self.createMenuBar()    

        # create several text controls
        text1 = wx.TextCtrl(self, -1, "Pane 1 - sample text",
                            wx.DefaultPosition, wx.Size(200,150),
                            wx.NO_BORDER | wx.TE_MULTILINE)

        text2 = wx.TextCtrl(self, -1, "Pane 2 - sample text",
                            wx.DefaultPosition, wx.Size(200,150),
                            wx.NO_BORDER | wx.TE_MULTILINE)

        text3 = wx.TextCtrl(self, -1, "Main content window",
                            wx.DefaultPosition, wx.Size(200,150),
                            wx.NO_BORDER | wx.TE_MULTILINE)

        # add the panes to the manager
        self._mgr.AddPane(text1, aui.AuiPaneInfo().Left().Caption("Pane Number One").Hide())
        self._mgr.AddPane(text2, aui.AuiPaneInfo().Right().Caption("Pane Number Two").Hide())
        self._mgr.AddPane(text3, aui.AuiPaneInfo().CenterPane())

        # tell the manager to "commit" all the changes just made
        self._mgr.Update()

        self.Bind(wx.EVT_CLOSE, self.OnClose)
        # self.Bind(wx.EVT_MENU, self.abril, fiten)

    def menuData(self):
        return [
            # menu de Registro
            ('&Registro',(
                ('&Registro\tCTRL-R','Entrada de Diario',self.onregistro),
                ('&Cuenta por Cobrar\tF1', 'Factura a Cliente', self.oncuentaporcobrar),
                ('Cuenta por &Pagar\tF3', 'Factura a Proveedores', self.oncuentaporpagar),
                ('Recibo de &Mercancia\tCTRL-M', 'Registro de Mercacia Recibida', self.onrecibodemercancia),
                ('C&atalo de Cuenta\tCTRL-L', 'Catalogo de Cuenta', self.oncatalogodecuenta),
                ['', '', ''],
                ('&Bloquear App\tCTRL-B', u'Bloque la aplicación', self.onbloquearapp),
                ('&Quit\tCTRL-Q', u'Cierre la Aplicación', self.onquit)
            )),
            # menu de Finanza
            ('&Finanza', (
                ['&Banco', (
                ('&Ingreso por...\tF2', 'Recibo de Ingreso', self.onrecibopor),
                ('&Pago de...\tF4', 'Pagos', self.onpagode)
                )],
                ('', '', ''),
                ('&Conciliaciones\tF5', 'Conciliacines Bancaria', self.onconciliaciones),
                (u'Balanza de &Comprobación', u'Balanza de Comprobación', self.onbalanzadecomprobacion),
                ('', '', ''),
                ['Estado Financieros', (
                ('&Balance General', 'Genera el Balance General', self.onbalancegeneral),
                ('&Estado de Resultado', 'Genera el Estado de Resultado', self.onestadoderesultado),
                ('&Flujo de Efectivo', 'Genera el Estado de Flujo de Efectivo', self.onflujodeefectivo)
                )],
                ['&Otros Estado', (
                ('Estado de &Capital', 'Genera el Estado de Capital', self.onestadodecapital)
                )
                ]
                )),
            # menu Habilitar
            ('&Habilitar', (
                ('&Habilitar Barra de &Herramienta\tCTRL-H', 'Habilita o Desabilita la Barra de Herramienta', self.onhabilitabarradeherramienta, wx.ITEM_CHECK)
            )),
            # menu de Impuesto
            ('&Impuesto', (
                ('ITBIS en &Compra 606', 'Genera el Fomulario 606', self.onitbisencompra),
                ('ITBIS en &Venta 607', 'Genera el Fomulario 607', self.onitbisenventa),
                ('Formulario de NCF Nulo 608', 'Genera el Fomulario 608', self.onformulariodencfnulo),
                ('ITBIS en &Aduano 609', 'Genera el Fomulario 609', self.onitbisenaduana),
                ['', '', ''],
                ('&IR-17', 'Genera el Fomulario IR-17', self.onirdiecisiete),
                ('I&R-3', 'Genera el Fomulario IR-3', self.onirtres)
            )),
            # menu de Gestion
            ('&Gestion', (
                ('Crear &Usuario\tF10', 'Crea un Nuevo Usuario', self.oncrearusuario),
                ('&CXC Empleado\tCTRL-C', 'Crear Cuenta por Cobrar a Empleado', self.oncxcempleado),
                ('Decuento a Empleado\tCTRL-D', 'Descuento a Empleado', self.ondescuentoaempleado),
                ('', '', ''),
                ('&Nomina', (
                    (u'&Añadir Empleado\CTRL-F6', 'Registrar en Empleado', self.onagnadirempleado),
                    (u'Añadir &Nomina\tF7', u'Añade Nomina', self.onagnadirnomina),
                    ('&Impuesto Nominales\tF8', 'Configura los Impuestos Nominales', self.onimpuestonominales)
                ))
            )),
            # menu de configuracion
            ('&Configuraciones', (
                ('&Configuraciones Generales\tF12', u'Configuraciones de la Aplicación', self.onconfiguracionesgenerales)
            )),
            # menu Acerca de
            ('&Acerca...', (
                ('&Acera de', 'Muestra el Formulario de Acerca de', self.onacercade),
            ))]
        # return data

    def createMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.menuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.createMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)

    def createMenu(self, menuData):
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.createMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(), label, subMenu)
            else:
                self.createMenuItem(menu, *eachItem)
        return menu

    def createMenuItem(self, menu, label, status, handler, kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)
        self.Bind(wx.EVT_MENU, handler, menuItem)

    def OnClose(self, event):
        # deinitialize the frame manager
        self._mgr.UnInit()
        del self._mgr
        self.Destroy()
        event.Skip()

    def onregistro(self, event):
        print("Event handler 'onregistro' not implemented!")
        event.Skip()

    def oncuentaporcobrar(self, event):
        print("Event handler 'cuentaporcobrar' not implemented!")
        event.Skip()

    def oncuentaporpagar(self, event):
        print("Event handler 'cuentaporpagar' not implemented!")
        event.Skip()

    def onrecibodemercancia(self, event):
        print("Event handler 'recibodemercancia' not implemented!")
        event.Skip()

    def oncatalogodecuenta(self, event):
        print("Event handler 'catalogodecuenta' not implemented!")
        event.Skip()

    def oncuenta(self, event):
        print("Event handler 'cuenta' not implemented!")
        event.Skip()

    def onbloquearapp(self, event):
        print("Event handler 'bloquearapp' not implemented!")
        event.Skip()

    def onquit(self, event):
        print("Event handler 'onquit' not implemented!")
        event.Skip()

    def oningesopor(self, event):
        print("Event handler 'ingesopor' not implemented!")
        event.Skip()

    def onpagode(self, event):
        print("Event handler 'pagode' not implemented!")
        event.Skip()

    def onconciliaciones(self, event):
        print("Event handler 'conciliaciones' not implemented!")
        event.Skip()

    def onbalanzadecomprobacion(self, event):
        print("Event handler 'balanza_de_comprobacion' not implemented!")
        event.Skip()

    def onbalancegeneral(self, event):
        print("Event handler 'balance_general' not implemented!")
        event.Skip()

    def onestadoderesultado(self, event):
        print("Event handler 'estado_de_resultado' not implemented!")
        event.Skip()

    def onflujodeefectivo(self, event):
        print("Event handler 'flujo_de_efectivo' not implemented!")
        event.Skip()

    def onestadodecapital(self, event):
        print("Event handler 'Estado_de_capital' not implemented!")
        event.Skip()

    def onhabilitabarradeherramienta(self, event):
        print("Event handler 'habilitar' not implemented!")
        event.Skip()

    def onitbisencompra(self, event):
        print("Event handler 'itbis_en_compra' not implemented!")
        event.Skip()

    def onitbisenventa(self, event):
        print("Event handler 'itbis_en_venta' not implemented!")
        event.Skip()

    def onformulariodencfnulo(self, event):
        print("Event handler 'Formulario_de_NCF_Nulo' not implemented!")
        event.Skip()

    def onitbisenaduana(self, event):
        print("Event handler 'itbis_en_aduana' not implemented!")
        event.Skip()

    def onirdiecisiete(self, event):
        print("Event handler 'ir_dicisiete' not implemented!")
        event.Skip()

    def onirtres(self, event):
        print("Event handler 'ir_tres' not implemented!")
        event.Skip()

    def oncrearusuario(self, event):
        print("Event handler 'crearusuario' not implemented!")
        event.Skip()

    def oncxcempleado(self, event):
        print("Event handler 'oncxcempleado' not implemented!")
        event.Skip()

    def ondescuentoaempleado(self, event):
        print("Event handler 'ondescuentoaempleado' not implemented!")
        event.Skip()

    def onagnadirempleado(self, event):
        print("Event handler 'agnadirempleado' not implemented!")
        event.Skip()

    def onagnadirnomina(self, event):
        print("Event handler 'agnomina' not implemented!")
        event.Skip()

    def onimpuestonominales(self, event):
        print("Event handler 'impuestonomina' not implemented!")
        event.Skip()

    def onconfiguracionesgenerales(self, event):
        print("Event handler 'configuraciones' not implemented!")
        event.Skip()

    def onacercade(self, event):
        print("Event handler 'acerca' not implemented!")
        event.Skip()

    def onrecibopor(self, event):
        print("Event handler 'resivodeingreso' not implemented!")
        event.Skip()

    def onpagos(self, event):
        print("Event handler 'pagos' not implemented!")
        event.Skip()

    def onmercanciaresibida(self, event):
        print("Event handler 'mercanciaresibida' not implemented!")
        event.Skip()

    def onbloquear(self, event):
        print("Event handler 'bloquear' not implemented!")
        event.Skip()

    def onclose(self, event):
        print("Event handler 'close' not implemented!")
        event.Skip()

    def abril(self, event):
        panel = wx.Panel(self,-1)
        self._mgr.AddPane(panel, aui.AuiPaneInfo().Bottom().Caption("Mi Panel").
        Float().FloatingPosition(self.GetPosition()).FloatingSize(wx.Size(600, 400)).CloseButton(True).MaximizeButton(True).MinimizeButton(True).Layer(0))
        self._mgr.Update()

# our normal wxApp-derived class, as usual
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()