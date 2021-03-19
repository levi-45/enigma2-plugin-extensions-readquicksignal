# Created BY RAED 18-11-2019

from Screens.Screen import Screen
from Components.Pixmap import Pixmap
import os

def DreamOS():
    if os.path.exists('/var/lib/dpkg/status'):
        return DreamOS

### SKIN_setup
SKIN_setup = """
<screen backgroundColor="#16000000" name="RaedQuickSignal_setup" position="center,center" size="745,662" title="RAED's RaedQuickSignal setup" flags="wfNoBorder">
  <eLabel position="0,40" size="745,1" zPosition="10" backgroundColor="#00ffffff" transparent="0"/>
  <widget source="Title" render="Label" font="RSQFont;24" foregroundColor="#00bab329" position="20,5" size="712,34" transparent="1" />
  <widget name="config" position="15,45" size="720,341" scrollbarMode="showOnDemand" backgroundColor="#16000000"/>
  <widget source="key_red" render="Label" position="17,625" zPosition="2" size="165,30" font="RSQFont;20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <widget source="key_green" render="Label" position="206,625" zPosition="2" size="165,30" font="RSQFont;20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <!--widget source="key_yellow" render="Label" position="387,625" zPosition="2" size="200,30" font="RSQFont;20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <widget source="key_blue" render="Label" position="566,624" zPosition="2" size="200,30" font="RSQFont;20" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" /-->
  <ePixmap position="17,658" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/red.png" alphatest="blend" />
  <ePixmap position="206,658" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/green.png" alphatest="blend" />
  <!--ePixmap position="387,658" zPosition="1" size="200,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/yellow.png" alphatest="blend" />
  <ePixmap position="561,658" zPosition="1" size="200,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/blue.png" alphatest="blend" /-->
  <widget source="help" render="Label" position="15,391" size="309,225" font="Regular;23" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="330,225" size="400,225" zPosition="5" alphatest="on"/>
  <ePixmap position="448,439" zPosition="3" size="150,150" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/fairbirdhd.png" alphatest="blend" />
 </screen>
"""
if DreamOS():
      SKIN_setup_FHD = """
<screen backgroundColor="#16000000" name="RaedQuickSignal_setup" position="center,center" size="1050,899" title="RAED's RaedQuickSignal setup" flags="wfNoBorder">
  <eLabel position="0,53" size="1050,1" zPosition="10" backgroundColor="#00ffffff" transparent="0"/>
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bab329" position="30,5" size="981,45" transparent="1" />
  <widget name="config" position="15,60" size="1015,647" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="1" />
  <widget source="key_red" render="Label" position="45,858" zPosition="2" size="165,32" font="RSQFont;30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <widget source="key_green" render="Label" position="265,858" zPosition="2" size="165,32" font="RSQFont;30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <!--widget source="key_yellow" render="Label" position="480,858" zPosition="2" size="200,32" font="RSQFont;30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <widget source="key_blue" render="Label" position="700,858" zPosition="2" size="200,32" font="RSQFont;30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" /-->
  <ePixmap position="45,890" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/red.png" alphatest="blend" />
  <ePixmap position="265,890" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/green.png" alphatest="blend" />
  <!--ePixmap position="480,890" zPosition="1" size="200,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/yellow.png" alphatest="blend" />
  <ePixmap position="700,890" zPosition="1" size="200,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/blue.png" alphatest="blend" /-->
  <widget source="help" render="Label" position="45,612" size="554,225" font="Regular;28" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="613,612" size="400,225" zPosition="5" alphatest="on"/>
  <ePixmap position="712,625" size="200,200" zPosition="3" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/fairbirdfhd.png" alphatest="blend" />
 </screen>
"""
else:
      SKIN_setup_FHD = """
<screen backgroundColor="#16000000" name="RaedQuickSignal_setup" position="center,center" size="1050,899" title="RAED's RaedQuickSignal setup" flags="wfNoBorder">
  <eLabel position="0,53" size="1050,1" zPosition="10" backgroundColor="#00ffffff" transparent="0"/>
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bab329" position="30,5" size="981,45" transparent="1" />
  <widget name="config" position="15,60" size="1015,647" foregroundColor="#ffffff" backgroundColor="#16000000" foregroundColorSelected="#ffffff" backgroundColorSelected="#0e6382" scrollbarMode="showOnDemand" transparent="1" zPosition="1" font="RSQFont;30" itemHeight="40" />
  <widget source="key_red" render="Label" position="45,858" zPosition="2" size="165,32" font="RSQFont;30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <widget source="key_green" render="Label" position="265,858" zPosition="2" size="165,32" font="RSQFont;30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <!--widget source="key_yellow" render="Label" position="480,858" zPosition="2" size="200,32" font="RSQFont;30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" />
  <widget source="key_blue" render="Label" position="700,858" zPosition="2" size="200,32" font="RSQFont;30" halign="center" valign="center" backgroundColor="#54111112" foregroundColor="#00f0f0f0" transparent="1" /-->
  <ePixmap position="45,890" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/red.png" alphatest="blend" />
  <ePixmap position="265,890" zPosition="1" size="165,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/green.png" alphatest="blend" />
  <!--ePixmap position="480,890" zPosition="1" size="200,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/yellow.png" alphatest="blend" />
  <ePixmap position="700,890" zPosition="1" size="200,2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/blue.png" alphatest="blend" /-->
  <widget source="help" render="Label" position="45,612" size="554,225" font="Regular;28" foregroundColor="#00e5b243" backgroundColor="#16000000" valign="center" transparent="1" zPosition="5"/>
  <widget name="Picture" position="613,612" size="400,225" zPosition="5" alphatest="on"/>
  <ePixmap position="712,625" zPosition="3" size="200,200" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/fairbirdfhd.png" alphatest="blend" />
 </screen>
"""

