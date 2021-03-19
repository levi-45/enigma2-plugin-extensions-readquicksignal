#!/usr/bin/python
# -*- coding: utf-8 -*-
#RAEDQuickSignal (c) RAED 07-02-2014
#Thank's mfaraj to help with some codes

# python3
from __future__ import print_function

from Components.config import config, getConfigListEntry, ConfigText, ConfigSelection, ConfigSubsection, ConfigYesNo, configfile, NoSave
from Components.ConfigList import ConfigListScreen
from Components.ActionMap import ActionMap
from GlobalActions import globalActionMap
from keymapparser import readKeymap
from enigma import eTimer, getDesktop, gFont, addFont
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from Screens.Standby import TryQuitMainloop
from Screens.ChannelSelection import ChannelSelection
from Screens.MessageBox import MessageBox
from Tools.Directories import fileExists
from Components.Sources.StaticText import StaticText
from Tools.Directories import *
from Components.config import *
from Screens.InputBox import InputBox
from Components.MenuList import MenuList
from Components.Label import Label
from datetime import datetime
import os, re, gettext

# import as python3 from plugin
from .screens.skin import *
from .tools.compat import PY3
from .tools.compat import compat_urlopen
from .tools.compat import compat_Request
from .tools.compat import compat_URLError
from .tools.Console import Console
from os import path as os_path, remove as os_remove
from six.moves.urllib.request import urlretrieve

Satfinderpy=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/Satfinder/plugin.py")
Satfinderpyo=resolveFilename(SCOPE_PLUGINS, "SystemPlugins/Satfinder/plugin.pyo")
FONTPLUGIN=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/images/")
PREVIEWPIC=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/images/preview/")

FONTSPATH = '/usr/share'
GETPath = os.path.join(FONTSPATH + '/fonts')

if os.path.exists(FONTSPATH + '/fonts/nmsbd.ttf'):
	DEFAULTFont =  'nmsbd'
else:
	fontfile = FONTPLUGIN + 'nmsbd.ttf'
	DEFAULTFont = addFont(fontfile, 'RSQFont', 100, 1)

fonts = []
try:
    if os.path.exists(GETPath):
        for fontName in os.listdir(GETPath):
            fontNamePath = os.path.join(GETPath, fontName)
            if fontName.endswith('.ttf'):
            	fontName = fontName[:-4]
            	fonts.append((fontNamePath, fontName))
except:
    print('Error in gettings fonts')

def removeunicode(data):
        try:
            try:
                data = data.encode('utf', 'ignore')
            except:
                pass
            data = data.decode('unicode_escape').encode('ascii', 'replace').replace('?', '').strip()
        except:
            pass
        return data

def getversioninfo():
    currversion='1.0'
    version_file=resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/tools/version")
    if os_path.exists(version_file):
        try:
            fp=open(version_file, 'r').readlines()
            for line in fp:
                if 'version' in line:
                    currversion=line.split('=')[1].strip()
        except:
            pass
    return (currversion)

VER = getversioninfo()

def trace_error():
    import sys
    import traceback
    try:
        traceback.print_exc(file=sys.stdout)
        traceback.print_exc(file=open('/tmp/RaedQuickSignal.log', 'a'))
    except:
        pass

def logdata(label_name = '', data = None):
    try:
        data=str(data)
        fp = open('/tmp/RaedQuickSignal.log', 'a')
        fp.write( str(label_name) + ' : ' + data+"\n")
        fp.close()
    except:
        trace_error()    
        pass

def dellog(label_name = '', data = None):
    try:
        if os_path.exists('/tmp/RaedQuickSignal.log'):
                os_remove('/tmp/RaedQuickSignal.log')
    except:
        pass

def DreamOS():
    if os_path.exists('/var/lib/dpkg/status'):
        return DreamOS

def BHVU():
    if os_path.exists('/proc/stb/info/vumodel') and os_path.exists('/usr/lib/enigma2/python/Blackhole'):
        return BHVU

def getDesktopSize():
    s = getDesktop(0).size()
    return (s.width(), s.height())

def isHD():
    desktopSize = getDesktopSize()
    return desktopSize[0] == 1280
