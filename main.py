import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__()
        self.SetId(-1)
        self.SetTitle('wxPython')
        self.SetSize((400, 400))
        self.Show()
    # 上記コードは以下のようにも、書ける
    #  super().__init__(None, -1, 'wxPython', (400, 400))
    #  self.Show()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.SetTopWindow(frame)  # 省略可能
    app.MainLoop()