### SKIN_WeatherLocation
SKIN_WeatherLocation = """
<screen backgroundColor="#16000000" name="WeatherLocationChoiceList" position="center,center" size="1280,720" title="Location list" flags="wfNoBorder">
			<widget source="Title" render="Label" position="70,47" size="950,43" font="RSQFont;35" transparent="1" />
			<widget name="choicelist" position="70,115" size="700,480" scrollbarMode="showOnDemand" scrollbarWidth="6" transparent="1" />
			<eLabel position=" 55,675" size="290, 5" zPosition="-10" backgroundColor="#00ff2525" />
			<eLabel position="350,675" size="290, 5" zPosition="-10" backgroundColor="#00389416" />
			<eLabel position="645,675" size="290, 5" zPosition="-10" backgroundColor="#00bab329" />
			<eLabel position="940,675" size="290, 5" zPosition="-10" backgroundColor="#000080ff" />
			<widget name="key_red" position="70,635" size="260,25" zPosition="1" font="RSQFont;20" halign="left" foregroundColor="#00f0f0f0" transparent="1" />
			<widget name="key_green" position="365,635" size="260,25" zPosition="1" font="RSQFont;20" halign="left" foregroundColor="#00f0f0f0" transparent="1" />
		</screen>
"""

### SKIN_AGC_Picon
SKIN_AGC_Picon_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="RSQFont; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="RSQFont; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_AGC_Picon_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="RSQFont; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_AGC_Picon_SNRdB_FHD = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="RSQFont; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="753,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""
SKIN_AGC_Picon_NOSNRdB_FHD = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="753,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""

### SKIN_AGC_Event_Des
SKIN_AGC_Event_Des_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Event_Des" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="RSQFont; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="RSQFont; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="185,403" size="410,65" font="RSQFont; 18" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
 <widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_AGC_Event_Des_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Event_Des" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="RSQFont; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="185,403" size="410,65" font="RSQFont; 18" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
 <widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_AGC_Event_Des_SNRdB_FHD = """
 <screen backgroundColor="#16000000" name="AGC_Event_Des" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="RSQFont; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="340,625" size="810,120" font="RSQFont; 28" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
   <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""
SKIN_AGC_Event_Des_NOSNRdB_FHD = """
 <screen backgroundColor="#16000000" name="AGC_Event_Des" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="340,625" size="810,120" font="RSQFont; 28" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
   <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""