##############################################################################
#if isHD():
#        Space = "             "
#        SKIN_setup = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Setup.xml")
#        SKIN_WeatherLocation = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/WeatherLocation.xml")
#        SKIN_AGC_Picon = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Picon.xml")
#        SKIN_AGC_Event_Des = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Event_Des.xml")
#        SKIN_AGC_Weather = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Weather.xml")
#        SKIN_Event_Progress_Picon = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Picon.xml")
#        SKIN_Event_Progress_Event_Des = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Event_Des.xml")
#        SKIN_Event_Progress_Weather = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Weather.xml")
#        SKIN_AGC_Picon_media = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Picon_media.xml"
#        SKIN_Event_Progress_Picon_media = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Picon_media.xml")
#else:
#        Space = "                                          "
#        SKIN_setup = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Setup_FHD.xml")
#        SKIN_WeatherLocation = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/WeatherLocation.xml")
#        SKIN_AGC_Picon = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Picon_FHD.xml")
#        SKIN_AGC_Event_Des = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Event_Des_FHD.xml")
#        SKIN_AGC_Weather = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Weather_FHD.xml")
#        SKIN_Event_Progress_Picon = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Picon_FHD.xml")
#        SKIN_Event_Progress_Event_Des = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Event_Des_FHD.xml")
#        SKIN_Event_Progress_Weather = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Weather_FHD.xml")
#        SKIN_AGC_Picon_media = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/AGC_Picon_media_FHD.xml")
#        SKIN_Event_Progress_Picon_media = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/screens/Event_Progress_Picon_media_FHD.xml")
##############################################################################
config.plugins.RaedQuickSignal = ConfigSubsection()
config.plugins.RaedQuickSignal.updateonline = ConfigYesNo(default=True)
config.plugins.RaedQuickSignal.enabled = ConfigYesNo(default=True)
config.plugins.RaedQuickSignal.fonts = ConfigSelection(default=DEFAULTFont, choices=fonts)
#config.plugins.RaedQuickSignal.fonts = ConfigSelection(default = "nmsbd", choices = [
#                ("nmsbd", "nmsbd"),
#                ("analog", "analog"),
#                ("setrixHD", "setrixHD"),
#                ("army-digital", "army-digital"),
#                ("ForgottenFuturistShadow", "ForgottenFuturistShadow"),
#                ])
config.plugins.RaedQuickSignal.keyname = ConfigSelection(default = "KEY_TEXT", choices = [
                ("KEY_TEXT", "TEXT"),
                ("KEY_TV", "TV"),
                ("KEY_RADIO", "RADIO"),
                ("KEY_OK", "OK"),
                ("KEY_HELP", "HELP"),
                ("KEY_INFO", "INFO"),
                ("KEY_RED", "RED"),
                ("KEY_GREEN", "GREEN"),
                ("KEY_BLUE", "BLUE"),
                ("KEY_PVR", "PVR"),
                ("KEY_0", "0"),
                ("KEY_1", "1"),
                ("KEY_2", "2"),
                ("KEY_3", "3"),
                ("KEY_F1", "f1"),
                ("KEY_F2", "f2"),
                ("KEY_F3", "f3"),
                ])
config.plugins.RaedQuickSignal.style = ConfigSelection(default = "AGC1", choices = [
                ("AGC1", "AGC Progress + Picon"),
                ("AGC2", "AGC Progress + Event Description"),
                ("AGC3", "AGC Progress + Weather"),
                ("Event1", "Event Progress + Picon"),
                ("Event2", "Event Progress + Event Description"),
                ("Event3", "Event Progress + Weather"),
                ("Full", "Full Screen without any extra functions"),
                ])
config.plugins.RaedQuickSignal.enabledBD = ConfigSelection(default = "Enable", choices = [
                ("Enable", "Enable show db value"),
                ("Disable", "Disable show db value")
                ])
config.plugins.RaedQuickSignal.piconpath = ConfigSelection(default = "PLUGIN", choices = [
                ("PLUGIN", "Set Picon Path from Plugin"),
                ("MEDIA", "Set Picon Path from /media"),
                ])
config.plugins.RaedQuickSignal.refreshInterval = ConfigNumber(default=30) #in minutes
##############################################################################
try:
        config.plugins.RQweather = ConfigSubsection()       
        config.plugins.RQweather.city = ConfigText(default="Manama", visible_width = 250, fixed_size = False)       
        config.plugins.RQweather.windtype = ConfigSelection(default="ms", choices = [
                ("ms", _("m/s")),
                ("fts", _("ft/s")),
                ("kmh", _("km/h")),
                ("mph", _("mp/h")),
                ("knots", _("knots"))])
        config.plugins.RQweather.degreetype = ConfigSelection(default="C", choices = [
                ("C", _("Celsius")),
                ("F", _("Fahrenheit"))])
        config.plugins.RQweather.weather_location= ConfigText(default="bh-BH", visible_width = 250, fixed_size = False)       
except:
        trace_error()
        pass

