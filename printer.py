#!/usr/bin/env python
import urllib2
import re
from datetime import datetime

response = urllib2.urlopen('https://cardenalprinter.stanford.edu/hp/device/this.LCDispatcher')

html = response.read()
m1 = re.findall('id=\"Text17\".*?>(.*?)</span>', html)
m2 = re.findall('id=\"Text18\".*?>(.*?)</span>', html)

status1 = m1[0]
status2 = m2[0]

if status1.find('Empty') >= 0 or status2.find('Empty') >= 0:
  raise Exception('%s: Printer tray is empty' % datetime.now())
elif status1.find('OK') >= 0 or status2.find('OK'):
  print '%s: Printer is fine' % datetime.now()
else:
  raise Exception('%s: Unknown printer status: %s | %s' % (datetime.now(), status1, status2))