### SKIN_AGC_Weather
SKIN_AGC_Weather_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="RSQFont; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="RSQFont; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="180,400" size="80,22" font="RSQFont; 20" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="171,420" size="58,58" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="233,449" size="200,25" font="RSQFont; 17" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="236,420" size="77,30" font="RSQFont; 24" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="416,445" size="40,33" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/wind.png" />
<widget source="session.CurrentService" render="Label" position="336,436" size="80,30" font="RSQFont; 16" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="410,405" size="30,30" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/humd.png" />
<widget source="session.CurrentService" render="Label" position="329,405" size="80,30" font="RSQFont; 20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/rise.png" position="456,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="456,440" size="60,25" font="RSQFont;20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/set.png" position="530,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="530,440" size="60,25" font="RSQFont;20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_AGC_Weather_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="RSQFont; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="180,400" size="80,22" font="RSQFont; 20" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="171,420" size="58,58" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="233,449" size="200,25" font="RSQFont; 17" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="236,420" size="77,30" font="RSQFont; 24" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="416,445" size="40,33" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/wind.png" />
<widget source="session.CurrentService" render="Label" position="336,436" size="80,30" font="RSQFont; 16" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="410,405" size="30,30" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/humd.png" />
<widget source="session.CurrentService" render="Label" position="329,405" size="80,30" font="RSQFont; 20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/rise.png" position="456,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="456,440" size="60,25" font="RSQFont;20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/set.png" position="530,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="530,440" size="60,25" font="RSQFont;20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_AGC_Weather_SNRdB_FHD = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="RSQFont; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="332,613" size="241,32" font="RSQFont; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,645" size="100,100" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,691" size="400,40" font="RSQFont; 30" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,636" size="150,60" font="RSQFont; 45" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="775,694" size="50,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/wind_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,693" size="147,50" font="RSQFont; 30" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="760,625" size="60,60" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/humd_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,631" size="147,50" font="RSQFont; 35" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/risefhd.png" position="850,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="850,699" size="130,35" font="RSQFont;32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/setfhd.png" position="1000,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1000,699" size="130,35" font="RSQFont;32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
    <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""

SKIN_AGC_Weather_NOSNRdB_FHD = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="332,613" size="241,32" font="RSQFont; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,645" size="100,100" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,691" size="400,40" font="RSQFont; 30" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,636" size="150,60" font="RSQFont; 45" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="775,694" size="50,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/wind_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,693" size="147,50" font="RSQFont; 30" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="760,625" size="60,60" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/humd_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,631" size="147,50" font="RSQFont; 35" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/risefhd.png" position="850,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="850,699" size="130,35" font="RSQFont;32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/setfhd.png" position="1000,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1000,699" size="130,35" font="RSQFont;32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""

### SKIN_Event_Progress_Picon
SKIN_Event_Progress_Picon_SNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="RSQFont; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="RSQFont;30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_Event_Progress_Picon_NOSNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="RSQFont;30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_Event_Progress_Picon_SNRdB_FHD = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="RSQFont; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="RSQFont;35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="753,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
   <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""

SKIN_Event_Progress_Picon_NOSNRdB_FHD = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="RSQFont;35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconProv" position="547,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/piconSat" position="753,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
   <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""

### SKIN_Event_Progress_Event_Des
SKIN_Event_Progress_Event_Des_SNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="RSQFont; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="RSQFont;30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="185,403" size="410,65" font="RSQFont; 18" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
 <widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_Event_Progress_Event_Des_NOSNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="RSQFont;30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="185,403" size="410,65" font="RSQFont; 18" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
 <widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_Event_Progress_Event_Des_SNRdB_FHD = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="RSQFont; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="RSQFont;35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="340,625" size="810,120" font="RSQFont; 28" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
   <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""