import gettext
REDC =  '\033[31m'
ENDC = '\033[m'

def cprint(text):
    print(REDC+"[RaedQuickSignal] "+text+ENDC)

def downloadFile(url, filePath):
    try:
        # Download the file from `url` and save it locally under `file_name`:
        urlretrieve(url, filePath)
        return True
        req = compat_Request(url)
        response = compat_urlopen(req)         
        cprint("response.read",response.read())
        output = open(filePath, 'wb')
        output.write(response.read())
        output.close()
        response.close()
        return True
    except compat_URLError as e:
        trace_error()
        if hasattr(e, 'code'):
            cprint('We failed with error code - %s.' % e.code)
        elif hasattr(e, 'reason'):
            cprint('We failed to reach a server.')
            cprint('Reason: %s' % e.reason)
    return False

def readurl(url):
    try:
        req = compat_Request(url)
        response = compat_urlopen(req)
        data = response.read()
        response.close()
        cprint("[data %s]" % data)
        return data
    except compat_URLError as e:
        if hasattr(e, 'code'):
            cprint('We failed with error code - %s.' % e.code)
        elif hasattr(e, 'reason'):
            cprint('We failed to reach a server.')
            cprint('Reason: %s' % e.reason)

def getcities(weather_location):

    import requests,re
    S = requests.Session()
    url = (b"http://www.geonames.org/advanced-search.html?q=&country=%s&featureClass=P&startRow=".decode("utf-8")) % str(weather_location.upper())
    pages = range(0, 1501, 50) ## change 2001 as page you want
    try:
        cities=[]
        for page in pages:
                ##Change the startRow in the URL
                url_2 = url.replace("startRow=","startRow="+str(page))
                request = requests.get(url_2)
                if request.status_code == 200:
                        data = S.get(url_2, verify=False).content.decode('ascii', 'ignore')
                        blocks = str(data).split('alt="P">')
                        blocks.pop(0)
                        for block in blocks:
                                regx='''<a href="(.*?)">.*?</a>'''
                                href = re.findall(regx, block)[0]
                                cityName = os.path.split(href)[1].replace(".html","").replace("-"," ").lstrip(' ')
                                #cityName = re.findall(str(regx), str(block), re.M|re.I)[0]#.replace(".html","").split("_%", 1)[0].split("%", 1)[0]
                                cities.append(cityName)
                        cities.sort()
    except Exception as error:
                cprint('excepyion',str(error))
                trace_error()
    cities.sort()
    return cities

##### Old
        #url = (b"http://www.geonames.org/advanced-search.html?q=&country=%s&featureClass=P&continentCode=".decode("utf-8")) % str(weather_location.upper())
        #data = readurl(url)
        #if data == None:
        #        return []
        #try:
        #        regx='''<a href="(.*?)"><img src=".*?" border="0" alt=".*?"></a>'''
        #        match = re.findall(str(regx), str(data), re.M|re.I)
        #        cities = []
        #        for cityURL in match:
        #            cityName = os.path.split(cityURL)[1].replace(".html","").split("_%", 1)[0].split("%", 1)[0]    
        #            if cityName in cities:
        #                continue
        #            cities.append(cityName)
        #        cities.sort()
        #        return cities
        #except Exception as error:
        #        trace_error()

