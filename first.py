import xml.sax.handler as saxhandler
import xml.sax as saxparser
 
class MyReport:
    def __init__(self):
        self.Y = 1
 
class MyCH(saxhandler.ContentHandler):
    def __init__(self, report):
        self.X = 1
        self.report = report
 
    def startDocument(self):
        print 'startDocument'
 
    def startElement(self, name, attrs):
        print 'Element:', name
 
report = MyReport()          #for future use
ch = MyCH(report)
 
xml = """\
<collection>
  <comic title=\"Sandman\" number='62'>
     <writer>Neil Gaiman</writer>
     <penciller pages='1-9,18-24'>Glyn Dillon</penciller>
     <penciller pages="10-17">Charles Vess</penciller>
  </comic>
</collection>
"""
 
print xml
 
saxparser.parseString(xml, ch)