SKIN_Event_Progress_Event_Des_NOSNRdB_FHD = """
<screen backgroundColor="#16000000" name="Event_Progress_Event_Des" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="RSQFont;35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Event Description -->
  <widget source="session.Event_Now" render="Label" position="340,625" size="810,120" font="RSQFont; 28" halign="center" foregroundColor="#00bbbbbb" backgroundColor="#54111112" transparent="1">
      <convert type="EventName">ExtendedDescription</convert>
  </widget>
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
   <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""

### SKIN_Event_Progress_Weather
SKIN_Event_Progress_Weather_SNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="RSQFont; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="RSQFont;30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="180,400" size="80,22" font="RSQFont; 20" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="171,420" size="58,58" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="233,449" size="200,25" font="RSQFont; 17" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="236,420" size="77,30" font="RSQFont; 24" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="416,445" size="40,33" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/wind.png" />
<widget source="session.CurrentService" render="Label" position="336,436" size="80,30" font="RSQFont; 18" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="410,405" size="30,30" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/humd.png" />
<widget source="session.CurrentService" render="Label" position="329,405" size="80,30" font="RSQFont; 20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/rise.png" position="456,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="456,440" size="60,25" font="RSQFont;20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/set.png" position="530,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="530,440" size="60,25" font="RSQFont;20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_Event_Progress_Weather_NOSNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="RSQFont;30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="180,400" size="80,22" font="RSQFont; 20" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="171,420" size="58,58" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="233,449" size="200,25" font="RSQFont; 17" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="236,420" size="77,30" font="RSQFont; 24" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="416,445" size="40,33" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/wind.png" />
<widget source="session.CurrentService" render="Label" position="336,436" size="80,30" font="RSQFont; 18" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="410,405" size="30,30" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/humd.png" />
<widget source="session.CurrentService" render="Label" position="329,405" size="80,30" font="RSQFont; 20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/rise.png" position="456,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="456,440" size="60,25" font="RSQFont;20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/set.png" position="530,405" size="60,30" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="530,440" size="60,25" font="RSQFont;20" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_Event_Progress_Weather_SNRdB_FHD = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="RSQFont; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="RSQFont;35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="332,613" size="241,32" font="RSQFont; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,645" size="100,100" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,691" size="400,40" font="RSQFont; 30" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,636" size="150,60" font="RSQFont; 45" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="775,694" size="50,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/wind_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,693" size="147,50" font="RSQFont; 30" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="760,625" size="60,60" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/humd_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,631" size="147,50" font="RSQFont; 35" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/risefhd.png" position="850,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="850,699" size="130,35" font="RSQFont;32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/setfhd.png" position="1000,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1000,699" size="130,35" font="RSQFont;32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
   <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""
SKIN_Event_Progress_Weather_NOSNRdB_FHD = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="RSQFont;35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
<!-- Weather -->
<!-- Today -->
<widget source="session.CurrentService" render="Label" position="332,613" size="241,32" font="RSQFont; 30" zPosition="3" halign="center" valign="center" foregroundColor="#00ffffff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Day</convert>
    </widget>
<widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="RaedQuickSignal/PICONS/weather" position="326,645" size="100,100" zPosition="3" transparent="1" alphatest="blend">
      <convert type="RaedQuickWeather">Picon</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,691" size="400,40" font="RSQFont; 30" zPosition="3" halign="left" valign="center" foregroundColor="#00f37104" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Location</convert>
    </widget>
<widget source="session.CurrentService" render="Label" position="424,636" size="150,60" font="RSQFont; 45" zPosition="3" halign="center" valign="center" foregroundColor="#ff0000" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Temp</convert>
    </widget>
<ePixmap position="775,694" size="50,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/wind_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,693" size="147,50" font="RSQFont; 30" zPosition="3" halign="center" valign="center" foregroundColor="#0000ff00" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Windspeed</convert>
    </widget>
<ePixmap position="760,625" size="60,60" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/humd_fhd.png" />
<widget source="session.CurrentService" render="Label" position="627,631" size="147,50" font="RSQFont; 35" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
      <convert type="RaedQuickWeather">Humidity</convert>
    </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/risefhd.png" position="850,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="850,699" size="130,35" font="RSQFont;32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunrise</convert>
  </widget>
  <ePixmap alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/PICONS/weather/setfhd.png" position="1000,628" size="130,60" zPosition="2"/>
  <widget source="session.CurrentService" render="Label" position="1000,699" size="130,35" font="RSQFont;32" zPosition="3" halign="center" valign="center" foregroundColor="#0000deff" backgroundColor="#54111112" transparent="1" noWrap="1">
    <convert type="RaedQuickWeather">Sunset</convert>
  </widget>
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
   <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""

### SKIN_AGC_Picon_media
SKIN_AGC_Picon_media_SNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="RSQFont; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="RSQFont; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_AGC_Picon_media_NOSNRdB = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,112" size="80,35" font="RSQFont; 25" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,112" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_AGC_Picon_media_SNRdB_FHD = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="RSQFont; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="547,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="753,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""
SKIN_AGC_Picon_media_NOSNRdB_FHD = """
<screen backgroundColor="#16000000" name="AGC_Picon" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- AGC -->
  <eLabel name="agc" text="AGC:" position="0,117" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,112" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">AGC</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="547,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="753,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""