class WeatherLocationChoiceList(Screen):
        def __init__(self, session, country):
                self.skin = SKIN_WeatherLocation
                #with open(SKIN_WeatherLocation, 'r') as f:
                #     self.skin = f.read()
                #     f.close()
                self.session = session
                self.country = country
                list = []
                Screen.__init__(self, session)
                self.title = _(country)
                self["choicelist"] = MenuList(list)
                self["key_red"] = Label(_("Cancel"))
                self["key_green"] = Label(_("Add city"))
                self["myActionMap"] = ActionMap(["SetupActions", "ColorActions"],
                {
                        "ok": self.keyOk,
                        "green": self.add_city,
                        "cancel": self.keyCancel,
                        "red": self.keyCancel,
                }, -1)
                #self.iConsole = iConsole()             
                self.timer = eTimer()
                try:
                        self.timer.callback.append(self.createChoiceList)
                except:
                        self.timer_conn = self.timer.timeout.connect(self.createChoiceList)
                self.timer.start(5, False)

        def createChoiceList(self):
                self.timer.stop()
                clist = []
                clist=getcities(self.country)
                self["choicelist"].l.setList(clist)

        def control_xml(self, result, retval, extra_args):
                if retval != 0:
                        self.write_none()

        def write_none(self):
                with open('/tmp/weathermsn.xml', 'w') as noneweather:
                        noneweather.write('None')
                noneweather.close()

        def get_xmlfile(self,weather_city,weather_location):
                degreetype = config.plugins.RQweather.degreetype.value
                weather_city = removeunicode(weather_city)
                weather_city = weather_city.decode("utf-8")
                url = 'http://weather.service.msn.com/data.aspx?weadegreetype=%s&culture=%s&weasearchstr=%s&src=outlook' % (degreetype, weather_location, weather_city)
                file_name ='/tmp/weathermsn.xml'
                # Download the file from `url` and save it locally under `file_name`:
                try:
                       ret=downloadFile(url, file_name)
                       return ret
                except Exception as error:### new
                       trace_error()
                       return False
                #self.iConsole.ePopen("wget -P /tmp -T2 'http://weather.service.msn.com/data.aspx?weadegreetype=%s&culture=%s&weasearchstr=%s&src=outlook' -O /tmp/weathermsn.xml" % (degreetype, weather_location, weather_city), self.control_xml)

        def add_city(self):
                 self.session.openWithCallback(self.cityCallback, InputBox, title=_("Please enter a name of the city"), text="cityname", maxSize=False, visible_width =250)

        def cityCallback(self,city=None):
                try:
                        if os_path.exists('/tmp/weathermsn.xml'):
                                os_remove('/tmp/weathermsn.xml')
                        returnValue = self["choicelist"].l.getCurrentSelection()
                        countryCode=self.country.lower()+"-"+self.country.upper()
                        if self.get_xmlfile(returnValue,countryCode)==False:
                                self.session.open(MessageBox, _("Sorry, your city is not available1."),MessageBox.TYPE_ERROR)
                                return 
                        if not fileExists('/tmp/weathermsn.xml'):
                                self.write_none()
                                self.session.open(MessageBox, _("Sorry, your city is not available2."),MessageBox.TYPE_ERROR)
                                return None
                        if returnValue != None:
                                self.close(returnValue)
                        else:
                                self.keyCancel()
                except Exception as error:
                        trace_error()

        def keyOk(self):
                try:
                        if os_path.exists('/tmp/weathermsn.xml'):
                                os_remove('/tmp/weathermsn.xml')
                        returnValue = self["choicelist"].l.getCurrentSelection()
                        countryCode=self.country.lower()+"-"+self.country.upper()
                        if self.get_xmlfile(returnValue,countryCode)==False:
                                self.session.open(MessageBox, _("Sorry, your city is not available."),MessageBox.TYPE_ERROR)
                                return 
                        if not fileExists('/tmp/weathermsn.xml'):
                                self.write_none()
                                self.session.open(MessageBox, _("Sorry, your city is not available."),MessageBox.TYPE_ERROR)
                                return None
                        if returnValue != None:
                                self.close(returnValue)
                        else:
                                self.keyCancel()
                except Exception as error:
                        trace_error()

        def keyCancel(self):
                self.close(None)

