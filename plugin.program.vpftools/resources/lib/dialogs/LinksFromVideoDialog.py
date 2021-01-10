import xbmc
import xbmcgui
import xbmcaddon
import simplejson as json
class LinksFromVideoDialog(xbmcgui.WindowXMLDialog):
  def __init__(self, *args, **kvargs):#xmlFilename="plugin-extrabuttons-links.xml", scriptPath=xbmcaddon.Addon("plugin.program.vpftools").getAddonInfo('path'), defaultSkin="default", defaultRes="1080i", comments=None, loadMoreFunction = None, replyFunction = None):
    self.buttons = self.generateButtons(kvargs['links'])
    xbmcgui.WindowXMLDialog.__init__(self, *args, **kvargs)
  def generateButtons(self, links):
    #{'name': name, 'link': link, 'kodiLink': kodiLink}
    result = []
    for link in links:
      print('jjjjjjjjjjjjjjjjjjjjjjj')
      print(json.dumps(link))
      print('jjjjjjjjjjjjjjjjjjjjjjj')
      label = link['name']
      path = link['link']
      if link['kodiLink']:
        label2 = 'Open in kodi'
      else:
        label2 = path
      li = xbmcgui.ListItem(label, label2)
      li.setPath(path=path)
      result.append(li)
    return result
  def onInit(self):
    listControl = self.getControl(50111)
    listControl.addItems(self.buttons)
    self.getControl(50111).selectItem(0)
    self.setFocus(50111)
      
  def onClick(self, controlId):
    print('&*&*&*&' + str(controlId))
    xbmc.executebuiltin('RunScript(special://home/addons/plugin.program.vpftools/plugin.py, ' + self.getControl(50111).getSelectedItem().getPath() + ')')
    #self.close()