### SKIN_Event_Progress_Picon_media
SKIN_Event_Progress_Picon_media_SNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="284,15" zPosition="2" size="200,35" font="RSQFont; 30" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="RSQFont;30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_Event_Progress_Picon_media_NOSNRdB = """
<screen backgroundColor="#16000000" name="Event_Progress_Picon" position="210,130" size="800,470" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;23" foregroundColor="#00bbbbbb" position="0,0" size="350,30" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="545,0" size="250,30" font="RSQFont;23" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
<convert type="ClockToText">Format:%d-%m-%Y   %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,55" size="80,35" font="RSQFont; 25" halign="center" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="85,50" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="690,55" size="110,35" font="RSQFont; 25" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="85,105" size="600,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="88,105" size="600,50" font="RSQFont;30" valign="center"  backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="85,337" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,368" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="85,397" size="600,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="85,171" size="600,150" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,341" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="656,341" size="80,25" font="RSQFont; 22" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="85,370" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="85,373" size="600,25" font="RSQFont; 20" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="4,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="8,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="12,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="16,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="20,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="25,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="30,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="35,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="40,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="45,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="50,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="55,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="60,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="65,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="70,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="75,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="80,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="85,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="90,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="95,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="100,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="200,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="250,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="400,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="550,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="580,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,188" size="650,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position = "740,340" size = "45,30" zPosition = "4" alphatest = "blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu.png" />
  <!-- Picon -->
  <ePixmap position="185,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="185,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="288,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="288,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="390,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="390,402" size="100,60" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="495,402" size="100,60" zPosition="5" transparent="1" alphatest="on" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="495,402" size="100,60" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="0,400" size="180,22" font="RSQFont; 18" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,420" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="0,443" size="180,22" font="RSQFont; 16" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="599,403" size="200,25" font="RSQFont; 20" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="599,435" size="200,23" font="RSQFont; 18" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