class RaedQuickSignalScreen(Screen):
        def __init__(self, session):
                Screen.__init__(self, session)
                dellog()
                ## Add Fonts codes
                try:
                	fontfile = config.plugins.RaedQuickSignal.fonts.value
                	addFont(fontfile, 'RSQFont', 100, 1)
                except:
                	try:
                		fontfile = FONTPLUGIN + 'nmsbd.ttf'
                		addFont(fontfile, 'RSQFont', 100, 1)
                	except Exception as ex:
                		print('addfont', ex)
                ## End Add Fonts codes
                if config.plugins.RaedQuickSignal.style.value == "AGC1":
                        if config.plugins.RaedQuickSignal.piconpath.value == "PLUGIN":
                             if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                                   if isHD():
                                         self.skin = SKIN_AGC_Picon_SNRdB
                                   else:
                                         self.skin = SKIN_AGC_Picon_SNRdB_FHD
                             else:
                                   if isHD():
                                         self.skin = SKIN_AGC_Picon_NOSNRdB
                                   else:
                                         self.skin = SKIN_AGC_Picon_NOSNRdB_FHD
                        elif config.plugins.RaedQuickSignal.piconpath.value == "MEDIA":
                             if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                                   if isHD():
                                         self.skin = SKIN_AGC_Picon_media_SNRdB
                                   else:
                                         self.skin = SKIN_AGC_Picon_media_SNRdB_FHD
                             else:
                                   if isHD():
                                         self.skin = SKIN_AGC_Picon_media_NOSNRdB
                                   else:
                                         self.skin = SKIN_AGC_Picon_media_NOSNRdB_FHD
                elif config.plugins.RaedQuickSignal.style.value == "AGC2":
                        if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                             if isHD():
                                   self.skin = SKIN_AGC_Event_Des_SNRdB
                             else:
                                   self.skin = SKIN_AGC_Event_Des_SNRdB_FHD
                        else:
                             if isHD():
                                   self.skin = SKIN_AGC_Event_Des_NOSNRdB
                             else:
                                   self.skin = SKIN_AGC_Event_Des_NOSNRdB_FHD
                elif config.plugins.RaedQuickSignal.style.value == "AGC3":
                        if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                             if isHD():
                                   self.skin = SKIN_AGC_Weather_SNRdB
                             else:
                                   self.skin = SKIN_AGC_Weather_SNRdB_FHD
                        else:
                             if isHD():
                                   self.skin = SKIN_AGC_Weather_NOSNRdB
                             else:
                                   self.skin = SKIN_AGC_Weather_NOSNRdB_FHD
                elif config.plugins.RaedQuickSignal.style.value == "Event1":
                        if config.plugins.RaedQuickSignal.piconpath.value == "PLUGIN":
                             if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                                   if isHD():
                                         self.skin = SKIN_Event_Progress_Picon_SNRdB
                                   else:
                                         self.skin = SKIN_Event_Progress_Picon_SNRdB_FHD
                             else:
                                   if isHD():
                                         self.skin = SKIN_Event_Progress_Picon_NOSNRdB
                                   else:
                                         self.skin = SKIN_Event_Progress_Picon_NOSNRdB_FHD
                        elif config.plugins.RaedQuickSignal.piconpath.value == "MEDIA":
                             if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                                   if isHD():
                                         self.skin = SKIN_Event_Progress_Picon_media_SNRdB
                                   else:
                                         self.skin = SKIN_Event_Progress_Picon_media_SNRdB_FHD
                             else:
                                   if isHD():
                                         self.skin = SKIN_Event_Progress_Picon_media_NOSNRdB
                                   else:
                                         self.skin = SKIN_Event_Progress_Picon_media_NOSNRdB_FHD
                elif config.plugins.RaedQuickSignal.style.value == "Event2":
                        if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                             if isHD():
                                   self.skin = SKIN_Event_Progress_Event_Des_SNRdB
                             else:
                                   self.skin = SKIN_Event_Progress_Event_Des_SNRdB_FHD
                        else:
                             if isHD():
                                   self.skin = SKIN_Event_Progress_Event_Des_NOSNRdB
                             else:
                                   self.skin = SKIN_Event_Progress_Event_Des_NOSNRdB_FHD
                elif config.plugins.RaedQuickSignal.style.value == "Event3":
                        if config.plugins.RaedQuickSignal.enabledBD.value == "Enable":
                             if isHD():
                                   self.skin = SKIN_Event_Progress_Weather_SNRdB
                             else:
                                   self.skin = SKIN_Event_Progress_Weather_SNRdB_FHD
                        else:
                             if isHD():
                                   self.skin = SKIN_Event_Progress_Weather_NOSNRdB
                             else:
                                   self.skin = SKIN_Event_Progress_Weather_NOSNRdB_FHD
                elif config.plugins.RaedQuickSignal.style.value == "Full":
                       if isHD():
                             self.skin = SKIN_Full_Screen
                       else:
                             self.skin = SKIN_Full_Screen_FHD
                self.session = session
                if not DreamOS() and not BHVU():
                        self.startupservice = config.servicelist.startupservice.value
                        sref = self.session.nav.getCurrentService()
                        from ServiceReference import ServiceReference
                        p = ServiceReference(str(sref))
                        servicename = str(p.getServiceName())
                        serviceurl = p.getPath()
                        config.servicelist.startupservice.value = serviceurl
                        config.servicelist.startupservice.save()
                self.servicelist = self.session.instantiateDialog(ChannelSelection)
                self["setupActions"] = ActionMap(["WizardActions", "SetupActions", "MenuActions", "ColorActions"],
                    {
                         "cancel": self.exit,
                         "menu":self.showsetup,
                         "up": self.keyUp,
                         "down": self.keyDown,
                         "left": self.keyLeft,
                         "right": self.keyRight,
                         "blue": self.keyblue,
                    })
                shown=True
                #self.onLayoutFinish.append(self.layoutFinished)
                if os.path.exists(Satfinderpy) or os.path.exists(Satfinderpyo):
                	self["Satfinder"] = Label(_("Blue Button(Open Satfinder)"))
                else:
                	self["Satfinder"] = Label(_(""))
                self.onShown.append(self.onWindowShow)

        def onWindowShow(self):
                self.onShown.remove(self.onWindowShow)
                self.instance.show()
                #self.setTitle("QuickSignal by RAED V" + str(VER + Space + datetime_now))
                self.setTitle("RaedQuickSignal V %s" % VER)
                self.new_version = VER
                updateOnline = config.plugins.RaedQuickSignal.updateonline.value
                if updateOnline:
                         self.checkupdates()
                cfile = open("/tmp/.qsignal","w")
                cfile.close()

        #def layoutFinished(self):
        #        self.instance.show()
                #self.setTitle("QuickSignal by RAED V" + str(VER + Space + datetime_now))
        #        self.setTitle("RaedQuickSignal V %s" % VER)
        #        self.new_version = VER
        #        if config.plugins.RaedQuickSignal.updateonline.value:
        #                 self.checkupdates()
        #        cfile = open("/tmp/.qsignal","w")
        #        cfile.close()

        def keyblue(self):
                try:
                	if os.path.exists(Satfinderpy) or os.path.exists(Satfinderpyo):
                		from Plugins.SystemPlugins.Satfinder.plugin import Satfinder
                		self.session.open(Satfinder)
                	else:
                		print('Satfinder Not Installed')
                except:
                	print('Satfinder Not Installed')

        def keyLeft(self):
                self.servicelist.moveUp()
                self.servicelist.zap()

        def keyRight(self):
                self.servicelist.moveDown()
                self.servicelist.zap()

        def keyUp(self):
                self.session.execDialog(self.servicelist)

        def keyDown(self):
                self.session.execDialog(self.servicelist)

        def exit(self):
                if os_path.exists("/tmp/.qsignal"):
                        os_remove("/tmp/.qsignal")
                if not DreamOS() and not BHVU():
                        config.servicelist.startupservice.value = self.startupservice
                        config.servicelist.startupservice.save()
                self.close()

        def setupback(self,answer=False):
                if answer:
                        self.exit()
                        
        def showsetup(self):
                self.session.openWithCallback(self.setupback,RaedQuickSignal_setup)

        def checkupdates(self):
               try:
                       from twisted.web.client import getPage, error
                       url = b"http://tunisia-dreambox.info/TSplugins/RaedQuickSignal/installer.sh" 
                       getPage(url,timeout=10).addCallback(self.parseData).addErrback(self.errBack)
               except Exception as error:
                       trace_error()

        def errBack(self,error=None):
               logdata("errBack-error",error)

        def parseData(self, data):
               if PY3:
                   data = data.decode("utf-8")
               else:
                   data = data.encode("utf-8")
               if data:
                   lines = data.split("\n")
                   for line in lines:
                       if line.startswith("version"):
                          self.new_version = line.split("=")[1]
                          #break #if enabled the for loop will exit before reading description line
                       if line.startswith("description"):
                          self.new_description = line.split("=")[1]
                          break
               logdata("Current VER",VER)
               logdata('New VER',self.new_version)
               if float(VER) == float(self.new_version) or float(VER)>float(self.new_version):
                   logdata("Updates","No new version available")
               else :
                   new_version = self.new_version
                   new_description = self.new_description
                   self.session.openWithCallback(self.install, MessageBox, _('New version %s is available.\n\n%s.\n\nDo want ot install now.' % (new_version, new_description)), MessageBox.TYPE_YESNO)

        def install(self,answer=False):
                try:
                     if answer:
                           cmdlist = []
                           cmd='wget http://tunisia-dreambox.info/TSplugins/RaedQuickSignal/installer.sh -O - | /bin/sh'
                           cmdlist.append(cmd)
                           self.session.open(Console, title='Installing last update, enigma will be started after install', cmdlist=cmdlist, finishedCallback=self.myCallback, closeOnSuccess=False)
                except:
                           trace_error()
        
        def myCallback(self,result):
                return

