import xbmc
import xbmcgui
import xbmcaddon
class PopUpDialog(xbmcgui.WindowXMLDialog):
  def __init__(self, *args, **kvargs):#xmlFilename="plugin-extrabuttons-comments.xml", scriptPath=xbmcaddon.Addon("plugin.program.vpftools").getAddonInfo('path'), defaultSkin="default", defaultRes="1080i", comments=None, loadMoreFunction = None, replyFunction = None):
    self.buttons = kvargs['buttons']
    xbmcgui.WindowXMLDialog.__init__(self, *args, **kvargs)
  
  def onInit(self):
    listControl = self.getControl(50111)
    self.getControl(50112).setWidth((len(self.buttons)+1) * 85 + 10)
    self.getControl(50113).setWidth((len(self.buttons)+1) * 85)
    self.getControl(50111).setWidth((len(self.buttons)+1) * 85)
    listControl.addItems(self.buttons)
    self.getControl(50111).selectItem(0)
    self.setFocus(50111)
      
  def onClick(self, controlId):
    print('&*&*&*&' + str(controlId))
    xbmc.executebuiltin('RunScript(special://home/addons/plugin.program.vpftools/plugin.py, ' + self.getControl(50111).getSelectedItem().getPath() + ')')
    #self.close()