<widget name="Satfinder" position="5,319" size="300,18" zPosition="1" font="RSQFont;17" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1" />
</screen>
"""
SKIN_Event_Progress_Picon_media_SNRdB_FHD = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="559,05" zPosition="2" size="400,45" font="RSQFont; 40" foregroundColor="#00f23d21" halign="center" valign="center" transparent="1">
    <convert type="RaedQuickFrontendInfo2">SNRdB</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="RSQFont;35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="547,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="753,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
  <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""
SKIN_Event_Progress_Picon_media_NOSNRdB_FHD = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="230,205" size="1500,750" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
  <widget source="Title" render="Label" font="RSQFont;35" foregroundColor="#00bbbbbb" position="10,5" size="400,40" transparent="1" />
  <widget source="global.CurrentTime" render="Label" position="1160,5" size="338,40" font="RSQFont;32" valign="top" halign="left" foregroundColor="#00bbbbbb" transparent="1">
        <convert type="ClockToText">Format:%d-%m-%Y    %H:%M:%S</convert>
  </widget>
  <!-- SNR -->
  <eLabel name="snr" text="SNR:" position="0,59" size="150,40" font="RSQFont; 35" halign="right" foregroundColor="#00bbbbbb" transparent="1" />
  <widget source="session.FrontendStatus" render="Progress" position="160,54" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan2.png" zPosition="2" borderWidth="4" borderColor="#656565">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <widget source="session.FrontendStatus" render="Label" position="1348,59" size="150,40" font="RSQFont; 35" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="FrontendInfo">SNR</convert>
  </widget>
  <!-- Progressbar (current event duration) -->
  <widget source="session.Event_Now" render="Progress" position="160,112" size="1180,50" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/progress.png" zPosition="2" borderWidth="4" borderColor="#656565" >
    <convert type="EventTime">Progress</convert>
  </widget>
  <widget source="session.Event_Now" render="Label" position="160,112" size="1180,50" font="RSQFont;35" valign="center" backgroundColor="#000000" transparent="1" zPosition="3">
    <convert type="EventName">Name</convert>
  </widget>
  <eLabel position="148,512" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,560" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <eLabel position="145,609" size="1200,2" backgroundColor="#00bbbbbb" zPosition="4" />
  <widget source="session.CurrentService" render="Label" position="40,178" size="1400,300" font="RSQFont; 28" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" noWrap="1" halign="center">
    <convert type="RaedQuickEcmInfo">ecmfile</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,514" size="1200,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">caids</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1244,514" size="200,45" font="RSQFont; 32" zPosition="3" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1" valign="top" halign="center">
    <convert type="RaedQuickEcmInfo">activecaid</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="40,564" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#41ff9900" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">pids</convert>
  </widget>
  <!--widget source="session.CurrentService" render="Label" position="40,563" size="1400,45" font="RSQFont; 32" zPosition="2" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" valign="center" halign="center">
    <convert type="RaedQuickEcmInfo">bitrate</convert>
  </widget-->
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="124,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1,10</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="128,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">11,20</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="32,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">21,30</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="136,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">31,40</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">41,50</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="145,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">51,60</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="150,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">61,70</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="155,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">71,80</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="160,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">81,90</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="165,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">91,100</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="170,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">101,200</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="175,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">201,300</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="180,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">301,400</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="185,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">401,500</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="190,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">501,600</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="195,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">601,700</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="300,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">701,800</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="305,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">801,900</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="310,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">901,1000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="315,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">1001,5000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="320,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">5001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="370,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">9001,10000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="620,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">10001,50000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="670,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">50001,100001</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="820,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">100001,150000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="970,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">150001,200000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1000,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">200001,250000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1140,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">250001,319999</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <widget source="session.FrontendStatus" render="Pixmap" position="60,183" size="1350,60" zPosition="2" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_ber-scan_on2.png" transparent="1">
    <convert type="RaedQuickSignalText">BerNum</convert>
    <convert type="ValueRange">320000,320000</convert>
    <convert type="ConditionalShowHide" />
  </widget>
  <ePixmap position="1400,560" size="65,50" zPosition="4" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/menu2.png" />
  <!-- Picon -->
  <ePixmap position="335,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" position="340,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Reference</convert>
  </widget>
  <ePixmap position="540,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconProv" position="547,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <ePixmap position="746,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPiconUni" path="piconSat" position="753,624" size="190,110" zPosition="3" alphatest="on">
    <convert type="RaedQuickServName2">OrbitalPos</convert>
  </widget>
  <ePixmap position="954,619" size="200,120" zPosition="5" transparent="1" alphatest="blend" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/picon_fon2.png" />
  <widget source="session.CurrentService" render="RaedQuickSignalPicEmuF" path="RaedQuickSignal/PICONS/emu" position="961,624" size="190,110" transparent="1" alphatest="blend" zPosition="3" />
  <!-- Number and Channel and Provider -->
  <widget source="session.CurrentService" render="Label" position="2,620" size="330,40" font="RSQFont; 30" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Number</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,660" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="2,700" size="330,40" font="RSQFont; 28" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="1156,625" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="1156,680" size="340,55" font="RSQFont; 25" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
   <widget name="Satfinder" position="5,479" size="500,32" zPosition="1" font="RSQFont;28" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
</screen>
"""