class RaedQuickSignal():
        def __init__(self):
                self.dialog = None

        def gotSession(self, session):
                self.session = session
                self.qsignal = None
                if os_path.exists("/tmp/.qsignal"):
                        os_remove("/tmp/.qsignal")
                keymap = resolveFilename(SCOPE_PLUGINS, "Extensions/RaedQuickSignal/tools/keymap.xml")
                global globalActionMap
                readKeymap(keymap)
                if 'displayHelp' in globalActionMap.actions:
                        del globalActionMap.actions['displayHelp']
                elif 'showSherlock' in globalActionMap.actions:
                        del globalActionMap.actions['showSherlock']
                globalActionMap.actions['showRaedQuickSignal'] = self.ShowHide

        def ShowHide(self):
                if os_path.exists("/tmp/.qsignal") == False:
                        if config.plugins.RaedQuickSignal.enabled.value:
                                self.session.open(RaedQuickSignalScreen)

#################################
pSignal = RaedQuickSignal()
#################################

class RaedQuickSignal_setup(ConfigListScreen, Screen):
        def __init__(self, session):
                self.session = session
                Screen.__init__(self, session, self.changedEntry)
                if isHD():
                        self.skin = SKIN_setup
                else:
                        self.skin = SKIN_setup_FHD
                #self.setTitle(_("RaedQuickSignal setup V" + VER))
                self.setTitle("RaedQuickSignal setup V %s" % VER)
                self.RaedQuickSignal_fake_entry = NoSave(ConfigNothing())
                list = []
                ConfigListScreen.__init__(self, list, on_change = self.changedEntry)
                self.configChanged = False
                self["key_red"] = StaticText(_("Close"))
                self["key_green"] = StaticText(_("Save"))
                #self["key_yellow"] = StaticText(_(" "))
                #self["key_blue"] = StaticText(_(" "))
                self["setupActions"] = ActionMap(["SetupActions", "ColorActions", "EPGSelectActions"],
                {
                        "red": self.cancel,
                        "cancel": self.cancel,
                        "green": self.save,
                        #"yellow": self.restart,
                        #"blue": self.keyOk,
                        "ok": self.keyOk
                }, -2)
                self["Picture"] = Pixmap()
                self["help"] = StaticText()
                self.createConfigList()

        #def run(self):
        #          self.session.open(RaedQuickSignalScreen)

        def createConfigList(self):
                self.configChanged = True
                self.currenabled_value = config.plugins.RaedQuickSignal.enabled.value
                self.currkeyname_value = config.plugins.RaedQuickSignal.keyname.value

                self.set_enabled = getConfigListEntry(_("Enable Plugin"), config.plugins.RaedQuickSignal.enabled, _("This option for Enable or Disable Plugin"))
                self.set_updateonline = getConfigListEntry(_("Enable/Disable Check for update"), config.plugins.RaedQuickSignal.updateonline, _("This option for Enable or Disable Check for update"))
                self.set_keyname = getConfigListEntry(_("Select key"), config.plugins.RaedQuickSignal.keyname, _("This option for choose Hot key to show RaedQuickSignal"))
                self.set_enabledBD = getConfigListEntry(_("Enable/Disable DB Value"), config.plugins.RaedQuickSignal.enabledBD, _("This option for Enable or Disable DB tuner Value"))
                self.set_piconpath = getConfigListEntry(_("Select Path Of Picons Folder"), config.plugins.RaedQuickSignal.piconpath, _("This option for  Select Path to pring picons from insdie or outside plugin"))
                self.set_style = getConfigListEntry(_("Select Style of Plugin"), config.plugins.RaedQuickSignal.style, _("This option for Select what skins Style you like to use"))
                self.set_fonts = getConfigListEntry(_("Select Style of Font"), config.plugins.RaedQuickSignal.fonts, _("This option for Select what font Style you like to use.\n\nAnd you can also add new fonts in (/use/share/fonts).\n(NEED) do Restart GUI if add new fonts"))
                self.set_refreshInterval = getConfigListEntry(_("Refresh interval in minutes:"), config.plugins.RaedQuickSignal.refreshInterval, _("This option for Adjust times to update weather info"))
                self.set_degreetype = getConfigListEntry(_("Temperature unit:"), config.plugins.RQweather.degreetype, _("This option for Select type of Temperature what you need"))
                self.set_city = getConfigListEntry(_("Location #press OK to change:"), config.plugins.RQweather.city, _("This option for choose your city name and code for weather"))

                self.list = []
                self.list.append(getConfigListEntry(_(" ________________________ 礑 Plugin 礑 ________________________"), ))
                self.list.append(self.set_enabled)
                self.list.append(self.set_updateonline)
                self.list.append(self.set_keyname)
                self.list.append(getConfigListEntry(_(" _________________________ 礑 Skin 礑 _________________________"), ))
                self.list.append(self.set_enabledBD)
                self.list.append(self.set_piconpath)
                self.list.append(self.set_style)
                self.list.append(self.set_fonts)
                self.list.append(getConfigListEntry(_(" ________________________ 礑 Weather 礑 ________________________"), ))
                self.list.append(self.set_refreshInterval)
                self.list.append(self.set_degreetype)
                self.list.append(self.set_city)

                self["config"].list = self.list
                self["config"].l.setList(self.list)
                self["config"].onSelectionChanged.append(self.updateHelp)
                self["config"].onSelectionChanged.append(self.Picture)

                #if not isHD() and DreamOS():
                #        self["config"].l.setValueFont(gFont("Regular", 30)) ## set font to config menu (DreamOS images Need it)
                #        self["config"].l.setItemHeight(40) ## set ItemHeight to config menu (DreamOS images Need it)

	def updateHelp(self):
		cur = self["config"].getCurrent()
		if cur:
			self["help"].text = cur[2]

	def Picture(self):
		try:
			cur = self["config"].getCurrent()
			if cur == self.set_style:
				preview = PREVIEWPIC + "%s.png" % config.plugins.RaedQuickSignal.style.value
				if os.path.exists(preview):
					self['Picture'].instance.setPixmapFromFile(preview)
					self["Picture"].show()
				else:
					print('No preview image')
			else:
				self["Picture"].hide()
		except Exception as error:
			cprint(str(error))

        def keyLeft(self):
                ConfigListScreen.keyLeft(self)
                self.Picture()

        def keyRight(self):
                ConfigListScreen.keyRight(self)
                self.Picture()

        def cancel(self):
                for i in self["config"].list:
                        if len(i)>1:
                        	i[1].cancel()
                self.close(False)

        def restart(self,answer=None):
                if answer:
                   self.session.open(TryQuitMainloop, 3)
                   return
                self.close(True)

        def keyOk(self):
                cur = self["config"].getCurrent()
                if cur == self.set_city:
            		countriesFile = resolveFilename(SCOPE_PLUGINS, 'Extensions/RaedQuickSignal/tools/countries')
            		countries=open(countriesFile).readlines()
            		clist=[]
            		for country in countries:
                		countryCode,countryName=country.split(",")
                		clist.append((countryName,countryCode))
            		from Screens.ChoiceBox import ChoiceBox
            		self.session.openWithCallback(self.choicesback, ChoiceBox, _('select your country\nAnd wait to download data after Press (Ok)'), clist)

        def choicesback(self, select):
                if select:
                    self.country=select[1]
                    config.plugins.RQweather.weather_location.value=self.country.lower()+"-"+self.country.upper()
                    config.plugins.RQweather.weather_location.save()
                    self.session.openWithCallback(self.citiesback, WeatherLocationChoiceList, self.country)
                    
        def citiesback(self,select):
                if select:
                  weather_city = select
                  weather_city.capitalize() 
                  config.plugins.RQweather.city.setValue(weather_city)
                  self.createConfigList()

        def save(self):
                #if self["config"].isChanged():
                if self.configChanged:
                        for x in self["config"].list:
                        	if len(x)>1:
                            		x[1].save()
                        configfile.save()
                        # we can not use resolveFilename(SCOPE_PLUGINS) here the keymap.xml will be not writable 
                        if not os_path.exists('/usr/lib64'):
                            keyfile = open("/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/tools/keymap.xml", "w")
                        else:
                            keyfile = open("/usr/lib64/enigma2/python/Plugins/Extensions/RaedQuickSignal/tools/keymap.xml", "w")
                        keyfile.write('<keymap>\n\t<map context="GlobalActions">\n\t\t<key id="%s" mapto="showRaedQuickSignal" flags="m" />\n\t</map>\n</keymap>' % config.plugins.RaedQuickSignal.keyname.value)
                        keyfile.close()
                        if not self.currkeyname_value == config.plugins.RaedQuickSignal.keyname.value: # not self.currenabled_value == config.plugins.RaedQuickSignal.enabled.value
                           self.session.openWithCallback(self.restart, MessageBox, _("Settings changed,restart enigma2 now?"))
                        else:
                                self.close(True)
                else:
                        self.close(False)
##############################################################################
def sessionstart(reason, session = None, **kwargs):
        if reason == 0:
                pSignal.gotSession(session)
##############################################################################
def main(session, **kwargs):
        session.open(RaedQuickSignal_setup)
##############################################################################
def Plugins(**kwargs):
        result = [
                PluginDescriptor(
                        where = [PluginDescriptor.WHERE_SESSIONSTART],
                        fnc = sessionstart
                ),
                PluginDescriptor(
                        name=_("RaedQuickSignal Setup"),
                        description = _("RAED's RaedQuickSignal setup"),
                        where = PluginDescriptor.WHERE_PLUGINMENU,
                        icon = 'images/RaedQuickSignal.png',
                        fnc = main
                ),
        ]
        return result