### SKIN_Full_Screen
SKIN_Full_Screen = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="1280,720" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
	<widget source="Title" render="Label" position="30,7" size="734,75" backgroundColor="#16000000" transparent="1" zPosition="1" font="RSQFont;38" valign="center" halign="left"/>
	<widget source="global.CurrentTime" render="Label" position="1050,17" size="225,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="RSQFont;36" valign="center" halign="right">
		<convert type="ClockToText">Format:%-H:%M</convert>
	</widget>
	<widget source="global.CurrentTime" render="Label" position="825,52" size="450,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="RSQFont;24" valign="center" halign="right">
		<convert type="ClockToText">Date</convert>
	</widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="352,353" size="907,95" font="RSQFont; 45" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="492,289" size="237,55" font="RSQFont; 38" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="661,289" size="488,55" font="RSQFont; 38" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="352,478" size="907,95" font="RSQFont; 40" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="354,584" size="907,95" font="RSQFont; 40" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan3.png" position="30,120" size="1240,60" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<eLabel text="SNR:" position="37,120" size="150,60" valign="center" foregroundColor="#00000000" backgroundColor="#00ffffff" transparent="1" font="RSQFont;40"/>
	<widget source="session.FrontendStatus" render="Label" position="1042,120" size="230,60" halign="right" valign="center" transparent="1" font="RSQFont;40">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan3.png" position="30,190" size="1240,60" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="AGC:" position="37,190" size="150,60" valign="center" foregroundColor="#00000000" backgroundColor="#00ffffff" transparent="1" font="RSQFont;40"/>
	<widget source="session.FrontendStatus" render="Label" position="1042,190" size="230,60" halign="right" valign="center" transparent="1" font="RSQFont;40">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="SNR:" position="30,260" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="RSQFont;35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,296" size="300,80" backgroundColor="#16000000" font="RSQFont;75" halign="left" transparent="1">
		<convert type="FrontendInfo">SNRdB</convert>
	</widget>
	<eLabel text="AGC:" position="30,385" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="RSQFont;35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,425" size="300,80" backgroundColor="#16000000" font="RSQFont;75" halign="left" transparent="1">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="BER:" position="30,510" size="180,40" backgroundColor="#16000000" transparent="1" zPosition="5" font="RSQFont;35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,550" size="300,80" font="RSQFont;75" halign="left" backgroundColor="#16000000" transparent="1">
		<convert type="FrontendInfo">BER</convert>
	</widget>
	<widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="30,635" size="300,80" font="RSQFont;75" halign="left" foregroundColor="#00ee00" backgroundColor="#16000000" transparent="1" >
		<convert type="FrontendInfo">LOCK</convert>
		<convert type="ConditionalShowHide"/>
	</widget>
	<widget name="Satfinder" position="30,87" size="507,28" halign="left"  zPosition="1" font="RSQFont;25" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
	</screen>
"""
SKIN_Full_Screen_FHD = """
<screen backgroundColor="#16000000" name="RaedQuickSignalScreen" position="0,0" size="1920,1080" title="Quick Signal Info" zPosition="1" flags="wfNoBorder">
	<widget source="Title" render="Label" position="30,7" size="1860,75" backgroundColor="#16000000" transparent="1" zPosition="1" font="RSQFont;45" valign="center" halign="left"/>
	<widget source="global.CurrentTime" render="Label" position="1665,22" size="225,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="RSQFont;36" valign="center" halign="right">
		<convert type="ClockToText">Format:%-H:%M</convert>
	</widget>
	<widget source="global.CurrentTime" render="Label" position="1440,52" size="450,37" backgroundColor="#16000000" transparent="1" zPosition="1" font="RSQFont;24" valign="center" halign="right">
		<convert type="ClockToText">Date</convert>
	</widget>
  <!-- Channel and mumber and Provider -->
  <widget source="session.CurrentService" render="Label" position="541,532" size="1319,131" font="RSQFont; 60" backgroundColor="#54111112" foregroundColor="#ff0000" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Name</convert>
  </widget>
  <eLabel text="Provider:" position="794,422" size="315,97" font="RSQFont; 55" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center"/>
  <widget source="session.CurrentService" render="Label" position="1081,422" size="488,97" font="RSQFont; 55" backgroundColor="#54111112" foregroundColor="#0000ff00" transparent="1" halign="center">
    <convert type="RaedQuickServName2">Provider</convert>
  </widget>
  <!-- Tuner Info  -->
  <widget source="session.CurrentService" render="Label" position="541,716" size="1319,131" font="RSQFont; 55" halign="center" backgroundColor="#54111112" foregroundColor="#fec000" transparent="1">
    <convert type="RaedQuickServName2">%F %p %Y %M %s</convert>
  </widget>
  <widget source="session.CurrentService" render="Label" position="541,839" size="1319,131" font="RSQFont; 50" halign="center" backgroundColor="#54111112" foregroundColor="#00bbbbbb" transparent="1">
    <convert type="RaedQuickServName2">%c %l %h %m %g %b %e %S</convert>
  </widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan3.png" position="30,150" size="1860,75" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<eLabel text="SNR:" position="37,150" size="150,75" valign="center" foregroundColor="#00000000" backgroundColor="#00ffffff" transparent="1" font="RSQFont;52"/>
	<widget source="session.FrontendStatus" render="Label" position="1552,150" size="330,75" halign="right" valign="center" transparent="1" font="RSQFont;52">
		<convert type="FrontendInfo">SNR</convert>
	</widget>
	<widget source="session.FrontendStatus" render="Progress" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/RaedQuickSignal/images/icons_quick/icon_snr-scan3.png" position="30,240" size="1860,75" borderWidth="1" borderColor="#808888">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="AGC:" position="37,240" size="150,75" valign="center" foregroundColor="#00000000" backgroundColor="#00ffffff" transparent="1" font="RSQFont;52"/>
	<widget source="session.FrontendStatus" render="Label" position="1552,240" size="330,75" halign="right" valign="center" transparent="1" font="RSQFont;52">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="SNR:" position="30,360" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="RSQFont;35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,390" size="450,112" font="RSQFont;108" halign="left" backgroundColor="#16000000" transparent="1">
		<convert type="FrontendInfo">SNRdB</convert>
	</widget>
	<eLabel text="AGC:" position="30,540" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="RSQFont;35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,570" size="450,112" backgroundColor="#16000000" transparent="1" font="RSQFont;108" halign="left">
		<convert type="FrontendInfo">AGC</convert>
	</widget>
	<eLabel text="BER:" position="30,720" size="250,50" backgroundColor="#16000000" transparent="1" zPosition="5" font="RSQFont;35"/>
	<widget source="session.FrontendStatus" render="Label" position="30,750" size="450,112" font="RSQFont;108" halign="left" backgroundColor="#16000000" transparent="1">
		<convert type="FrontendInfo">BER</convert>
	</widget>
	<widget text="LOCK" source="session.FrontendStatus" render="FixedLabel" position="30,900" size="465,135" font="RSQFont;108" halign="left" foregroundColor="#00ee00" backgroundColor="#16000000" transparent="1" >
		<convert type="FrontendInfo">LOCK</convert>
		<convert type="ConditionalShowHide"/>
	</widget>
	<widget name="Satfinder" position="32,92" size="800,50" zPosition="1" font="RSQFont;40" halign="left" backgroundColor="#54111112" foregroundColor="#0000deff" transparent="1"/>
	</screen>"""
